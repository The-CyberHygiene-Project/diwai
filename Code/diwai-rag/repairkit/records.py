"""Run folders under paths.runs (root-only in production). Every write goes
through shell.mac(..., sudo=True), so tests (sudo_prefix=[]) use a temp folder."""
import json
import time
from pathlib import Path


class RunStore:
    def __init__(self, paths, shell):
        self.paths, self.shell = paths, shell

    def _root(self, argv, data=None, binary=False):
        r = self.shell.mac(argv, sudo=True, input=data, binary=binary)
        if r.returncode != 0:
            raise OSError(f"{' '.join(argv)} failed: {r.stderr!r}")
        return r

    def lock(self):
        """True if taken; "held" if another run holds it; "error" if sudo or the
        folder refused (so a refused password is not mistaken for a busy lock)."""
        lock = str(self.paths.runs / ".lock")
        if self.shell.mac(["/bin/mkdir", lock], sudo=True).returncode == 0:
            return True
        held = self.shell.mac(["/bin/test", "-d", lock], sudo=True).returncode == 0
        return "held" if held else "error"

    def lock_since(self):
        """When a lock left in place was taken, or None if there is no lock."""
        r = self.shell.mac(["/usr/bin/stat", "-f", "%Sm", str(self.paths.runs / ".lock")], sudo=True)
        return r.stdout.strip() if r.returncode == 0 else None

    def unlock(self):
        self.shell.mac(["/bin/rmdir", str(self.paths.runs / ".lock")], sudo=True)

    def new_run(self, repair_id):
        run = self.paths.runs / f"{time.strftime('%Y%m%d-%H%M%S')}-{repair_id}"
        self._root(["/usr/bin/install", "-d", "-m", "700", str(run)])
        return run

    def write_file(self, run, name, data):
        self._root(["/usr/bin/tee", str(Path(run) / name)], data=data, binary=True)

    def read_file(self, run, name):
        return self._root(["/bin/cat", str(Path(run) / name)], binary=True).stdout

    def save(self, run, record):
        self.write_file(run, "record.json", json.dumps(record, indent=1).encode())

    def load(self, run):
        return json.loads(self.read_file(run, "record.json"))

    def runs(self):
        r = self.shell.mac(["/bin/ls", "-1", str(self.paths.runs)], sudo=True)
        names = [n for n in r.stdout.split() if not n.startswith(".")]
        return [self.paths.runs / n for n in sorted(names, reverse=True)]
