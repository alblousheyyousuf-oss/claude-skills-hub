#!/usr/bin/env bash
# Install bundles of skills into ~/.claude/skills (or $DEST). Each installed skill's description is loaded into every
# session, so install only the bundles you need.
# usage: ./install.sh core unity webxr      |  ./install.sh list
set -e
DEST="${DEST:-$HOME/.claude/skills}"
HERE="$(cd "$(dirname "$0")" && pwd)"
declare -A B=(
  [core]="skills"
  [unity]="vendor/gomesgustavoo__vr-dev-skills vendor/CoplayDev__unity-mcp vendor/scenario-labs__skills/game-engines/unity"
  [blender]="vendor/EL4CTEO__blender-skills"
  [blender-extra]="vendor/arjun988__blender-skills vendor/scenario-labs__skills/dcc"
  [webxr]="vendor/viettranx__3dviz-pro-max vendor/anthropics__skills"
  [vfx]="vendor/kanaworksai-hue__effekseer-vfx-skill"
  [godot]="vendor/laurentvv__godot-skill-quality vendor/scenario-labs__skills/game-engines/godot"
  [ai3d]="vendor/scenario-labs__skills"
  [tokens]="vendor/egorfedorov__claude-context-optimizer"
  [optional]="vendor/_optional"
)
if [ "$1" = "list" ] || [ -z "$1" ]; then for k in "${!B[@]}"; do echo "$k: ${B[$k]}"; done; exit 0; fi
mkdir -p "$DEST"
for b in "$@"; do
  for src in ${B[$b]}; do
    find "$HERE/$src" -name SKILL.md | while read -r f; do d="$(dirname "$f")"; n="$(basename "$d")"
      if [ -e "$DEST/$n" ]; then echo "skip (exists): $n"; else cp -r "$d" "$DEST/$n"; echo "installed: $n"; fi; done
  done
done
