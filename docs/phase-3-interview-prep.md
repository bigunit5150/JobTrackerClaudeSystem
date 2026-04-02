# Phase 3: Interview Prep Workflow

## Overview

For every role you actively pursue, create a dedicated Claude Project. This
project becomes the living workspace for that opportunity — it accumulates
context across every conversation, from initial prep through final round to
post-interview debrief.

---

## Why a Dedicated Project Per Opportunity?

Claude Projects persist context. If you prep for a phone screen, then come
back two days later for the hiring manager round, Claude remembers the company
research, your talking points, and what you covered in the mock interview —
without you re-explaining anything. The project builds on itself over time.

---

## Project Initialization (Run Once Per Opportunity)

When a role moves to "Applying" or "Applied" in your Job Tracker:

1. Go to [claude.ai](https://claude.ai) → Projects → New Project
2. Name it: `[Company] — [Role Title]` (e.g. "Stripe — Director of Engineering")
3. Paste the Job Tracker row URL and run the initialization prompt from
   `prompts/interview-prep/interview-prep-init.md`

Claude will:
- Read the JD and your optimized resume from Notion
- Create a row in your Interview Prep Hub
- Run company research (web search)
- Generate a cheat sheet with your top stories mapped to the JD
- Save everything back to Notion

Paste the Claude Project URL into the Interview Prep Hub row so you can
navigate back to it from Notion.

---

## Cheat Sheet Contents

Claude generates a one-page cheat sheet covering:

- **Top 5 STAR stories** mapped to the JD's key requirements
  (2-3 sentences each, ready to expand in conversation)
- **3 things to emphasize** specific to this company and role
- **1-2 gaps to acknowledge** and how to frame them confidently
- **5 smart questions to ask** the interviewer (role-specific)
- **Compensation notes** — their likely range vs your minimum, negotiation angles

---

## Mock Interviews

After initialization, start a new chat in the same project and run:

```
Run a mock [Phone Screen / Hiring Manager / Panel / Final Round] interview
for [Company] [Role]. Play the interviewer, ask realistic questions for this
role level, and give me feedback after each answer.
```

Claude will:
- Open with realistic questions based on the round type and role level
- Stay in character as the interviewer until you finish
- Give structured feedback: what landed, what to tighten, what to add

Subsequent rounds build on earlier ones — Claude knows what you've already
practiced and can focus on weaker areas.

---

## Post-Interview Debrief

After each round, come back to the project and run:

```
I just finished my [round] interview with [Company]. Let me debrief.
[Describe how it went, questions asked, your answers, any surprises]
```

Claude will:
- Help you analyze how it went
- Identify signals from the interviewer's questions
- Update your prep for the next round
- Save notes to Interview Prep Hub

---

## Prompt Locations

| Use Case | File |
|---|---|
| Initialization | `prompts/interview-prep/interview-prep-init.md` |
| Mock interview | `prompts/interview-prep/mock-interview.md` |
| Automated version | `skills/interview-prep-builder/SKILL.md` |
