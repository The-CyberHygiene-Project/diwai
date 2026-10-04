"""diwai-repair: runs only YubiKey-approved repairs (owner decision 13).

Exit codes: 0 done or nothing to do; 1 failed and put back; 2 refused before
any change; 3 undo failed, a person must restore by hand."""
import ast
import importlib.util
import re
import subprocess
import sys
import time

from repairkit import signing
from repairkit.context import Context, RepairFailed
from repairkit.paths import PRODUCTION
from repairkit.records import RunStore
from repairkit.shell import Shell

VM_LOGIN = "NOT RUN. This repair works on the VM. Please log in to the VM first (ssh services)."
VM_PASSWORD = "NOT RUN. The VM password was not accepted (or not typed in time). Nothing was changed."
RUN_NAME = re.compile(r"^\d{8}-\d{6}-([a-z0-9][a-z0-9-]*)$")


def terminal_ask(prompt):
    """A yes must be typed by a person: refuse answers piped in by a program."""
    if not sys.stdin.isatty():
        raise EOFError
    return input(prompt)


def _sudo_sign_out():
    """Forget the cached sudo sign-in, so nothing else in this terminal gets root
    from the password typed for a repair."""
    subprocess.run(["/usr/bin/sudo", "-k"], capture_output=True)


def manual_restore_text(path):
    """Read MANUAL_RESTORE without running the module (used when it is no longer approved)."""
    try:
        tree = ast.parse(path.read_text())
    except (OSError, SyntaxError):
        return "See the repair's runbook card."
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "MANUAL_RESTORE" for t in node.targets):
            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                return node.value.value
    return "See the repair's runbook card."


