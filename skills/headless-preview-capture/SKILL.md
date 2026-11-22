---
name: headless-preview-capture
description: Capture preview frames and videos of WebGL/three.js/simulator scenes headlessly (Playwright + Chromium + ffmpeg) and review them cheaply with contact sheets. Use when you need to see a 3D scene you built, record a preview video for the user, or compare iterations. التقاط معاينات وفيديو بلا شاشة.
---
# Headless preview capture

- Chromium flags: `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`. Preinstalled Playwright: `NODE_PATH=$(npm root -g) node rec.js`.
- Page exposes `__ready`, `__frame(dt)`, `__sync()`; loop: frame → (every k) screenshot JPEG q≈88 → ffmpeg `-framerate 30 -i f%05d.jpg -c:v libx264 -pix_fmt yuv420p -crf 26 -movflags +faststart`.
- Warm-up in chunks of ~10 frames with a sync, or screenshots time out.
- **Review via one contact sheet** (`contact_sheet.py dir out.jpg 0.5`): 6–12 frames at 0.2 s spacing to judge motion, ~1.5 s spacing to judge variety. Read a single full frame only for detail.
- Long recordings: run in background, ~0.1–0.4 s per frame in SwiftShader; reduce particle count for previews.
- Don't `rm -rf dir/*` after `cd` (blocked by safety checks); write to a new folder name instead.
- Before sending a video: check duration/size with ffprobe; keep < ~25 MB.
