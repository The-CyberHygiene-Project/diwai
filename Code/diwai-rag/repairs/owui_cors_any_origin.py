"""Open WebUI lets any web site read its answers. CORS_ALLOW_ORIGIN is unset,
so it defaults to '*'; checked 2026-10-03, it echoed http://evil.example back
with credentials allowed. One change: set CORS_ALLOW_ORIGIN to the site's own
address in the launcher, then restart Open WebUI."""
import os
import tempfile
import time

from repairkit.context import RepairFailed

ID = "owui-cors-any-origin"
TITLE = "Open WebUI: allow only its own web address"
HOST = "mac"
CARD = "OPEN_WEBUI_ACCEPTS_ANY_ORIGIN"
SAY_NO_IF = "Someone is in the middle of a conversation in Open WebUI: the restart interrupts it."
MANUAL_RESTORE = ("Copy backup-open-webui-start from the run folder back to /usr/local/sbin/open-webui-start "
                  "(sudo install -m 755 -o root -g wheel <backup> /usr/local/sbin/open-webui-start), then "
                  "restart Open WebUI: launchctl kickstart -k gui/501/org.diwai.open-webui")
SITE = "https://ai.[DOMAIN.ORG]"
LINE = f"export CORS_ALLOW_ORIGIN={SITE}"
WARNING = "CORS_ALLOW_ORIGIN IS SET TO '*'"
DEFAULTS = {"LAUNCHER": "/usr/local/sbin/open-webui-start", "URL": "http://127.0.0.1:3000",
            "LOG": os.path.expanduser("~/Library/Logs/open-webui.log"),
            "KEY_FILE": os.path.expanduser("~/.config/diwai/owui-api-key"), "WAIT": 60}


def _o(ctx, key):
    return ctx.options.get(key, DEFAULTS[key])


def _allows(ctx, origin):
    """True if Open WebUI tells a browser that ORIGIN may read its answers."""
    r = ctx.shell.mac(["/usr/bin/curl", "-s", "-o", "/dev/null", "-D", "-", "-H", f"Origin: {origin}",
                       _o(ctx, "URL") + "/api/version"])
    for line in r.stdout.replace("\r", "").splitlines():
        if line.lower().startswith("access-control-allow-origin:"):
            value = line.split(":", 1)[1].strip()
            if value == "*" or value == origin:     # "*" means any site may read
                return True
    return False


def check(ctx):
    if not _allows(ctx, "http://evil.example"):
        return None
    return (f"Open WebUI lets any web site read its answers. Add one line to its launcher so that only "
            f"{SITE} may, then restart Open WebUI (about 20 seconds).")


def backup(ctx):
    with open(_o(ctx, "LAUNCHER"), "rb") as fh:
        ctx.save_backup("open-webui-start", fh.read())


def _write_launcher(ctx, data):
    r = ctx.shell.mac(["/usr/bin/tee", _o(ctx, "LAUNCHER")], sudo=True, input=data, binary=True)
    if r.returncode != 0:
        raise RepairFailed("Could not write Open WebUI's launcher.")


def _restart(ctx):
    ctx.shell.mac(["/bin/launchctl", "kickstart", "-k", f"gui/{os.getuid()}/org.diwai.open-webui"])


def apply(ctx):
    with open(_o(ctx, "LAUNCHER"), "rb") as fh:
        lines = fh.read().splitlines(keepends=True)
    exports = [i for i, line in enumerate(lines) if line.startswith(b"export ")]
    if not exports:
        raise RepairFailed("Open WebUI's launcher does not look as expected (no settings lines).")
    lines.insert(exports[-1] + 1, LINE.encode() + b"\n")
    ctx.log_mark = os.path.getsize(_o(ctx, "LOG"))   # read only what is logged after the restart
    _write_launcher(ctx, b"".join(lines))
    _restart(ctx)


def verify(ctx):
    deadline = time.time() + _o(ctx, "WAIT")
    while True:
        r = ctx.shell.mac(["/usr/bin/curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
                           _o(ctx, "URL") + "/health"])
        if r.stdout.strip() == "200":
            break
        if time.time() > deadline:
            raise RepairFailed("Open WebUI did not come back within 60 seconds.")
        time.sleep(2)
    if _allows(ctx, "http://evil.example"):
        raise RepairFailed("Open WebUI still lets other web sites read its answers.")
    if not _allows(ctx, SITE):
        raise RepairFailed(f"Open WebUI no longer answers its own site {SITE}.")
    with open(_o(ctx, "LOG"), errors="replace") as fh:
        fh.seek(getattr(ctx, "log_mark", 0))
        if WARNING in fh.read():
            raise RepairFailed("Open WebUI still warns that it accepts any site.")
    # The key goes to curl through a private header file, never on its command
    # line, where any local account could read it in the process list.
    with open(_o(ctx, "KEY_FILE")) as fh:
        key = fh.read().strip()
    with tempfile.NamedTemporaryFile("w", prefix="diwai-hdr-") as hdr:
        hdr.write(f"Authorization: Bearer {key}\n")
        hdr.flush()
        r = ctx.shell.mac(["/usr/bin/curl", "-s", "-H", f"@{hdr.name}", _o(ctx, "URL") + "/api/models"])
    if '"diwai-library"' not in r.stdout:
        raise RepairFailed("Open WebUI came back without its DIWAI Library assistant.")


def undo(ctx):
    _write_launcher(ctx, ctx.load_backup("open-webui-start"))
    _restart(ctx)
