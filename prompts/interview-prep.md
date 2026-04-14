---
prompt: Interview Prep & Coaching
phase: 3 — Interview Prep
version: 3.0
last_updated: 2026-04-13
depends_on: Job Tracker row with AI-reviewed resume, Notion connector, web search
trigger: Say "Start interview prep for [role]" in a new chat in your CareerPilot Claude Project
---

# Interview Prep & Coaching

**Where to use:** Your CareerPilot Claude Project — start a **new chat** for
each opportunity. The entire interview lifecycle for this role happens in
this one chat.
**When to use:** Once you've decided to actively pursue a role
(Status: Applying or Applied).
**What to provide:** The Notion URL of the Job Tracker row for this role.

---

## The Prompt

```
CAREERPILOT — INTERVIEW PREP

Start interview prep for this opportunity. Stay in this chat through the
entire interview process — initialization, mock interviews,
interviewer-specific prep, debriefs, and cheat sheet updates.

Job Tracker row URL: [PASTE THE NOTION URL HERE]

===================================================================
SECTION 1 — INITIALIZATION
===================================================================

STEP 1 — LOAD CONTEXT
Read the following from my Notion workspace:
- The Job Tracker row at the URL I provided
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

After creating the row, tell me the Interview Prep Hub row URL.

---

STEP 3 — COMPANY RESEARCH
Search the web and research this company. Only use real, verifiable
information — never invent company details.

Summarize:
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

STEP 4 — MASTER CHEAT SHEET
Generate a comprehensive interview cheat sheet with the following
8 sections. This is the master cheat sheet — it will be updated
throughout the interview process as we learn more.

SECTION 1: SELF-INTRODUCTION
Write a polished 60-90 second self-introduction tailored to this role.
Cover: who I am, my career arc, what I'm doing now, and why this role
is the logical next step. Keep it conversational, not a resume recitation.

SECTION 2: WHY THIS COMPANY
Write 3-4 specific, researched reasons I would be genuinely interested
in this company and role. Reference concrete details from the company
research — products, mission, recent news, culture, technical challenges.
Avoid generic statements like "I admire your innovation."

SECTION 3: KEY ACCOMPLISHMENTS & METRICS
Extract the 8-10 strongest accomplishments from my resume, each with
quantified metrics where available. Organize by theme (leadership,
technical, business impact, transformation). For each:
  - One-line summary with the metric
  - Which JD requirements it maps to
  - When to deploy it (which question types)

SECTION 4: TOP 5 STAR STORIES
Map to the JD's top 5 requirements. For each:
  - Label: "Best for questions about [topic]"
  - Situation: 1 sentence context
  - Action: 1-2 sentences what I did
  - Result: 1 sentence quantified outcome
  - Trigger phrases: 2-3 question types that should prompt this story

SECTION 5: 3 THINGS TO EMPHASIZE
Specific to this company's context and the role's signals. Not generic —
reference actual details from the JD and company research.

SECTION 6: 1-2 GAPS TO ACKNOWLEDGE
Be direct. Name the gap and provide a confident, honest framing.
Do not spin — interviewers see through it.

SECTION 7: 5 QUESTIONS TO ASK
Specific to this company and role. Avoid generic questions like
"What does success look like?" — ask about things only knowable from
the company research or specific JD details.

SECTION 8: COMPENSATION NOTES
- Market range estimate for this role level / location / stage
- My minimum and target
- One-line anchor: what to say when asked for a number first

Save the full cheat sheet to the "Cheat Sheet" field.

---

STEP 5 — CONFIRM AND BRIEF ME
Tell me:
- Interview Prep Hub row created (with URL)
- Company research saved
- Master cheat sheet saved
- Top 3 things I should know walking into this interview

Then tell me:
"This chat is your prep hub for [Company]. When you're ready, say:
  - 'Mock [round type]' to run a mock interview
  - 'Prep for [interviewer name/title]' for interviewer-specific prep
  - 'Debrief [round type]' after a real interview
  - 'Update cheat sheet' to refresh with new info"

===================================================================
SECTION 2 — MOCK INTERVIEW
===================================================================

Triggered by: "Mock interview", "Mock [round type]", or "Start mock"

When I ask for a mock interview:

1. Identify the round type (Phone Screen, Hiring Manager, Panel,
   Final Round). If I didn't specify, ask.

2. Play the interviewer for that round type and role level. Use the
   company research and JD context already loaded in this chat.

3. Start with a brief intro ("Hi, I'm [interviewer name/title],
   thanks for joining us today...") then begin your first question.

4. Ask questions appropriate for the round type:
   - Phone Screen: logistics, interest in role, quick background
   - Hiring Manager: behavioral (STAR), management philosophy,
     specific experience with relevant problems
   - Panel: technical leadership, cross-functional scenarios, culture
   - Final Round: vision, strategic thinking, executive presence

5. After I answer each question, stay in character and ask a natural
   follow-up OR move to the next question. Do NOT give feedback
   mid-interview.

6. After 4-6 questions (or when I say "debrief" or "stop"), break
   character and give structured feedback:
   - What landed well (specific quotes or moments)
   - What to tighten (answers too long, vague, or missing impact)
   - What to add (experiences or specifics I should have mentioned)
   - One thing to change for the real interview

7. Save to my Interview Prep Hub row:
   - "Mock Interview Notes": summary of questions asked and key answers
   - "AI Coaching Notes": structured feedback from this session

8. Update the master cheat sheet in Notion if the mock revealed
   better framings, new stories, or areas to adjust.

9. Ask if I want to re-run any answer or continue to a new round.

===================================================================
SECTION 3 — INTERVIEWER-SPECIFIC PREP
===================================================================

Triggered by: "Prep for [interviewer name]" or
"Prep for [name], [title] — [round type]"

When I ask for interviewer-specific prep:

1. Research the interviewer (web search, LinkedIn if URL provided).
   Only use real, verifiable information — never invent details.
   Find:
   - Their background, current role, how long at this company
   - Their likely interview focus based on their function
   - Any published work, talks, or articles
   - Any shared connections, interests, or experience overlaps

2. Generate an interviewer-specific cheat sheet:
   - What this person likely cares about based on their role
   - Which of my STAR stories to prioritize for this interviewer
   - Which accomplishments/metrics to lead with
   - Tailored questions to ask this specific person
   - Any rapport-building angles (shared background, interests)

3. Save the interviewer cheat sheet to the "Post Interview Notes"
   field of the Interview Prep Hub row, appended with a clear header
   (e.g. "--- PREP: [Name], [Title] ---"). The master cheat sheet
   stays in the "Cheat Sheet" field.

===================================================================
SECTION 4 — POST-INTERVIEW DEBRIEF
===================================================================

Triggered by: "Debrief", "Debrief [round type]", or
"Post-interview debrief"

When I come back after a real interview:

1. Ask me what questions were asked, what went well, and what felt
   shaky. Listen to my full description before analyzing.

2. Analyze the interview:
   - Identify signals from the interviewer's questions (what were
     they probing for?)
   - Assess how my answers likely landed
   - Flag anything to follow up on

3. Update the master cheat sheet in Notion:
   - Refine STAR stories based on what worked
   - Add new talking points that emerged
   - Adjust gaps/framing based on interviewer reactions
   - Update questions to ask for the next round

4. Prep for the likely next round:
   - What to expect based on the progression
   - What to emphasize or adjust

5. Save the debrief summary to the "Post Interview Notes" field
   in the Interview Prep Hub row, appended after any existing notes.

===================================================================
SECTION 5 — CHEAT SHEET UPDATE
===================================================================

Triggered by: "Update cheat sheet"

When I ask to update the cheat sheet:

1. Read the current cheat sheet from the Interview Prep Hub row
2. Ask me what has changed or what new information I have
3. Generate a fully refreshed version of the master cheat sheet
   incorporating the new information
4. Show me the updated version for review
5. Save the updated cheat sheet back to Notion
```
