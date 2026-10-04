default_repair: none
decisions:
objectives: 3.5.3[b]
user_sees: Signing in at the Mac's own keyboard, or in the virtual server's console window, asks only for a password.
means: Anyone who learns an administrator password and sits at the machine gets full control. A second proof of identity would stop them.
evidence: Signing in remotely needs a code from the authenticator app as well as a key. Signing in at the keyboard needs only a password.
repair: No automatic repair. This needs a planned change by the owner, made only after the emergency spare administrator account has been tested the same day.
if_wrong: A mistake in the Mac's sign-in settings has locked the owner out twice before, and recovery meant erasing the Mac and reinstalling everything.
rollback: A sign-in change can be undone from a session that is still open. Once nobody can sign in, it cannot be undone this way.
say_no_if: Someone proposes changing how the Mac's login screen checks people, without first testing the spare administrator account and keeping a second session open.
---
Status as of 2026-08-07 (POA&M v1.32; DIWAI-CR-2026-08-17). Mac sshd requires publickey,keyboard-interactive:pam (pam_google_authenticator), exercised 2026-08-07; Match Address [LAN-IP-REDACTED] reverts to publickey for the VM's automated jobs. VM SSH requires TOTP since 2026-08-04 (POA&M-004 closed). 3.5.3 stands at -3, capped by single-factor console access: loginwindow and the UTM console are password only, and DisableFDEAutoLogin is the same factor twice. Related open item POA&M-060: on the VM, DISALLOW_REUSE and RATE_LIMIT were removed to make TOTP work and scratch codes are unverified. Before any PAM or loginwindow change on the Mac (DIWAI-INC-002: two lockouts ending in DFU reinstall), verify `dscl . -authonly sysadmin` returns silently, keep a second authenticated session open, and have a same-day Time Machine backup.
