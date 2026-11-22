---
name: procedural-3d-glb
description: Build 3D models (GLB/glTF) procedurally in Python with numpy + trimesh (meshes, vertex colours, baked textures, morph-target animation) from a drawing or idea, for VR viewers, AR, Open Brush import or engines. Use when turning a 2D drawing or concept into a 3D model or simple animated GLB without Blender. تحويل رسمة إلى نموذج ثلاثي الأبعاد.
---
# Procedural GLB with Python

Stack: `numpy`, `trimesh`, `PIL`, `scipy.ndimage.map_coordinates` (sample a drawing as a texture/height map).
- Revolve/loft profiles for caps, vessels; sample the user's drawing for colours; place motifs on surfaces by UV.
- Keep GLB small: JPEG textures (≈1024 px), merge meshes per material, decimate.
- Clamp before powers (e.g. `np.clip(1-g,0,1)**2.2`) — negative bases produce NaN and break the GLB.
- Symmetric ornaments: generate one sector and rotate copies; pin feature centres manually when auto-detection drifts.
- Morph-target animation (bloom/grow) via glTF morph targets; preview with three.js headless (see `headless-preview-capture`).
- Quest viewing: send GLB to the headset (phone → headset file transfer keeps full quality); open in a GLB viewer or import into Open Brush/Unity.
For heavier modelling use Blender headless (`blender -b --python`) — see vendored blender skills.
