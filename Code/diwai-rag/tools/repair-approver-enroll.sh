#!/bin/bash
# repair-approver-enroll.sh -- create the ISSO's repair-approval credential on the YubiKey.
# Asks for the FIDO2 PIN (at fido2-cred's own prompt, never echoed) and a touch.
# Writes ~/.config/diwai/repair-approver.credid (credential id) and .pem (public key).
# Nothing secret is written: the private key never leaves the YubiKey.
set -u
B=/opt/homebrew/bin; OUT="$HOME/.config/diwai/repair-approver"
dev=$($B/fido2-token -L 2>/dev/null | head -1 | awk -F': ' '{print $1}')
[ -n "$dev" ] || { echo "No YubiKey found. Is it plugged in?"; exit 1; }
[ -e "$OUT.credid" ] && { echo "An approval credential already exists ($OUT.credid). Not replacing it."; exit 1; }
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
{ /usr/bin/openssl rand -base64 32; echo "diwai-repair"; echo "diwai-isso"; /usr/bin/openssl rand -base64 16; } > "$tmp/in"
echo "Enter your YubiKey PIN when asked, then touch the YubiKey when it blinks."
/usr/bin/say "Type your YubiKey PIN, then touch the key when it blinks." &
if ! $B/fido2-cred -M -i "$tmp/in" -o "$tmp/cred" "$dev" es256; then echo "RESULT: NOT created (wrong PIN, no touch within 30 seconds, or key unplugged). Nothing was changed."; exit 1; fi
if ! $B/fido2-cred -V -i "$tmp/cred" -o "$tmp/pub" es256; then echo "RESULT: created, but its attestation did not check out. Tell Claude."; exit 1; fi
umask 022; sed -n 1p "$tmp/pub" > "$OUT.credid"; sed -n '2,$p' "$tmp/pub" > "$OUT.pem"
echo "RESULT: approval credential created."; /usr/bin/openssl ec -pubin -in "$OUT.pem" -noout -text 2>/dev/null | grep -m1 "ASN1 OID"
