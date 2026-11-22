---
name: webxr-quest-art
description: Build, host and test WebXR art pages for the Meta Quest browser with three.js (GPU particles, hand tracking, spatial audio, record mode). Use when making a VR piece that opens from a link, prototyping before an engine build, or recording previews of a three.js scene. صفحات WebXR فنية لمتصفح النظارة.
---
# WebXR art for Quest

## Gotchas (all hit in practice)
- **GPGPU in XR:** `GPUComputationRenderer.compute()` while presenting renders with the XR camera → corrupt sim. Wrap: `xr.enabled=false; gpu.compute(); xr.enabled=true`.
- Use `HalfFloatType` render targets on Quest.
- Additive points: compute pixel size from projection (`px = h/(2 tan(fov/2))`; XR ≈ 950).
- Hands: `renderer.xr.getHand(i).joints['index-finger-tip']` (`visible` when tracked); fall back to `getController(i)`.
- Audio must start on a user gesture; listener from `renderer.xr.getCamera().matrixWorld` when presenting.
- WebGPU in Quest browser is still experimental (2026): ship WebGL2.

## Hosting a GitHub file as a page
`https://rawcdn.githack.com/<user>/<repo>/<commit-sha>/<path>/index.html` — use a **commit SHA** (CDN caches forever). First visit shows a "One more step → Open the page" notice; tell the user. jsDelivr serves HTML as text/plain (doesn't work). GitHub Pages is the clean alternative if the user enables it.

## Record mode (for previews)
Add `?record`: no UI, `window.__frame(dt)` steps deterministically, `window.__sync()` does a 1-px `readPixels` to drain the GPU queue (else screenshots time out after big warm-ups). Capture with Playwright + ffmpeg (see `headless-preview-capture`).

## Structure that worked
`index.html` (Arabic RTL landing, buttons: Enter / Watch on screen, mute) + `main.js` module + data module; importmap → three@0.160 on jsDelivr; URL params for speed/glow/count.
