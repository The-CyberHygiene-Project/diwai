"""Every command the library runs goes through Shell, so tests can replace
sudo, ssh and the runner itself."""
import shlex
import subprocess
import sys

SUDO = ["/usr/bin/sudo", "--"]
VM = ["/usr/bin/ssh", "-tt", "-o", "BatchMode=yes", "services"]


def _vm_master_alive():
    return subprocess.run(["/usr/bin/ssh", "-O", "check", "services"],
                          capture_output=True).returncode == 0


def _tee_run(argv, **kw):
    """Run ARGV showing its output live (a sudo prompt must be visible) while
    also capturing it."""
    p = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    out = []
    for line in p.stdout:
        sys.stdout.write(line)
        sys.stdout.flush()
        out.append(line)
    p.wait()
    return subprocess.CompletedProcess(argv, p.returncode, "".join(out), "")


class Shell:
    def __init__(self, sudo_prefix=None, vm_prefix=None, runner=None, vm_check=None,
                 vm_runner=None, speaker=None, interactive=None):
        self.sudo_prefix = SUDO if sudo_prefix is None else sudo_prefix
        self.vm_prefix = VM if vm_prefix is None else vm_prefix
        self.runner = runner or subprocess.run
        # Remote VM steps show their output live (the VM's sudo prompt must be seen).
        self.vm_runner = vm_runner or runner or (_tee_run if self.vm_prefix else subprocess.run)
        self.vm_check = vm_check or _vm_master_alive
        self.speaker = speaker
        # Runs a command attached to the person's terminal (nothing captured), so
        # a prompt without a line break, like sudo's, is seen at once.
        self.interactive = interactive or subprocess.run

    def mac(self, argv, sudo=False, input=None, binary=False):
        """BINARY: input and output are bytes, untouched (text mode would turn
        a carriage return into a newline and corrupt a backup)."""
        cmd = (self.sudo_prefix + list(argv)) if sudo else list(argv)
        if binary:
            return self.runner(cmd, input=input, capture_output=True)
        return self.runner(cmd, input=input, capture_output=True, text=True)

    def vm(self, script, sudo=False, show=False):
        """SHOW: stream the output live (needed only when a prompt must be seen).
        Otherwise capture quietly, with errors kept out of the data: a VM file
        read this way may hold secrets and must not be echoed."""
        if self.vm_prefix:   # remote: ssh joins its arguments, so send one quoted string
            prefix = self.vm_prefix if show else [a for a in self.vm_prefix if a != "-tt"]
            # Quiet steps use sudo -n: with no terminal to prompt on, sudo must
            # refuse at once rather than wait for a password nobody can see.
            run_as = ("sudo bash -c " if show else "sudo -n bash -c ") if sudo else "bash -c "
            cmd = prefix + [run_as + shlex.quote(script)]
        else:                # local test mode: the "VM" is a temp folder; sudo_prefix is [] in tests
            cmd = (self.sudo_prefix if sudo else []) + ["bash", "-c", script]
        r = (self.vm_runner if show else self.runner)(cmd, capture_output=True, text=True)
        r.stdout = (r.stdout or "").replace("\r", "")
        return r

    def vm_ready(self):
        return bool(self.vm_check())

    def vm_sudo_start(self):
        """Ask for the VM sudo password once, in the owner's terminal. The VM
        keeps it for at most 2 minutes for this account (sudoers.d/[USERNAME]:
        timestamp_type=global, timestamp_timeout=2). True if accepted."""
        if not self.vm_prefix:
            return True
        return self.interactive(self.vm_prefix + ["sudo -v"]).returncode == 0

    def vm_sudo_end(self):
        """Make the VM forget the sudo password at once."""
        if not self.vm_prefix:
            return
        quiet = [a for a in self.vm_prefix if a != "-tt"]
        self.runner(quiet + ["sudo -K"], capture_output=True, text=True)

    def say(self, text):
        if self.speaker:
            self.speaker(text)
        else:
            subprocess.run(["/usr/bin/say", text], capture_output=True)
