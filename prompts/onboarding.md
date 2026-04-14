---
prompt: CareerPilot Onboarding
phase: Setup
version: 2.0
last_updated: 2026-04-13
depends_on: Notion template duplicated, Notion connector active
trigger: Run once in your CareerPilot Claude Project on first use
---

# CareerPilot Onboarding

**Where to use:** Your CareerPilot Claude Project (with the system prompt
already set in the project instructions).
**When to use:** Once, during first-time setup.

---

## The Prompt

```
CAREERPILOT ONBOARDING

Let's set up CareerPilot together. Walk me through each step in order.
Tell me clearly what you're doing and what I need to do. Wait for my
confirmation before moving to the next step.

---

STEP 1 — PREREQUISITES CHECK

Before we begin, confirm each of these. If any are missing, pause and
walk me through fixing it before continuing.

1. Notion template: Have I duplicated the CareerPilot Notion template?
   (https://www.notion.so/342037c8790b819195a6f4aea08e8bb4)
   Try to read from my Job Tracker database to confirm.

2. Notion connection: Can you access my Notion workspace right now?
   If not, tell me to go to claude.ai Settings > Integrations > Notion
   and connect it.

3. Chrome extension: Have I installed the Job Post Tracker extension?
   (I'll confirm — you can't check this directly.)

If all three are confirmed, proceed. If not, help me fix what's missing.

---

STEP 2 — DATABASE ID COLLECTION

I need to configure the Chrome extension with my Job Tracker database ID.
Walk me through finding it:

1. Tell me to open the Job Tracker database in Notion (inside the
   CareerPilot dashboard, click into the Job Tracker table so it opens
   as a full-page database)
2. Tell me to copy the URL from the browser address bar
3. Explain that the database ID is the 32-character string in the URL
   before the ?v= parameter
4. Tell me to paste it into the Chrome extension Settings page along
   with my Notion Integration Token

Ask me to confirm the extension is configured and the "Test Notion
Connection" button works before continuing.

---

STEP 3 — RESUME INTAKE

Ask me to paste my current resume(s). For each resume I provide:

1. Read the full content
2. Assign a descriptive name based on the content
   (e.g. "Director of Engineering - Base", "Senior EM - Technical")
3. Identify the category: Director, Senior Manager, VP,
   AI/Technical Consulting, or Other
4. Show me a summary: name → category → key differentiator
5. Ask me to confirm or correct

Once all resumes are confirmed, create a row in my Notion Resume
Repository for each one:
  - Resume Name: the descriptive name
  - Category: your best match
  - Version: "v1.0"
  - Resume Content: full text of the resume
  - Active: "Yes"
  - Last Updated: today's date

Confirm how many rows were created before moving on.

---

STEP 4 — BUILD RESUME SELECTION RULES

This is the most important step. Extract everything you can from my
resumes automatically, then ask me questions ONE SECTION AT A TIME.
Do not move to the next section until I've answered the current one.

AUTO-EXTRACT FROM RESUMES (show me a summary to confirm):
- Full name and contact information
- Most recent job title and company
- Total years of experience (engineering and management separately)
- Largest team managed and at what reporting level
- All employers in order with approximate dates
- Key accomplishments that include metrics
- Technical skills (languages, cloud platforms, frameworks, tools)
- What differentiates each resume variant from the others

After showing the summary, ask me to confirm it's accurate. Correct
anything I flag before continuing.

---

SECTION A — TARGETS & COMPENSATION
Ask me:
1. What is your minimum acceptable base salary?
2. What role levels are you actively targeting?
3. Any role types to explicitly avoid?
4. Preferred company stage and size?
5. Any specific companies to target or avoid?

---

SECTION B — LOCATION & WORK ARRANGEMENT
Ask me:
6. What locations and work arrangements are you open to?
7. Any you'd consider but want flagged as non-ideal?

---

SECTION C — DOMAIN & INDUSTRY PREFERENCES
Based on my resume, suggest 5-8 industries or domains that match
my background. Ask me to react: which interest me most, which to
avoid, and whether there are any I want to add.

---

SECTION D — RESUME SELECTION LOGIC
For each resume variant I provided, propose a use-when rule based
on the content. Cover:
  - Minimum years of management experience the JD signals
  - Team size and org scope
  - Reporting level
  - Primary emphasis (strategic, technical, people leadership)
Ask me to confirm, adjust, or add rules for each variant.
Then ask: if two resumes both qualify for a role, how do we break
the tie?

---

SECTION E — OPTIMIZATION SCOPE
Confirm which of these are in scope when tailoring a resume:
  - Reorder or re-emphasize existing bullet points
  - Rewrite bullets to mirror JD language (same facts, better framing)
  - Adjust the summary or objective section
  - Add or remove skills from the skills section
  - Suggest sections to cut when length is tight

Then ask: What is strictly off limits?
(e.g. never fabricate experience, never change job titles at previous
employers, never invent metrics)

---

SECTION F — SIDE PROJECTS & ADDITIONAL WORK
Ask me:
Do you have any side projects, open source work, freelance, or
consulting engagements to optionally include on your resume?
For each, I need:
  - Name and one-sentence description
  - Tech stack (if technical)
  - Live URL or GitHub link
  - When to include: always, only for certain role types, never by default

---

SECTION G — FIT ASSESSMENT FRAMEWORK
Based on everything above, draft a scoring system:
  8-10: Strong match — proceed and optimize resume
  6-7: Partial match — proceed with caveats noted
  Below 6: Recommend skip — do not optimize unless overridden

Ask me to review and adjust the criteria for each tier.
Then ask: if a role scores below 6, should you still generate a
resume if I ask for one anyway, or always decline?

---

SECTION H — FORMATTING STANDARDS
Ask me:
- Maximum resume length?
- Preferred output format? (Markdown, Word doc, plain text)
- File naming convention?
- Any sections to always include or exclude?
- Any specific formatting rules?

---

AFTER ALL SECTIONS ARE COMPLETE:

1. Generate a complete Resume Selection Rules document with:
   - Candidate Profile
   - Target Criteria
   - Resume Selection Logic (with tiebreaker)
   - Optimization Rules
   - Side Projects Reference
   - Key Accomplishments Table (tagged by best-fit role type)
   - Fit Assessment Framework (scoring scale)
   - Formatting Standards
   - Role-Specific Framing Notes (one section per domain)

2. Save it to my Notion Resume Repository as a new row:
   - Resume Name: "Resume Selection Rules v1.0"
   - Category: "Other"
   - Active: "Yes"
   - Notes: "Master configuration — CareerPilot workflow"
   - Resume Content: full document text

---

STEP 5 — SETUP CONFIRMATION

Perform a final check by reading back the databases you can see via
the Notion connector:
  - Job Tracker: accessible? (yes/no)
  - Resume Repository: accessible? How many resumes loaded?
  - Interview Prep Hub: accessible? (yes/no)
  - Resume Selection Rules: found and readable? (yes/no)

Show me a summary:

  CAREERPILOT SETUP COMPLETE
  ──────────────────────────
  Databases:        ✓ All three accessible
  Resumes:          [count] loaded
  Selection Rules:  ✓ Saved to Notion
  Extension:        ✓ Configured (user confirmed)

---

STEP 6 — WHAT'S NEXT

Tell me:

"You're all set. Here's how to use CareerPilot:

1. Find a job on any job board and click the Chrome extension to save it
2. Come back here and say 'Review bookmarked jobs' — I'll assess fit
   and optimize your resume for each role
3. When you get an interview, start a new chat in this project and say
   'Start interview prep for [role]' — I'll research the company and
   build your cheat sheet

Your CareerPilot dashboard in Notion tracks everything."
```
