---
name: session-economy
description: Keep long creative/3D/coding sessions cheap and fast. Use at the start of any multi-hour task, before iterating on renders or videos, when a session is getting long, or when the user complains about cost, speed or tokens. اقتصاد الجلسة وتوفير التوكينز والسرعة.
---
# Session economy

Measured on a real 1,460-call session (3D/VR art): **95% of all cost was re-reading the context**, not output. Every tool call re-sends the whole conversation, so cost ≈ (number of calls) × (context size). A call at hour 6 costs ~10× a call at hour 1.

## Rules, by impact
1. **Fresh session per sub-project.** When a phase ends (a delivery, a direction change), write a handoff (`HANDOFF.md`: goal, decisions, file paths, open questions) and continue in a new session. Biggest single saving.
2. **Agree before building.** 18% of the measured session built a concept the user then rejected. Use `brief-lock` before any build that takes more than ~20 calls.
3. **Batch tool calls.** Put independent reads/searches in one message; chain shell steps in one command; write several small files in one heredoc. Aim for fewer, larger calls.
4. **Images are the heaviest results.** 114 images were read. Look at one contact sheet (4–12 frames, ≤1600 px wide) instead of separate frames; read a single full frame only to judge fine detail; never read a raw screenshot just to "check it worked" when a number (pixel mean, file size, error count) answers it.
5. **Quiet commands.** Pipe to `tail -n 20`, `grep -E 'error|warn'`, `--quiet`, `-q`. Never print whole files you just wrote.
6. **Edit, don't rewrite.** Patch files with exact-string replacements (one script, many edits) instead of re-writing 60 KB files.
7. **Long jobs in the background** (renders, encodes) with one completion notification; do other work meanwhile; never poll with sleep loops.
8. **Research budget.** Cap web searches per question (≈5–8), save findings to a file once, cite from it; don't re-search known facts.
9. **Videos for the user**: encode at CRF 26–28, ≤1080p; check size before sending (a 58 MB preview was sent once).
10. **Measure.** Run `scripts/session_cost.py` on the session log to see where tokens went.

## Quick checklist before each step
- Can this be one call instead of three?
- Do I need to *see* this, or just know a number?
- Is the direction confirmed?
