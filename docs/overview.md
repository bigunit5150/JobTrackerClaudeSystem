# System Overview

## What This Is

A three-phase AI-powered job search system that eliminates the manual work of
job applications. It uses a Chrome extension to capture job postings, Claude AI
to evaluate fit and optimize resumes, and a dedicated Claude Project per
opportunity to handle interview preparation — all coordinated through a Notion
workspace.

---

## Architecture

### The Three Phases

**Phase 1 — Capture (Chrome Extension)**
When you find a job posting on any job board, click the Job Post Tracker
extension. It saves the role title, company, and full job description directly
to your Notion Job Tracker database with Status set to "Bookmarked". No
copy-pasting, no manual entry.

**Phase 2 — Review (Claude AI Job Review)**
In your Claude Project, say "Review bookmarked jobs." Claude reads every
Bookmarked row, runs a fit assessment against your Resume Selection Rules,
selects the appropriate resume variant, rewrites it to mirror the JD language,
and writes the result back to Notion — updating AI Notes, Resume, and Status
in one pass.

**Phase 3 — Prepare (Per-Opportunity Claude Project)**
When you decide to pursue a role, create a new Claude Project for that
opportunity. Run the Interview Prep initialization prompt. Claude researches
the company, generates a cheat sheet with your top stories mapped to the JD,
and prepares mock interview questions. Subsequent chats in the same project
build on this context for each interview round.

---

### Data Flow

```
[Job Board] ──► [Chrome Extension] ──► [Notion: Job Tracker]
                                              │
                                        Status: Bookmarked
                                              │
                                    [Claude Project: Job Search]
                                              │
                                        Fit Assessment
                                        Resume Selection
                                        Resume Optimization
                                              │
                                    Notion Write-Back:
                                    - AI Notes (assessment)
                                    - Resume (optimized text)
                                    - Status: AI Reviewed
                                              │
                                    You decide to apply
                                              │
                                    [New Claude Project: [Company]]
                                              │
                                        Company Research
                                        Cheat Sheet Generation
                                        Mock Interviews
                                              │
                                    [Notion: Interview Prep Hub]
                                    - Cheat Sheet
                                    - Company Research
                                    - Mock Interview Notes
                                    - Post-Interview Debrief
```

---

### Notion Workspace Structure

Three databases, all living in a single Notion parent page:

| Database | Purpose |
|---|---|
| Job Tracker | Every job saved, with status, JD, AI notes, and optimized resume |
| Resume Repository | Base resumes + selection rules document |
| Interview Prep Hub | Per-opportunity prep: research, cheat sheets, interview notes |

---

### Claude Projects Structure

| Project | Purpose |
|---|---|
| [Your Name] — Job Search | Phase 2 home: all job reviews run here |
| [Company] — [Role] | Phase 3: one project per opportunity being actively pursued |

The Job Search project holds your Resume Selection Rules as project knowledge.
Each opportunity project is seeded with the JD and your optimized resume at init.

---

## Key Design Decisions

**Why Notion?**
Notion's MCP connector lets Claude read and write directly to databases without
any custom backend. It's free, flexible, and most job seekers already use it.

**Why a Chrome Extension for capture?**
Manual copy-paste of JDs introduces errors and friction. The extension captures
the full raw JD text reliably, which is what Claude needs for accurate
fit assessment and keyword mirroring.

**Why per-opportunity Claude Projects?**
Claude Projects persist context across conversations. A dedicated project per
role means Claude remembers the company, your resume, previous interviews, and
feedback — without you re-explaining it in every chat. Each chat builds on
the last.

**Why Skills for Phase 2B?**
The job review workflow (fit → select → optimize → write-back) is fully
autonomous once configured. Wrapping it as a Claude Code Skill enables
scheduled automation and chaining with other skills — no human in the loop.

---

## What This System Does Not Do

- Does not auto-apply to jobs on your behalf
- Does not fabricate experience or invent metrics on resumes
- Does not replace your judgment on which roles to pursue
- Does not handle compensation negotiation
