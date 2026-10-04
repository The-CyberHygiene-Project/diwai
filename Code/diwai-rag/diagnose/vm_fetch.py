"""Read the VM's latest monitor report through the owner's SSH session. Never sudo."""
import subprocess

NOT_CHECKED = "the VM was not checked: log in with ssh services"
PATH = "/var/lib/diwai-control-health/latest.json"


TIMEOUT = 20            # a VM stuck at its LUKS prompt must not freeze the tool


def fetch_vm_report(runner=subprocess.run):
    """(text, note): text None = no session; "" = could not be read; else the report text."""
    try:
        chk = runner(["/usr/bin/ssh", "-O", "check", "services"], capture_output=True, text=True, timeout=TIMEOUT)
    except (OSError, subprocess.TimeoutExpired):
        return None, NOT_CHECKED
    if chk.returncode != 0:
        return None, NOT_CHECKED
    try:
        r = runner(["/usr/bin/ssh", "-o", "BatchMode=yes", "-o", f"ConnectTimeout={TIMEOUT}", "services",
                    f"cat {PATH}"], capture_output=True, text=True, timeout=TIMEOUT)
    except (OSError, subprocess.TimeoutExpired):
        return "", f"the VM did not answer within {TIMEOUT} seconds"
    if r.returncode != 0:
        return "", "the VM report could not be read"
    return r.stdout, ""
