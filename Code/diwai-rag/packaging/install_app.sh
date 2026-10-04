#!/bin/bash
# Copy the launcher into /Applications. Re-run after changing packaging/.
set -e
SRC="$(cd "$(dirname "$0")" && pwd)/DIWAI Library.app"
DEST="/Applications/DIWAI Library.app"
rm -rf "$DEST"
cp -R "$SRC" "$DEST"
echo "Installed $DEST"
