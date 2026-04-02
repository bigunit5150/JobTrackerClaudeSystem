# Phase 2: AI Job Review Workflow

## Overview

Phase 2 is where Claude earns its keep. Given a set of Bookmarked jobs in
your Notion Job Tracker, Claude evaluates each one, selects and optimizes
the right resume, and writes everything back to Notion — all without you
doing anything beyond triggering the workflow.

---

## Trigger Options

### Option A — Claude Project (Interactive)

Say "Review bookmarked jobs" in your Claude Job Search Project on claude.ai.
Claude reads all Bookmarked rows and processes them one by one. Best for
validating the workflow and reviewing Claude's output before automating.

### Option B — Claude Code (Automated)

Run the `job-review-workflow` skill in Claude Code. Claude Code connects to
Notion via the MCP server configured in `.mcp.json` and processes all
Bookmarked jobs autonomously. No browser session required.

```bash
# From the project root (NOTION_TOKEN must be set in your environment)
claude "Run the job-review-workflow skill"
```

### Option C — OpenClaw (Always-On)

Set up OpenClaw with this project as the workspace and configure a cron job
or heartbeat to process Bookmarked jobs automatically. OpenClaw loads the
`job-review-workflow` skill from the `skills/` directory and runs it on
schedule — no manual trigger required.

```bash
# OpenClaw processes jobs on its configured schedule, or trigger manually:
openclaw "Run the job-review-workflow skill"
```

See `docs/openclaw-setup.md` for full configuration.

### Option D — Scheduled Scan

Run `scripts/scan-bookmarked-jobs.py` on a schedule (cron, GitHub Actions,
or similar). The script queries Notion for Bookmarked rows and fires each
through the Claude API. See `scripts/README.md` for setup.

### Option E — Notion Automation + Webhook (Most Seamless)

Use Notion's built-in Automations (paid plans) to trigger a webhook when a
row's Status changes to "Bookmarked". The webhook hits a Make or n8n flow
that calls the Claude API. Effectively real-time — Claude processes the job
within seconds of you saving it.

**Recommended path:** Start with Option A to validate, then graduate to B, C, D, or E.

---

## What Claude Does For Each Job

### Step 1 — Read the Job

Claude reads Role Title, Company, and Raw JD. If Raw JD is empty, it writes
a note to AI Notes and skips: "Raw JD not populated — add JD text to process."

### Step 2 — Fit Assessment

Using your Resume Selection Rules from the Resume Repository, Claude evaluates:

- Does compensation appear to meet your minimum? (flagged if unknown)
- Does the role level match your targets?
- Does the location/arrangement work?
- Maps the top 5 JD requirements to your experience: Strong / Partial / Gap
- Assigns overall fit: 🟢 Green / 🟡 Yellow / 🔴 Red

**If 🔴 Red:**

- Writes assessment to AI Notes explaining why
- Sets Status → "AI Reviewed - Skip"
- Moves to next job — no resume generated

### Step 3 — Resume Selection

For Green and Yellow roles, Claude selects the appropriate resume variant based
on your selection rules. The choice is documented in AI Notes.

### Step 4 — Resume Optimization

Claude rewrites the selected resume to mirror the JD's language and priorities.

**In scope:**

- Reorder or re-emphasize existing bullet points
- Rewrite bullets to mirror JD keywords (same facts, better framing)
- Adjust the summary / objective section
- Add or remove skills from the skills section
- Suggest cuts if length exceeds your limit

**Never:**

- Fabricate experience or invent accomplishments
- Change employer names or job titles at previous companies
- Invent metrics or numbers not in the original resume

### Step 5 — Write Back to Notion

Claude updates the job row with:

- **AI Notes**: fit tier, resume selection rationale, top 3 strengths,
  top 1-2 gaps, recommendation (apply / apply with note / stretch)
- **Resume**: full optimized resume text
- **Status**: "AI Reviewed"

---

## Output Format of AI Notes

Claude writes AI Notes in a consistent format:

```text
FIT: 🟢 Green

RESUME SELECTED: Director of Engineering - Base
REASON: Role requires 5+ years managing managers, multi-team scope (50+ eng),
reports to CTO — matches Director variant criteria.

TOP STRENGTHS:
1. Direct LinkedIn experience with $15B GTM ecosystem matches their enterprise focus
2. 30+ engineer org with manager-of-managers exactly meets stated scope
3. DealHub compensation platform maps to their "incentive infrastructure" language

GAPS:
1. No fintech-specific domain experience — addressable in cover letter

RECOMMENDATION: Apply — strong fit, resume optimized for key signals.
```

---

## Prompt Location

The manual trigger prompt lives at:
`review-bookmarked-jobs.md`

The automated skill lives at:
`skills/job-review-workflow/SKILL.md`
