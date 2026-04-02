---
prompt: Mock Interview Runner
phase: 3 — Interview Prep
version: 1.0
last_updated: 2026-03-29
depends_on: Interview prep initialized in this project
trigger: New chat in the same opportunity Claude Project
---

# Mock Interview Prompt

**Where to use:** The Claude Project for the specific opportunity (same project
where you ran the initialization prompt — context is already loaded).
**When to use:** Before any interview round. Run multiple times for different rounds.

---

## The Prompt

```
Let's run a mock interview. I have an upcoming [ROUND TYPE] interview
with [COMPANY] for the [ROLE TITLE] role.

Round type options:
- Phone Screen (recruiter, 30 min)
- Hiring Manager (45-60 min, behavioral + experience)
- Panel (60-90 min, multiple interviewers)
- Final Round (exec/leadership, strategic + culture)

---

INSTRUCTIONS FOR YOU (Claude):

1. Play the role of the interviewer for this specific round type and
   role level. Use what you know about this company and role from our
   earlier prep session.

2. Start with a brief intro ("Hi, I'm [interviewer name/title], thanks
   for joining us today...") then begin your first question.

3. Ask questions appropriate for the round type:
   - Phone Screen: logistics, interest in role, quick background check
   - Hiring Manager: behavioral (STAR format), management philosophy,
     specific experience with relevant problems
   - Panel: technical leadership, cross-functional scenarios, culture fit
   - Final Round: vision, strategic thinking, executive presence

4. After I answer each question:
   - Stay in character and ask a natural follow-up OR move to the next question
   - Do NOT give feedback mid-interview (save it for the debrief)

5. After 4-6 questions (or when I say "let's debrief"), break character
   and give me structured feedback:
   - What landed well (specific quotes or moments)
   - What to tighten (specific answers that were too long, too vague,
     or missing impact)
   - What to add (experiences or specifics I should have mentioned)
   - One thing to change for the real interview

6. Ask if I want to re-run any answer or continue to a new round.

---

Start the mock interview now.
```

---

## Post-Interview Debrief Prompt

After a real interview round, start a new chat in the project and say:

```
I just finished my [ROUND TYPE] interview with [COMPANY]. Let me debrief.

Here's how it went:
[Describe the interview — questions asked, how you answered, anything
surprising, your read on how it went]

Based on this, help me:
1. Identify what signals the interviewer's questions were sending
2. Assess how well my answers landed
3. Prep for the likely next round
4. Update my cheat sheet if anything new came up

Then save a summary of this debrief to the "Post Interview Notes" field
in my Interview Prep Hub row for this opportunity.
```
