# Phase 3: Interview Prep Workflow

## Overview

For every role you actively pursue, start a new chat in your Job Search
Claude Project. This chat becomes the living workspace for that opportunity —
accumulating context across the entire interview lifecycle: initialization,
mock interviews, interviewer-specific prep, real interview debriefs, and
cheat sheet updates.

---

## Why One Chat Per Opportunity?

Keeping the entire interview process in a single chat means Claude retains
full context: company research, your cheat sheet, mock interview feedback,
and debrief insights. Each interaction builds on the last — no re-explaining,
no lost context. When you debrief after a real interview, Claude updates your
master cheat sheet with what you learned and preps you for the next round.

---

## Initialization (Run Once Per Opportunity)

When a role moves to "Applying" or "Applied" in your Job Tracker:

### Option A — Claude Project (Interactive)

1. Open your Job Search Claude Project on [claude.ai](https://claude.ai)
2. Start a **new chat** for this opportunity
3. Paste the Job Tracker row URL and run the initialization prompt from
   `prompts/interview-prep-init.md`

Everything else for this opportunity (mock interviews, interviewer prep,
debriefs) happens in this same chat.

### Option B — Claude Code (Automated)

```bash
claude "Run the interview-prep-builder skill for [NOTION ROW URL]"
```

This creates the Interview Prep Hub row, runs company research, and generates
the full cheat sheet autonomously. Continue in a Claude Project chat for
interactive mock interviews and debriefs.

### Option C — OpenClaw (Automated)

```bash
openclaw "Run the interview-prep-builder skill for [NOTION ROW URL]"
```

Same as Option B but runs through OpenClaw. Can also be triggered via chat
(WhatsApp, Slack, etc.) if you have channels configured.

Claude will:

- Read the JD and your optimized resume from Notion
- Create a row in your Interview Prep Hub
- Run company research (web search)
- Generate a comprehensive master cheat sheet
- Save everything back to Notion

---

## Master Cheat Sheet Contents

Claude generates a comprehensive cheat sheet with 8 sections:

1. **Self-Introduction** — a polished 60-90 second intro tailored to this role
2. **Why This Company** — 3-4 specific, researched reasons for interest
3. **Key Accomplishments & Metrics** — 8-10 strongest achievements with
   quantified metrics, organized by theme, mapped to JD requirements
4. **Top 5 STAR Stories** — mapped to the JD's key requirements, with
   trigger phrases for when to use each
5. **3 Things to Emphasize** — specific to this company and role
6. **1-2 Gaps to Acknowledge** — honest framing, no spin
7. **5 Questions to Ask** — company-specific, not generic
8. **Compensation Notes** — market range, your targets, negotiation anchor

The master cheat sheet is a living document. It gets updated after each
mock interview and real interview debrief as you learn what works.

---

## Interviewer-Specific Cheat Sheets

Before a specific interview round, say in the same chat:

```text
Prep for [INTERVIEWER NAME], [TITLE] — [ROUND TYPE]
[Optional: LinkedIn URL, anything you know about them]
```

Claude will research the interviewer and generate a targeted cheat sheet:

- What this person likely cares about based on their function
- Which STAR stories and accomplishments to prioritize
- Tailored questions to ask this specific person
- Rapport-building angles (shared background, interests)

---

## Mock Interviews

Say in the same chat:

```text
Mock [Phone Screen / Hiring Manager / Panel / Final Round] interview.
Interviewer: [NAME and TITLE if known]
```

Claude will:

- Play the interviewer with realistic questions for the round type
- Stay in character through 4-6 questions
- Give structured feedback after the mock
- Update the master cheat sheet with improved framings
- Save notes to Interview Prep Hub

---

## Post-Interview Debrief

After each real round, come back to the same chat:

```text
Debrief [ROUND TYPE] with [INTERVIEWER NAME/TITLE].
Here's how it went: [describe the interview]
```

Claude will:

- Analyze signals from the interviewer's questions
- Assess how your answers landed
- Update the master cheat sheet with lessons learned
- Prep you for the likely next round
- Save debrief notes to Interview Prep Hub

---

## Prompt Locations

| Use Case | File |
| --- | --- |
| Full lifecycle prompt | `prompts/interview-prep-init.md` |
| Quick command reference | `prompts/mock-interview.md` |
| Automated version | `skills/interview-prep-builder/SKILL.md` |
