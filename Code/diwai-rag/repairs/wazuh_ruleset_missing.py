"""Wazuh's custom alert rules load only if ossec.conf's <ruleset> names the
custom rules and decoders folders. Before 2026-09-13 the block was missing, so
every custom rule (YARA, audit, incident) silently never fired. One change:
put back the approved <ruleset> block, test the configuration, restart Wazuh,
and prove a custom rule fires."""
import base64
import time
from pathlib import Path

from repairkit.context import RepairFailed

ID = "wazuh-ruleset-missing"
TITLE = "Wazuh: load the custom alert rules again"
HOST = "vm"
CARD = "WAZUH_CUSTOM_RULES_NOT_LOADED"
SAY_NO_IF = "Someone is changing Wazuh's settings by hand right now."
MANUAL_RESTORE = ("On the VM: sudo cp /var/ossec/etc/ossec.conf.diwai-repair-<run> /var/ossec/etc/ossec.conf "
                  "(a copy is also in the Mac run folder as backup-ossec.conf), then "
                  "sudo systemctl restart wazuh-manager.")
TEST_RULE = "100230"                         # local_rules.xml: program_name diwai-incident (checked 2026-10-04)
TEST_LINE = "logger -t diwai-incident"       # fired in 2 s on 2026-10-04; level 10, no mail
CONF = "/var/ossec/etc/ossec.conf"
ALERTS = "/var/ossec/logs/alerts/alerts.json"
ANALYSISD = "/var/ossec/bin/wazuh-analysisd"
BLOCK = (Path(__file__).parent / "wazuh_ruleset_missing.data" / "ruleset.xml").read_text().strip()
NEEDED = ("<decoder_dir>etc/decoders</decoder_dir>", "<rule_dir>etc/rules</rule_dir>")


def _p(ctx, path):
    return ctx.options.get("VM_ROOT", "") + path


def _vm(ctx, script):
    return ctx.shell.vm(script, sudo=True)


def _put(ctx, path, data):
    """Replace an existing file on the VM with DATA (bytes), all at once: write a
    copy beside it that keeps the file's owner and mode, then swap it in, so an
    interruption can never leave a half-written file. Sent as base64, so nothing
    in it can be read as shell syntax."""
    b64 = base64.b64encode(data).decode()
    tmp = f"{path}.diwai-tmp"
    return _vm(ctx, f"cp -p {path} {tmp} && echo '{b64}' | base64 -d > {tmp} && mv -f {tmp} {path}")


def _conf_bytes(ctx):
    """Read as base64: a terminal session would turn line endings into \\r\\n and
    the shell strips \\r, so plain text would not be byte-exact."""
    r = _vm(ctx, f"base64 < {_p(ctx, CONF)}")
    if r.returncode != 0:
        raise RepairFailed("Could not read Wazuh's settings on the VM.")
    return base64.b64decode("".join(r.stdout.split()))


def _conf(ctx):
    return _conf_bytes(ctx).decode()


def _block(text):
    start, end = text.find("<ruleset>"), text.find("</ruleset>")
    return (start, end) if start >= 0 and end > start else (-1, -1)


def check(ctx):
    text = _conf(ctx)
    start, end = _block(text)
    if start >= 0 and all(n in text[start:end] for n in NEEDED):
        return None
    return ("Wazuh is not loading the custom alert rules (malware scan, audit and incident alerts). "
            "Put back the approved rules section in its settings, test it, and restart Wazuh (about 1 minute).")


def backup(ctx):
    ctx.save_backup("ossec.conf", _conf_bytes(ctx))
    conf = _p(ctx, CONF)
    if _vm(ctx, f"cp -p {conf} {conf}.diwai-repair-{ctx.run_dir.name}").returncode != 0:
        raise RepairFailed("Could not keep a copy of Wazuh's settings on the VM.")


def apply(ctx):
    text = _conf(ctx)
    start, end = _block(text)
    if start >= 0:
        line_start = text.rfind("\n", 0, start) + 1
        text = text[:line_start] + "  " + BLOCK + text[end + len("</ruleset>"):]
    else:
        close = text.rfind("</ossec_config>")
        if close < 0:
            raise RepairFailed("Wazuh's settings file does not look as expected; nothing was changed.")
        text = text[:close] + "  " + BLOCK + "\n" + text[close:]
    if _put(ctx, _p(ctx, CONF), text.encode()).returncode != 0:
        raise RepairFailed("Could not write the new settings on the VM.")
    if _vm(ctx, f"{_p(ctx, ANALYSISD)} -t").returncode != 0:
        raise RepairFailed("Wazuh's configuration test failed; Wazuh was not restarted.")
    restart = ctx.options.get("FAKE_RESTART") or "systemctl restart wazuh-manager"
    if _vm(ctx, restart).returncode != 0:
        raise RepairFailed("Wazuh did not restart.")


def verify(ctx):
    """The configuration test alone proves nothing (2026-09-13): send a tagged
    line and require the custom rule's alert."""
    marker = f"DIWAI-REPAIR-TEST-{int(time.time())}"
    fake = ctx.options.get("FAKE_ALERT")
    if fake is not None:      # tests: write the alert Wazuh would write
        if fake:
            _vm(ctx, f"echo '{{\"rule\":{{\"id\":\"{fake}\"}},\"full_log\":\"{marker}\"}}' >> {_p(ctx, ALERTS)}")
    else:
        _vm(ctx, f"{TEST_LINE} '{marker} (repair library verification test, not an incident)'")
    deadline = time.time() + ctx.options.get("WAIT", 60)
    while True:
        r = _vm(ctx, f"grep -F '{marker}' {_p(ctx, ALERTS)} | grep -c '\"id\":\"{TEST_RULE}\"'")
        if r.stdout.strip() not in ("", "0"):
            return
        if time.time() > deadline:
            raise RepairFailed(f"The custom test rule {TEST_RULE} did not fire within a minute.")
        time.sleep(1)


def undo(ctx):
    if _put(ctx, _p(ctx, CONF), ctx.load_backup("ossec.conf")).returncode != 0:
        raise RepairFailed("Could not put Wazuh's settings back on the VM.")
    restart = ctx.options.get("FAKE_RESTART") or "systemctl restart wazuh-manager"
    if _vm(ctx, restart).returncode != 0:
        raise RepairFailed("Wazuh's settings were put back, but Wazuh did not restart.")
