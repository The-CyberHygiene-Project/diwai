#!/bin/bash
# repair-approver-signtest.sh -- sign one test file with the approval credential
# (PIN + touch), so Claude can check the signature. Writes only non-secret files.
set -u
B=/opt/homebrew/bin; K="$HOME/.config/diwai/repair-approver"; D="$HOME/.config/diwai/signtest"
dev=$($B/fido2-token -L 2>/dev/null | head -1 | awk -F': ' '{print $1}')
[ -n "$dev" ] || { echo "No YubiKey found. Is it plugged in?"; exit 1; }
mkdir -p "$D"; printf 'diwai repair approval signing test\n' > "$D/test.txt"
{ /usr/bin/openssl dgst -sha256 -binary "$D/test.txt" | /usr/bin/base64; echo "diwai-repair"; cat "$K.credid"; } > "$D/assert.in"
echo "Enter your YubiKey PIN when asked, then touch the YubiKey when it blinks."
/usr/bin/say "Type your YubiKey PIN, then touch the key when it blinks." &
if $B/fido2-assert -G -p -v -i "$D/assert.in" -o "$D/assert.out" "$dev"; then
  echo "RESULT: signed."; else echo "RESULT: NOT signed (wrong PIN, no touch in time, or key unplugged). Nothing was changed."; fi
