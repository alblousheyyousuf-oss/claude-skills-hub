---
name: cowork-handoff
description: Write a self-contained task prompt for a computer-use agent (Claude Cowork, Claude in Chrome, desktop agents) to do GUI work on the user's machine — installing software, clicking through Unity/Blender/Meta tools. Use when the user asks you to "control the device", can't follow GUI steps, or asks you to write the command for Cowork. اكتب أمراً يفهمه Cowork.
---
# Handoff prompt for a computer-use agent

You cannot click on the user's screen from a cloud session; say so once, then write a prompt they paste into the agent.

Template (English, since UIs are English):
```
Task: <one line outcome>
Context: <what is already open/installed, OS, user is a beginner>
Steps:
1. <exact menu path / button text>  …
N. Take a screenshot of <final state> and report.
Rules:
- STOP and ask the user at any password, login, payment or 2FA. Never enter credentials.
- Install nothing beyond the list; delete nothing.
- If a menu differs, screenshot + describe + ask before improvising.
- Report progress after each step in short plain <user language>.
```
Keep steps verifiable (button labels, expected screens). Ask the user to send back the agent's final report/screenshot.
