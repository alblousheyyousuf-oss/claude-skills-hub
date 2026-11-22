---
name: unity-quest-setup
description: Guide a beginner through setting up Unity for Meta Quest 3 (Unity 6 LTS, Android modules, Meta XR SDK, URP, developer mode, cable/Wi-Fi deploy) and troubleshoot it. Use when the user wants to build a Quest app, asks how to install or configure Unity for VR, hits developer-mode or device-connection errors, or needs a prompt for a computer-use agent to do the setup. إعداد يونيتي لنظارة كويست 3.
---
# Unity for Meta Quest 3 — beginner setup

Verify menu names against Meta's docs if unsure (they move between Unity versions):
https://developers.meta.com/vr/documentation/unity/unity-project-setup

## Order (one-time, ~1 h, mostly downloads)
1. **Unity Hub → Install Editor → newest *LTS* of Unity 6** (not the newest non-LTS; Meta SDK is tested on LTS). Modules: Android Build Support + OpenJDK + Android SDK & NDK Tools.
2. **Developer org** at developers.meta.com (free). Do **not** create an "App" there — not needed for sideloading.
3. **Developer mode**: Meta Horizon phone app → Devices → headset → Headset settings → Developer mode.
4. **Connect**: USB-C *data* cable (the headset's own charging cable or an original phone cable usually works) → in headset accept *Allow USB debugging → Always allow*. Bluetooth does NOT work for deploying. Wi-Fi ADB is possible after one cable connection (MQDH → ADB over Wi-Fi; same network; phone hotspots may block).
5. **Meta Quest Developer Hub** on PC; headset must show *Connected*.
6. **New project → Universal 3D (URP)** (not Learning templates) → name it.
7. Package Manager: **Meta XR All-in-One SDK** (Asset Store → Add to My Assets → My Assets → Install) + **Visual Effect Graph**.
8. Build Profiles → **Android → Switch Platform**.
9. Meta XR **Project Setup Tool → Fix All → Apply All** (repeat until clean).
10. **Build And Run** an empty scene first. Only then add the artwork.

After the build the app lives in the headset (Library → Unknown Sources) and runs without the PC.

## Troubleshooting
| Symptom | Fix |
|---|---|
| Phone app: "Unexpected Error" enabling developer mode | Headset awake & near phone, phone Bluetooth on; restart headset + force-close app; try home Wi-Fi instead of hotspot; complete account verification on developers.meta.com; same account everywhere |
| No "Allow USB debugging" prompt | charge-only cable — try another; replug while wearing the headset |
| Headset not in MQDH/Unity | cable/driver; on Windows install Oculus ADB drivers |

## Working with a beginner
- One screen at a time; ask for a photo of each screen; tell exactly which button.
- If they want hands-off: write a prompt for a computer-use agent (see `cowork-handoff`). Agents must stop at logins/2FA.
