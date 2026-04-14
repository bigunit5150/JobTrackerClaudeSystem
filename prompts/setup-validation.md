---
prompt: Setup Validation
phase: Setup
version: 1.0
last_updated: 2026-04-13
depends_on: Onboarding complete, Notion template duplicated, Chrome extension configured
trigger: Run after completing the onboarding prompt to verify everything is working
---

# Setup Validation Prompt

**Where to use:** Your CareerPilot Claude Project (the same project where you ran onboarding).
**When to use:** After completing the onboarding prompt to confirm your entire setup is working end-to-end.

---

## The Prompt

```
SETUP VALIDATION — CareerPilot

I just finished onboarding. Run a full validation of my CareerPilot setup
to make sure everything is connected and working before I start using the
system. Check each item below and report the result.

---

CHECK 1 — NOTION CONNECTION
Try to read from my Job Tracker database.
- Can you access it? (yes/no)
- How many rows are currently in it?
- What Status values are configured?

---

CHECK 2 — RESUME REPOSITORY
Read from my Resume Repository database.
- Can you access it? (yes/no)
- How many resume variants are loaded? List them by name.
- Is there a "Resume Selection Rules" row? (yes/no)
- Are all resumes marked Active = "Yes"?

---

CHECK 3 — INTERVIEW PREP HUB
Read from my Interview Prep Hub database.
- Can you access it? (yes/no)
- Is it empty? (expected for a fresh setup)

---

CHECK 4 — RESUME SELECTION RULES
Read the Resume Selection Rules document from the Resume Repository.
- Does it exist? (yes/no)
- Does it contain a Candidate Profile Summary?
- Does it contain Target Role Criteria (minimum salary, target levels)?
- Does it contain Resume Selection Logic (which variant to use when)?
- Does it contain a Fit Assessment Framework (scoring criteria)?

---

CHECK 5 — SYSTEM PROMPT
Confirm the system prompt (CareerPilot system context) is loaded in the
project instructions. You should know about the three-phase system, the
Notion database schemas, and the trigger commands. If you don't have
this context, tell the user to upload system-prompt.md to the project
instructions.

---

CHECK 6 — END-TO-END TEST (optional)
If my Job Tracker has at least one row with Status = "Bookmarked" and a
populated Raw JD field, run a quick test:
- Read the JD
- Run a fit assessment against my Resume Selection Rules
- Tell me the fit score (1-10) and which resume you would select
- Do NOT write anything back to Notion — this is a dry run

If there are no Bookmarked jobs, skip this check and tell me to save a
job with the Chrome extension first.

---

AFTER ALL CHECKS:

Show me a validation summary in this format:

  CAREERPILOT SETUP VALIDATION
  ─────────────────────────────
  Notion Connection:     ✓ / ✗
  Resume Repository:     ✓ / ✗  ([count] resumes loaded)
  Interview Prep Hub:    ✓ / ✗
  Selection Rules:       ✓ / ✗
  Workflow Prompts:      ✓ / ✗  ([count]/3 found)
  End-to-End Test:       ✓ / ✗ / skipped

If everything passes, tell me: "Your CareerPilot setup is verified and
ready. Save a job with the Chrome extension, then come back here and say:
Review bookmarked jobs."

If anything fails, tell me exactly what's wrong and how to fix it.
```
