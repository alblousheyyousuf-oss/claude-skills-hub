---
name: honest-preview
description: Make previews match what the user will really see on the device, and say plainly what a preview can and cannot predict. Use when building simulators/emulators, recording previews of VR/AR/engine content, or when the user says the result on the headset differs from the preview. المعاينة الصادقة: ما يراه المستخدم يطابق المعاينة.
---
# Honest preview

Lesson: an Open Brush simulator predicted *positions and motion* exactly but *guessed brush looks* (Dots drew round dots; the headset drew sharp dashes). The user lost trust.

1. **List what the preview models exactly vs. approximately** (geometry/timing vs. shaders, textures, bloom, lighting, environment) and tell the user in one line when you send it.
2. **Calibrate before relying on looks:** build a tiny test (one sample of each candidate brush/material/effect, numbered) and ask for a real photo/video from the device first. Match the preview to it.
3. **Prefer pipelines whose preview *is* the product:** the same engine/shader on desktop and device (WebXR page, Unity build) beats a hand-written emulator.
4. **Say which version a video shows** (browser vs app vs plugin) in the filename and caption.
5. When the user reports a difference: watch their video first (contact sheet of 12 frames), name the concrete difference, explain the cause, propose a calibration step — before rebuilding.
