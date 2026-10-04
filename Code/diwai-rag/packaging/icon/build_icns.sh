#!/bin/bash
# Rebuild AppIcon.icns from make_icon.swift.
set -e
cd "$(dirname "$0")"
WORK="$(mktemp -d)"
swift make_icon.swift "$WORK/icon_1024.png"
SET="$WORK/AppIcon.iconset"; mkdir "$SET"
for s in 16 32 128 256 512; do
  sips -z $s $s "$WORK/icon_1024.png" --out "$SET/icon_${s}x${s}.png" >/dev/null
  d=$((s * 2)); sips -z $d $d "$WORK/icon_1024.png" --out "$SET/icon_${s}x${s}@2x.png" >/dev/null
done
iconutil -c icns "$SET" -o "../DIWAI Library.app/Contents/Resources/AppIcon.icns"
cp "$WORK/icon_1024.png" preview.png
rm -rf "$WORK"
echo "built AppIcon.icns"
