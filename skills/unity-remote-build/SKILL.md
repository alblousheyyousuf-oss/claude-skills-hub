---
name: unity-remote-build
description: Run Unity builds on the user's PC without screen control, by dropping request files that an Editor script watches (compile, build, save, ping) and reading result files back; then ship the APK. Use when working on a Unity project remotely through file tools, when screen-control permissions reset, or when the user is away from the PC. البناء عن بُعد في يونيتي بملفات طلب.
---
# Unity remote build (file-triggered)

Proven on OmaniLightVR (Unity 6.3 LTS, Quest 3). The user was 100+ km from the PC.

## Pattern
- Editor script (in its **own asmdef**, e.g. `Project.Editor`, so it still compiles when gameplay code is broken) polls `RemoteBuild/request.txt` every few seconds while the Editor is open. First word = command, then a request id: `build 003`.
- Commands: `ping`, `compile` (refresh assets, wait for compilation, report errors), `build` (bump `bundleVersionCode`, set `bundleVersion=0.<code>.0`, disable Unity splash, build signed APK, roll back the version on failure), `save`, plus project-specific helpers.
- Writes: `status.txt` heartbeat every 10 s (state, version, compile errors), `result.txt` (`BUILD_OK`/`BUILD_FAILED`/`COMPILE_OK`/`COMPILE_FAILED` + details), `compile-log.txt`.
- Keystore password is read at build time from a file **outside** the project (`%USERPROFILE%\<app>-pass.txt`); never read or print it.

## Remote workflow
1. Check the connection (list the project dir). Check the heartbeat is fresh (< 1 min); if stale, the Editor is closed: open the project via Unity Hub (needs screen access).
2. Write code locally → commit files to `Assets/...` → **re-read and compare** what arrived.
3. `compile NNN` → read result + log. Then `build NNN` (3–8 min, IL2CPP) → expect `BUILD_OK` + version.
4. Upload (see `quest-alpha-release`).

## Gotchas
- When sending a request with a file-commit tool, use a **new source filename every time** (`req-003.txt`); reusing a name once delivered stale content.
- Build all UI/scene content from code at runtime (a `RuntimeInitializeOnLoadMethod` bootstrap), so remote edits are files only — no Editor clicks, no scene merge conflicts.
- Screen-control permissions reset after reboot or a brief disconnect; file tools don't need approval. Prefer files.
- Some Inspector foldouts (OVRManager) ignore clicks; edit the `.asset` files (e.g. `OculusProjectConfig.asset`) directly.
