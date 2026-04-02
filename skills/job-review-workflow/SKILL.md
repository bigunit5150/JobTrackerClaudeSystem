# SKILL: job-review-workflow

## Purpose
Orchestrates the end-to-end automated job review pipeline. Reads all
Bookmarked jobs from Notion, runs fit assessment and resume optimization
for each, and writes results back — with no human in the loop.

This skill chains the logical steps of job evaluation and resume tailoring
with Notion read/write operations. It is the Phase 2B automation layer
on top of the manual `review-bookmarked-jobs.md` prompt.

---

## When to Use This Skill
- Scheduled automated processing (cron, GitHub Actions)
- Bulk processing of a large backlog of Bookmarked jobs
- Any context where fully autonomous operation is desired

For interactive use with human review between jobs, use the conversational
prompt in `review-bookmarked-jobs.md` instead.

---

## Inputs Required
- Active Notion MCP connection with read/write access to:
  - Job Tracker database (ID: stored in config or provided at runtime)
  - Resume Repository database (ID: stored in config or provided at runtime)
- Resume Selection Rules row present in Resume Repository
- At least one resume row with Active = "Yes" in Resume Repository

---

## Outputs
For each Bookmarked job processed:
- `AI Notes` field updated with fit assessment and rationale
- `Resume` field updated with full optimized resume text
- `Status` updated to "AI Reviewed" (fit) or "AI Reviewed - Skip" (no fit)

---

## Execution Steps

### Step 1: Load Configuration
Read Resume Selection Rules from Notion Resume Repository:
- Query for row where Resume Name = "Resume Selection Rules v1.0"
- Load full Resume Content as working configuration
- If not found: halt and return error "Resume Selection Rules not found.
  Run onboarding prompt first."

### Step 2: Load Active Resumes
Query Resume Repository for all rows where Active = "Yes" and
Category != "Other". Build a map of category → resume content.

### Step 3: Fetch Bookmarked Jobs
Query Job Tracker for all rows where Status = "Bookmarked".
If zero results: return "No Bookmarked jobs found. Nothing to process."

### Step 4: Process Each Job
For each Bookmarked job row, execute the following sub-pipeline:

#### 4a — Validate
Check that Raw JD is not empty. If empty:
  - Write to AI Notes: "Raw JD not populated — add JD text to process"
  - Set Status → "AI Reviewed - Skip"
  - Continue to next job

#### 4b — Fit Assessment
Using loaded Resume Selection Rules, evaluate:
1. Compensation signal vs minimum threshold
2. Role level vs target levels
3. Location / arrangement vs preferences
4. Extract top 5 JD requirements
5. Map each to candidate experience: Strong / Partial / Gap
6. Count gaps. Assign fit tier: Green / Yellow / Red per rules thresholds.

#### 4c — Branch on Fit
If Red:
  - Compose AI Notes (see format below)
  - Set Status → "AI Reviewed - Skip"
  - Continue to next job
If Green or Yellow:
  - Continue to 4d

#### 4d — Resume Selection
Based on JD signals (years management required, team size, reporting level,
emphasis), select the appropriate resume variant using the Selection Logic
from Resume Selection Rules. Record rationale.

#### 4e — Resume Optimization
Optimize selected resume for this specific JD:
- Rewrite summary to address top 2-3 signals
- Reorder bullets to prioritize top 5 signal matches
- Mirror JD keywords naturally (do not keyword stuff)
- Adjust skills section for relevance
- Apply length constraints from Formatting Standards
- Never: fabricate, invent metrics, change employer history

#### 4f — Write Back to Notion
Update the job row:
  - `AI Notes`: formatted assessment (see AI Notes Format below)
  - `Resume`: full optimized resume text
  - `Status`: "AI Reviewed"

### Step 5: Return Summary
After all jobs processed, return:
- Total processed
- Green / Yellow / Red counts
- List of Green/Yellow jobs with one-line recommendation each
- List of skipped jobs (missing JD or Red) with reason

---

## AI Notes Format

```
FIT: [Green / Yellow / Red]

RESUME SELECTED: [Resume Name]
REASON: [1-2 sentences on why this variant was chosen]

TOP STRENGTHS:
1. [Specific strength mapped to JD requirement]
2. [Specific strength]
3. [Specific strength]

GAPS:
1. [Gap and brief framing note]

RECOMMENDATION: [Apply / Apply with note / Stretch / Skip]
[One sentence rationale]
```

---

## Error Handling

| Condition | Behavior |
|---|---|
| Notion connection unavailable | Halt, return error with reconnect instructions |
| Resume Selection Rules not found | Halt, return error with setup instructions |
| No active resumes found | Halt, return error listing missing categories |
| Raw JD empty | Skip job, write note to AI Notes, continue |
| Notion write fails on a row | Log error, continue processing remaining jobs, report failures in summary |

---

## Dependencies
- Notion MCP connector (read + write)
- Resume Selection Rules in Resume Repository
- Active resume variants in Resume Repository

## Related Files
- `review-bookmarked-jobs.md` — manual/interactive version
- `skills/interview-prep-builder/SKILL.md` — downstream Phase 3 skill
- `docs/phase-2-job-review.md` — full workflow documentation
