---
name: unity-vfx-lightshow
description: Build a real-time organic light show (glowing GPU particle mass, waves of light, hand interaction) for Meta Quest in Unity with URP, VFX Graph and bloom. Use when making glowing particle art, data-sculpture style masses (Refik Anadol/Ouchhh look), bioluminescence, swarms or any VR light show in Unity. عرض ضوئي عضوي في يونيتي للنظارة.
---
# Unity VFX light show for Quest

## Look recipe (what made the WebXR prototype read as "light")
- Many small particles (64k–300k) + **additive** blending + **bloom** (bloom is what browser/Open Brush lacked).
- Dim base glow (the mass is always readable) + bright transient flashes (waves, startles, hand). Too much flash = white blob; none = invisible.
- Motion: curl-noise flow + attraction to moving "lobes" stretched along their velocity (school-of-fish spine) + soft room boundary + floor clamp. Lobes part/rejoin on slow cycles; startle = radial impulse every 7–15 s.
- Flash triggers: wave fronts (|dist−r|<band), front edge of fast lobes, high jerk (threshold high, not the always-on cohesion accel), hand proximity, rare random sparks.

## Unity setup
- URP asset: HDR on, Post-processing on; Volume with **Bloom** (threshold ~0.8, intensity 0.6–1.2, Fast/low quality on Quest); tonemapping Neutral.
- Quest: target 72 Hz; OpenXR + Meta; **Single Pass Instanced**; MSAA 2–4x; Fixed Foveated Rendering medium.
- VFX Graph: GPU Event-free system; Capacity ≈ 131k to start; Update context with *Turbulence* (curl) + *Conform to SDF/Attractor* for lobes; store `flash` in a custom attribute; Output **Particle Quad, Additive**, size by flash; color gradient deep sea blue → cyan → white.
- Expose lobe positions/velocities, wave origin/radius, hand positions as **exposed properties**, driven by one C# MonoBehaviour (`SetVector3`, `SetFloat`).
- Hands: Meta XR Interaction SDK / `OVRSkeleton` fingertip transforms → properties.
- Reflection on water: second VFX output mirrored (y→−y) at low alpha, or a planar mirror only if budget allows.

## Performance budget (Quest 3)
Start 131k particles, measure with OVR Metrics Tool; drop to 65k if <72 fps. Keep overdraw low: small sizes, no huge soft sprites.

## Port from WebXR prototype
Logic map: `uL/uLV` → lobe properties; curl → Turbulence; `flash` → custom attribute with decay `flash *= exp(-dt*3.2)`; waves/startle/hand → properties updated each frame from C#.
