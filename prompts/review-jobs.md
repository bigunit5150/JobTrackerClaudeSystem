---
prompt: Review Bookmarked Jobs
phase: 2 — Job Review
version: 2.0
last_updated: 2026-04-13
depends_on: Resume Selection Rules in Notion, Notion connector active
trigger: Say "Review bookmarked jobs" in your CareerPilot Claude Project
---

# Review Bookmarked Jobs

**Where to use:** Your CareerPilot Claude Project.
**When to use:** Any time you have new jobs with Status = "Bookmarked" in
your Job Tracker.

---

## The Prompt

```
Review all jobs in my Notion Job Tracker where Status = "Bookmarked".

---

PRE-FLIGHT CHECK

Before reviewing any jobs, confirm:
1. Read my Resume Selection Rules from the Resume Repository
   (row named "Resume Selection Rules v1.0"). If it does not exist,
   stop and tell me to complete onboarding first.
2. Confirm at least one resume variant with Active = "Yes" exists
   in the Resume Repository. If none exist, stop and tell me to
   add resumes first.
3. Query the Job Tracker for all rows where Status = "Bookmarked".
   If zero results, tell me "No bookmarked jobs found" and stop.

Once all three checks pass, begin processing.

---

BATCH PROCESSING — FOR EACH BOOKMARKED JOB:

Process every Bookmarked job in a single session. Do not stop after one.

STEP 1 — READ THE JOB
- Read the Role Title, Company, and Raw JD fields
- If Raw JD is empty:
  Write to AI Notes: "Raw JD not populated — add JD text to process"
  Set Status → "AI Reviewed - Skip"
  Move to next job

---

STEP 2 — FIT ASSESSMENT
Using my Resume Selection Rules, evaluate and score fit on a 1-10 scale:
- Does compensation appear to meet my minimum? (flag if not mentioned)
- Does the role level match my targets?
- Does the location / arrangement work?
- Map the top 5 JD requirements to my experience:
  Strong match / Partial match / Gap
- Assign a fit score (1-10) with a brief rationale

If score is below 6:
- Write full assessment to AI Notes including the score and rationale
- Set Status → "AI Reviewed - Skip"
- Move to next job — do not generate a resume

---

STEP 3 — RESUME SELECTION (score 6+ only)
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
- AI Notes: fit score (1-10), resume selection rationale, top 3 strengths,
  top 1-2 gaps, recommendation (apply / apply with note / stretch)
- Resume: full optimized resume text
- Status: "AI Reviewed"

---

AFTER ALL JOBS ARE PROCESSED:

Give me a session summary table:

| Role Title | Company | Fit Score | Action |
|---|---|---|---|
| [title] | [company] | [1-10] | Reviewed / Skipped (reason) |

Then summarize:
- Total reviewed
- Reviewed (score 6+) vs Skipped (below 6) breakdown
- Recommended to apply (list with one-line reason each)
- Any jobs skipped due to missing JD text
```
