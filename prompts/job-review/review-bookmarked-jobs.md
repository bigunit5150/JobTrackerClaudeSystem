---
prompt: Review Bookmarked Jobs
phase: 2 — Job Review
version: 1.0
last_updated: 2026-03-29
depends_on: Resume Selection Rules saved in Notion, Notion connector active
trigger: Manual — say "Review bookmarked jobs" in your Job Search Claude Project
---

# Review Bookmarked Jobs Prompt

**Where to use:** Your main Job Search Claude Project (the one set up during onboarding).
**When to use:** Any time you have new jobs with Status = "Bookmarked" in your Job Tracker.

---

## The Prompt

```
Review all jobs in my Notion Job Tracker where Status = "Bookmarked".

First, read my Resume Selection Rules from the Notion Resume Repository
(the row named "Resume Selection Rules v1.0") so you have my preferences,
fit thresholds, and resume selection logic loaded before starting.

For each Bookmarked job, follow this process in order:

---

STEP 1 — READ THE JOB
- Read the Role Title, Company, and Raw JD fields
- If Raw JD is empty but Job URL exists, write to AI Notes:
  "Raw JD not populated — add JD text to process this role"
  Set Status → "AI Reviewed - Skip" and move to next job

---

STEP 2 — FIT ASSESSMENT
Using my Resume Selection Rules, evaluate:
- Does compensation appear to meet my minimum? (flag if salary not mentioned)
- Does the role level match my targets?
- Does the location / arrangement work?
- Map the top 5 JD requirements to my experience:
  Strong match / Partial match / Gap
- Assign overall fit: Green / Yellow / Red

If Red:
- Write full assessment to AI Notes
- Set Status → "AI Reviewed - Skip"
- Move to next job — do not generate a resume

---

STEP 3 — RESUME SELECTION (Green and Yellow only)
Select the appropriate resume variant based on my selection rules.
State which resume was chosen and why in 1-2 sentences.

---

STEP 4 — RESUME OPTIMIZATION
Optimize the selected resume for this specific role.

In scope:
- Reorder or re-emphasize existing bullet points
- Rewrite bullets to mirror JD language (same facts, better framing)
- Adjust the summary or objective section
- Add or remove skills from the skills section
- Suggest cuts if length exceeds my stated limit

Never:
- Fabricate experience or invent accomplishments
- Change employer names or job titles from previous roles
- Invent metrics or numbers not present in the original resume

Produce the full optimized resume text.

---

STEP 5 — WRITE BACK TO NOTION
Update the job row with:
- AI Notes: fit tier, resume selection rationale, top 3 strengths,
  top 1-2 gaps, recommendation (apply / apply with note / stretch)
- Resume: full optimized resume text
- Status: "AI Reviewed"

---

AFTER ALL JOBS ARE PROCESSED:

Give me a summary:
- Total reviewed
- Green / Yellow / Red breakdown
- Recommended to apply (list with one-line reason each)
- Any jobs skipped due to missing JD text
```
