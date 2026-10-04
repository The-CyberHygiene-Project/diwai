"""Where the installed library lives. PRODUCTION is fixed: nothing in the
environment may redirect it (a redirected approvals folder would let anyone
approve their own repair)."""
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Paths:
    lib: Path
    runs: Path
    openssl: str = "/usr/bin/openssl"                    # root-owned: does the checking
    fido_assert: str = "/opt/homebrew/bin/fido2-assert"  # signs (PIN + touch); never trusted to check
    fido_lib: str = "/opt/homebrew/opt/libfido2/lib/libfido2.1.dylib"  # loaded by fido2-assert
    rp_id: str = "diwai-repair"

    @property
    def approvals(self):
        return self.lib / "approvals"

    @property
    def approver_pem(self):
        return self.lib / "approver.pem"

    @property
    def approver_credid(self):
        return self.lib / "approver.credid"

    @property
    def fido_pins(self):
        return self.lib / "fido-tools.sha256"

    @property
    def repairs(self):
        return self.lib / "repairs"

    @property
    def kit(self):
        return self.lib / "repairkit"


PRODUCTION = Paths(lib=Path("/usr/local/lib/diwai-repair"),
                   runs=Path("/var/db/diwai-repair/runs"))
