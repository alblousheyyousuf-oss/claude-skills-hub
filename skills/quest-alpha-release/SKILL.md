---
name: quest-alpha-release
description: Ship a Unity Quest APK to the user's headset through a Meta Horizon release channel (ALPHA) so it updates automatically, without cables. Use when deploying builds remotely, setting up a test channel for a VR app, or debugging upload errors in Meta Quest Developer Hub. نشر التحديثات للنظارة عبر قناة ALPHA.
---
# Quest ALPHA channel release

- Needs: a developer org + an App on the developer dashboard (Meta Horizon Store platform), Developer Distribution Agreement (DDA) **signed by the user himself**, a release keystore (back it up + its password in two places — losing it means the app can never be updated).
- Upload: Meta Quest Developer Hub → App Distribution → app → Upload → APK → channel **ALPHA** → short release notes → wait for "Upload complete". Stop and ask the user at any login prompt.
- Channel: invite link with auto-approve; headsets in the channel update automatically (or Library → Updates). Link expires 90 days after the last upload.
- Errors: `OCULUS_PLATFORM_DDA_IS_NOT_ACCEPTED` → the user signs the DDA, re-upload. 32-bit perflogger libs warning (armeabi-v7a, Meta's own) is harmless.
- Never change the package name (`com.company.app`) after the first upload, or updates break; the display name can change.
- For an always-on remote PC: no sleep/lock, auto-login, Claude app at startup, BIOS "Restore on AC power loss".
