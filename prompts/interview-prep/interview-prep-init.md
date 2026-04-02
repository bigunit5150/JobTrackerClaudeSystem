---
prompt: Interview Prep Initialization
phase: 3 — Interview Prep
version: 1.0
last_updated: 2026-03-29
depends_on: Job Tracker row with AI-reviewed resume, Notion connector, web search
trigger: Run once per opportunity, in a NEW Claude Project for that company/role
---

# Interview Prep Initialization Prompt

**Where to use:** A brand new Claude Project named "[Company] — [Role Title]".
**When to use:** Once you've decided to actively pursue a role (Status: Applying or Applied).
**What to provide:** The Notion URL of the Job Tracker row for this role.

---

## The Prompt

```
I have an interview coming up. Let's set up my prep workspace for this
opportunity.

Job Tracker row URL: [PASTE THE NOTION URL HERE]

---

STEP 1 — LOAD CONTEXT
Read the following from my Notion workspace:
- The Job Tracker row at the URL I provided above
  (get Role Title, Company, Raw JD, Resume, AI Notes)
- My Resume Selection Rules from the Resume Repository
  (row named "Resume Selection Rules v1.0")

Confirm what you've loaded before continuing.

---

STEP 2 — CREATE INTERVIEW PREP HUB ROW
Create a new row in my Notion Interview Prep Hub database with:
- Opportunity: [Role Title] @ [Company]
- Company: [from job row]
- Role Title: [from job row]
- Status: Active Prep
- Job Tracker URL: [URL I provided]
- Resume Used: [name of the resume variant from AI Notes]

After creating the row, tell me the Interview Prep Hub row URL so I can
paste my Claude Project URL into it.

---

STEP 3 — COMPANY RESEARCH
Search the web and research this company. Summarize:
- What they do and their core business model
- Company size, funding stage, and recent growth signals
- News from the last 90 days (launches, hires, funding, press)
- Engineering culture signals (tech blog, open source, stack if known,
  engineering team size if findable)
- What business problems this specific role is likely meant to solve
- How my background maps to their current needs

Save the full research summary to the "Company Research" field of the
Interview Prep Hub row.

---

STEP 4 — CHEAT SHEET
Generate a one-page interview cheat sheet covering:

1. Top 5 STAR stories mapped to the JD's key requirements
   - Each story: 2-3 sentences (Situation → Action → Result)
   - Label each: "Best for questions about [topic]"

2. Top 3 things to emphasize for this specific role
   - What from my background most directly addresses their needs

3. 1-2 gaps to acknowledge confidently
   - What I don't have and how to frame it honestly and positively

4. 5 smart questions to ask the interviewer
   - Specific to this company and role — not generic

5. Compensation notes
   - Their likely range based on role/stage/location
   - My minimum and target
   - One-line negotiation anchor

Save the cheat sheet to the "Cheat Sheet" field of the Interview Prep Hub row.

---

STEP 5 — CONFIRM AND BRIEF ME
Tell me:
- Interview Prep Hub row created (with URL)
- Company research saved
- Cheat sheet saved
- Top 3 things I should know walking into this interview

Then ask: "Would you like to run a mock interview now, or save that for
a separate session?"
```

---

## Running Mock Interviews (Follow-Up)

After initialization, start a new chat in the same project and use
the prompt from `prompts/interview-prep/mock-interview.md`.
