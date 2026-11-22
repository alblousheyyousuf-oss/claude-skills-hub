---
name: openbrush-lua-plugins
description: Write, debug and simulate Open Brush (Tilt Brush successor) Lua plugins for Quest, especially Background plugins that draw and animate artwork. Use when the user wants something drawn or animated inside Open Brush, a plugin doesn't appear or does nothing, or results on the headset differ from expectations. إضافات Lua لبرنامج Open Brush.
---
# Open Brush Lua plugins (v2.3x)

## Install & run (tell the user exactly)
- File in `Open Brush/Plugins/`, name **ASCII only** and exact: `BackgroundScript.Name.lua` (browsers add " (1).txt" — check). Comments ASCII too.
- Extras → Plugins and Scripts → Background row → pick → **eye button** → **big button**.
- Show status with `App:Error("Name: on/growing.../alive")` (appears on the controller) and wrap `Main` in `pcall` reporting the error once.

## API facts (from the C# source)
- `path:DrawWithBrush(brush, size, color, smoothing, layer)`; size is absolute (not clamped); the **last path point is dropped** → duplicate it; point rotation = pen orientation; point scale = pressure.
- Points are stored in the **target layer's local space** (stroke is parented to the layer): draw in "sky-local" coords into a rotating layer.
- Layer pose = TRS; `layer.transform = Transform:New(pos, rot, scale)` sets all at once (cheaper). `CenterPivot` moves pivot to bounds centre and shifts strokes. `Layer:New()` makes it active — restore the active layer. Show/Hide are cheap.
- `Brush.size` is 0..1; `Brush.sizeAbsolute` is real. `Brush.direction` = pointing direction. Unity is left-handed: north-left-of-east = cross(E, Up).
- No date/clock (SoftSandbox: no os); no sound API (only importing a video widget); lowercase `math` IS available and is far cheaper than `Math:`.
- Avoid: drawing thousands of points at once, `allowStrokeAnimation` before drawing, shader clipping/dissolve (made everything invisible on device).

## Looks (verify on device!)
Hull brushes are **faceted** (gem/rock look). Lofted is a 4-sided ribbon. **Icing** = smooth round tube (pressure = radius) → soft beans/drops. **Dots** on device = sharp short dashes, not soft dots. Unlit Hull = flat colour. Calibrate with a numbered sample row before choosing (see `honest-preview`).

## Performance
MoonSharp interpreter is slow: count VM instructions per frame in a simulator; keep ≲40k at default. Draw once (budget 1–6 strokes/frame), then only move/scale/show layers; plain number arrays, no per-frame tables; neighbour checks in round-robin slices; half the objects integrated per frame with extrapolation.
