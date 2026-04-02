# SKILL: interview-prep-builder

## Purpose

Autonomously initializes an interview prep workspace for a specific
opportunity. Given a Job Tracker row URL, this skill researches the company,
generates a comprehensive cheat sheet (with self-introduction, key
accomplishments, and company-specific motivation), and writes everything
to the Interview Prep Hub — with no human interaction required beyond
providing the input URL.

This is the automated version of `prompts/interview-prep-init.md`.

---

## When to Use This Skill

- When a job moves to "Applying" or "Applied" status and you want prep
  materials generated immediately without a manual chat session
- As a downstream trigger after `job-review-workflow` marks a job Green/Yellow
  and you immediately want to begin prep

For the interactive version (with mock interviews, interviewer-specific
prep, and debriefs), use `prompts/interview-prep-init.md` in a Claude
Project chat instead.

---

## Inputs Required

- Job Tracker row URL (the specific opportunity to prep for)
- Active Notion MCP connection with read access to Job Tracker and
  Resume Repository, and write access to Interview Prep Hub
- Web search access (for company research)

---

## Outputs

A populated Interview Prep Hub row containing:

- Company Research (web-sourced, structured summary)
- Cheat Sheet (self-introduction, why this company, key accomplishments,
  STAR stories, talking points, gaps, questions, comp notes)
- Key Talking Points (top 3-5, role-specific)
- Questions To Ask (5 smart, company-specific questions)
- Status: Active Prep
- Links back to Job Tracker row

---

## Execution Steps

### Step 1: Load Job Context

Read the Job Tracker row at the provided URL. Extract:

- Role Title
- Company
- Raw JD
- Resume (the optimized resume Claude wrote in Phase 2)
- AI Notes (fit assessment and selection rationale from Phase 2)

If Raw JD or Resume is empty, halt and return:
"Cannot initialize prep — Raw JD or optimized Resume missing from Job Tracker
row. Complete Phase 2 review first."

### Step 2: Load Resume Selection Rules

Read Resume Selection Rules from Notion Resume Repository for candidate
background context used in story mapping and accomplishment extraction.

### Step 3: Create Interview Prep Hub Row

Create a new row in Interview Prep Hub:

- Opportunity: [Role Title] @ [Company]
- Company: [from job row]
- Role Title: [from job row]
- Status: Active Prep
- Job Tracker URL: [input URL]
- Resume Used: [resume variant name from AI Notes, if parseable]

Record the new row URL for subsequent writes.

### Step 4: Company Research

Using web search, research the company and compile:

**Business Overview**

- Core product / service and business model
- Target customers and market position
- Company size (employees) and funding stage
- Revenue / growth signals if public

**Recent Developments (last 90 days)**

- Product launches or major announcements
- Leadership changes
- Funding rounds
- Press coverage and industry positioning

**Engineering Culture**

- Tech blog or developer content (if exists)
- Open source contributions
- Known tech stack (if public)
- Engineering team size (if findable)
- Glassdoor signals (engineering culture, interview process)

**Role Context**

- What business problem this role likely solves
- Why they're hiring for this level now
- How the candidate's background maps to their needs

Format as structured Markdown. Save to "Company Research" field of the
Interview Prep Hub row.

### Step 5: Generate Master Cheat Sheet

Using the JD, optimized resume, candidate background from Selection Rules,
and company research just compiled, generate a comprehensive cheat sheet
with the following sections:

**Section 1: Self-Introduction**
A polished 60-90 second self-introduction tailored to this role. Cover:
who the candidate is, career arc, current situation, and why this role
is the logical next step. Conversational tone, not a resume recitation.

**Section 2: Why This Company**
3-4 specific, researched reasons the candidate would be interested in this
company and role. Reference concrete details from company research —
products, mission, recent news, culture, technical challenges. No generic
statements.

**Section 3: Key Accomplishments & Metrics**
Extract the 8-10 strongest accomplishments from the resume, each with
quantified metrics where available. Organize by theme (leadership,
technical, business impact, transformation). For each:

- One-line summary with the metric
- Which JD requirements it maps to
- When to deploy it (which question types)

**Section 4: Top 5 STAR Stories**
Map to the JD's top 5 requirements. For each:

- Label: "Best for questions about [topic]"
- Situation: 1 sentence context
- Action: 1-2 sentences what you did
- Result: 1 sentence quantified outcome
- Trigger phrases: 2-3 question types that should prompt this story

**Section 5: 3 Things to Emphasize**
Specific to this company's context and the role's signals. Not generic —
these should reference actual details from the JD and company research.

**Section 6: 1-2 Gaps to Acknowledge**
Be direct. Name the gap and provide a confident, honest framing.
Do not spin — interviewers see through it.

**Section 7: 5 Questions to Ask**
Specific to this company and role. Avoid generic questions like
"What does success look like?" — ask about things only knowable from
the company research or specific JD details.

**Section 8: Compensation Notes**

- Market range estimate for this role level / location / stage
- Candidate minimum and target
- One-line anchor: what to say when asked for a number first

Save the full cheat sheet to "Cheat Sheet" field. Also save sections 5
and 7 to "Key Talking Points" and "Questions To Ask" fields respectively.

### Step 6: Return Summary

Return:

- Interview Prep Hub row URL
- Company research: saved
- Master cheat sheet: saved (with all 8 sections)
- Top 3 things to know walking into this interview (pulled from cheat sheet)

---

## Error Handling

| Condition | Behavior |
| --- | --- |
| Job Tracker row not readable | Halt, return error with URL and access note |
| Raw JD or Resume missing | Halt, return error directing to Phase 2 |
| Web search unavailable | Skip company research section, note in output, continue with cheat sheet using JD only |
| Notion write fails | Retry once, then return error with the content so user can paste manually |

---

## Dependencies

- Notion MCP connector (read Job Tracker + Resume Repository, write Interview Prep Hub)
- Web search tool
- `job-review-workflow` skill (upstream — provides the optimized resume this skill reads)

## Related Files

- `prompts/interview-prep-init.md` — interactive version (full lifecycle)
- `prompts/mock-interview.md` — quick reference for mock interview commands
- `docs/phase-3-interview-prep.md` — full workflow documentation