class Runner:
    def __init__(self, paths, shell, ask=input, out=print, options=None, target=None):
        self.paths, self.shell, self.ask, self.out = paths, shell, ask, out
        self.options, self.target = options or {}, target
        self.store = RunStore(paths, shell)
        self._mods = {}

    # ---- helpers ---------------------------------------------------------
    def load(self, repair_id):
        """Load an installed repair. Callers check its approval first."""
        if repair_id not in self._mods:
            name = signing.module_name(repair_id)
            spec = importlib.util.spec_from_file_location(
                f"diwai_repair_{name}", self.paths.repairs / f"{name}.py")
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            self._mods[repair_id] = mod
        return self._mods[repair_id]

    def _approved(self, repair_id):
        ok, why = signing.verify(self.paths, repair_id)
        if not ok:
            self.out(f"NOT RUN. {why}")
        return ok

    def _ctx(self, run_dir):
        return Context(self.paths, self.shell, self.store, run_dir, self.options, self.target)

    def _record(self, run, rec, state, **extra):
        rec.update(state=state, updated=time.strftime("%Y-%m-%d %H:%M:%S"), **extra)
        self.store.save(run, rec)

    def _ready(self, repair_id):
        """Approved, loaded and reachable, or None (the reason was printed)."""
        if not self._approved(repair_id):
            return None
        mod = self.load(repair_id)
        if mod.HOST == "vm" and not self.shell.vm_ready():
            self.out(VM_LOGIN)
            return None
        return mod

    # ---- commands --------------------------------------------------------
    def cmd_list(self):
        for p in sorted(self.paths.repairs.glob("*.py")):
            rid = p.stem.replace("_", "-")
            ok, why = signing.verify(self.paths, rid)
            self.out(f"{rid:28s} {'approved' if ok else why}")
        return 0

    def _vm_sudo(self, mod, action):
        """Run ACTION; for a VM repair, ask the VM password once first and make
        the VM forget it afterwards, whatever happens."""
        if mod.HOST != "vm":
            return action()
        try:
            if not self.shell.vm_sudo_start():
                self.out(VM_PASSWORD)
                return 2
            return action()
        finally:
            self.shell.vm_sudo_end()

    def cmd_check(self, repair_id):
        mod = self._ready(repair_id)
        if mod is None:
            return 2
        return self._vm_sudo(mod, lambda: self._check(mod))

    def _check(self, mod):
        plan = mod.check(self._ctx(None))
        self.out(f"PROBLEM FOUND: {plan}" if plan else "Not present: nothing to do.")
        return 0

    def cmd_run(self, repair_id):
        mod = self._ready(repair_id)
        if mod is None:
            return 2
        taken = self.store.lock()
        if taken == "held":
            self.out("NOT RUN. Another repair is running. If none is, see 'diwai-repair status'.")
            return 2
        if taken is not True:
            self.out("NOT RUN. Could not take the lock: the password was refused, or the run folder "
                     "is missing. Nothing was changed.")
            return 2
        try:
            return self._vm_sudo(mod, lambda: self._run_locked(repair_id, mod))
        finally:
            self.store.unlock()

    def _run_locked(self, repair_id, mod):
        plan = mod.check(self._ctx(None))
        if not plan:
            self.out("Not present: nothing to do.")
            return 0
        # The plan is text from the system: shown to the person, never acted on.
        self.out(f"{mod.TITLE}\nPLANNED CHANGE: {plan}\nSAY NO IF: {mod.SAY_NO_IF}")
        try:
            answer = self.ask("Type yes to make this change: ")
        except (EOFError, KeyboardInterrupt):   # Ctrl-D or Ctrl-C: a cancel, not a failure
            answer = ""
        if answer != "yes":
            self.out("Cancelled. Nothing was changed.")
            return 2
        run = self.store.new_run(repair_id)
        rec = {"repair": repair_id, "run": run.name, "plan": plan,
               "started": time.strftime("%Y-%m-%d %H:%M:%S")}
        ctx = self._ctx(run)
        self._record(run, rec, "started")
        try:
            mod.backup(ctx)
        except Exception as exc:   # nothing was changed yet: nothing to undo
            reason = str(exc) if isinstance(exc, RepairFailed) else f"{type(exc).__name__}: {exc}"
            self._record(run, rec, "failed-nothing-changed", error=reason, log=ctx.lines)
            self.out(f"FAILED before any change: {reason}. Nothing was changed.")
            return 1
        self._record(run, rec, "backed-up")
        try:
            mod.apply(ctx)
            self._record(run, rec, "applied")
            mod.verify(ctx)
        except KeyboardInterrupt:
            self._record(run, rec, "interrupted", log=ctx.lines)
            self.out(f"INTERRUPTED. To restore: diwai-repair undo {run.name}")
            raise
        except Exception as exc:
            return self._roll_back(mod, ctx, run, rec, exc)
        self._record(run, rec, "done", log=ctx.lines)
        self.out(f"DONE. Run {run.name}. To undo: diwai-repair undo {run.name}")
        return 0

    def _roll_back(self, mod, ctx, run, rec, exc):
        reason = str(exc) if isinstance(exc, RepairFailed) else f"{type(exc).__name__}: {exc}"
        self.out(f"FAILED: {reason}. Putting things back.")
        try:
            mod.undo(ctx)
        except Exception as undo_exc:
            self._record(run, rec, "undo-failed", error=reason, undo_error=str(undo_exc), log=ctx.lines)
            self.out(f"UNDO FAILED. The system may be half-changed. Restore by hand:\n{mod.MANUAL_RESTORE}\n"
                     f"Backups are in {run}.")
            return 3
        still = mod.check(self._ctx(None))
        self._record(run, rec, "failed-rolled-back", error=reason, log=ctx.lines,
                     after_undo="problem present again (as before)" if still else "problem not present")
        self.out("Put back as it was. Nothing is left changed.")
        return 1

    def cmd_undo(self, run_name):
        m = RUN_NAME.match(run_name or "")
        run = self.paths.runs / run_name if m else None
        if run is None or run.parent != self.paths.runs:
            self.out(f"NOT RUN. '{run_name}' is not a run name. See 'diwai-repair status'.")
            return 2
        try:
            rec = self.store.load(run)
        except (OSError, ValueError):
            self.out(f"NOT RUN. No run called '{run_name}'. See 'diwai-repair status'.")
            return 2
        if rec.get("repair") != m.group(1):
            self.out(f"NOT RUN. The record in '{run_name}' does not match its name.")
            return 2
        if not self._approved(rec["repair"]):
            text = manual_restore_text(self.paths.repairs / f"{signing.module_name(rec['repair'])}.py")
            self.out(f"To restore by hand:\n{text}\nBackups are in {run}.")
            return 2
        mod = self.load(rec["repair"])
        if mod.HOST == "vm" and not self.shell.vm_ready():
            self.out(VM_LOGIN)
            return 2
        return self._vm_sudo(mod, lambda: self._undo(mod, run, rec, run_name))

    def _undo(self, mod, run, rec, run_name):
        self.out(f"{mod.TITLE}\nUNDO: put back what run {run_name} changed, from its backup.")
        try:
            answer = self.ask("Type yes to undo it: ")
        except (EOFError, KeyboardInterrupt):
            answer = ""
        if answer != "yes":
            self.out("Cancelled. Nothing was changed.")
            return 2
        try:
            mod.undo(self._ctx(run))
        except Exception as exc:
            self._record(run, rec, "undo-failed", undo_error=str(exc))
            self.out(f"UNDO FAILED: {exc}\nRestore by hand:\n{mod.MANUAL_RESTORE}")
            return 3
        back = mod.check(self._ctx(None))
        after = ("problem present again, as before the repair" if back else
                 "problem not present (something else fixed it, or the undo did not take)")
        self._record(run, rec, "undone", after_undo=after)
        self.out(f"Undone: {run_name}. " + ("The original problem is back, as expected." if back
                 else "Check: the original problem is NOT back; look at this by hand."))
        return 0

    def cmd_status(self):
        since = self.store.lock_since()
        if since:
            self.out(f"A repair lock is in place (since {since}). If no repair is running, a person can "
                     f"clear it with: sudo rmdir {self.paths.runs / '.lock'}")
        for run in self.store.runs()[:20]:
            try:
                state = self.store.load(run).get("state")
            except (OSError, ValueError):
                state = "record unreadable"
            self.out(f"{run.name:45s} {state}")
        return 0


USAGE = ("usage: diwai-repair list | check <repair> | run <repair> | undo <run> | status"
         " | approve <repair> | install")


def main(argv, paths=PRODUCTION):
    if not argv:
        print(USAGE)
        return 2
    try:
        return _dispatch(argv[0], argv[1:], paths)
    finally:
        _sudo_sign_out()


def _dispatch(cmd, args, paths):
    if cmd in ("approve", "install"):
        from repairkit import admin
        return admin.main(cmd, args, paths)
    r = Runner(paths, Shell(), ask=terminal_ask)
    table = {"list": (r.cmd_list, 0), "status": (r.cmd_status, 0), "check": (r.cmd_check, 1),
             "run": (r.cmd_run, 1), "undo": (r.cmd_undo, 1)}
    if cmd in table and len(args) == table[cmd][1]:
        try:
            return table[cmd][0](*args)
        except KeyboardInterrupt:
            return 1
    print(USAGE)
    return 2
