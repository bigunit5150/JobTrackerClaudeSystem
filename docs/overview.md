# System Overview

## What This Is

A three-phase AI-powered job search system that eliminates the manual work of
job applications. It uses a Chrome extension to capture job postings, Claude AI
to evaluate fit and optimize resumes, and a per-opportunity chat thread to
handle interview preparation — all coordinated through a Notion workspace.

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

**Phase 3 — Prepare (Per-Opportunity Chat)**
When you decide to pursue a role, start a new chat in your Job Search Claude
Project. Run the Interview Prep initialization prompt. Claude researches
the company, generates a master cheat sheet (self-introduction, key
accomplishments, STAR stories, company-specific motivation, and more), and
prepares mock interview questions. The entire interview lifecycle — mock
interviews, interviewer-specific prep, post-interview debriefs — happens
in this one chat, building context with each interaction.

---

### Data Flow

```text
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
                                    [New Chat in same Project]
                                              │
                                        Company Research
                                        Master Cheat Sheet
                                        Mock Interviews
                                        Interviewer-Specific Prep
                                        Post-Interview Debriefs
                                              │
                                    [Notion: Interview Prep Hub]
                                    - Cheat Sheet (living document)
                                    - Company Research
                                    - Mock Interview Notes
                                    - Post-Interview Notes
```

---

### Notion Workspace Structure

Three databases, all living in a single Notion parent page:

| Database | Purpose |
| --- | --- |
| Job Tracker | Every job saved, with status, JD, AI notes, and optimized resume |
| Resume Repository | Base resumes + selection rules document |
| Interview Prep Hub | Per-opportunity prep: research, cheat sheets, interview notes |

---

### Three Ways to Run the System

This system supports three execution modes. Use whichever fits your workflow,
or mix them.

#### Claude Projects (claude.ai)

Interactive mode. You run prompts in Claude Projects with the Notion
integration enabled under Settings > Integrations > Notion.

| Project | Purpose |
| --- | --- |
| [Your Name] — Job Search | Phase 2 home: all job reviews run here |
| [Company] — [Role] | Phase 3: one project per opportunity being actively pursued |

The Job Search project holds your Resume Selection Rules as project knowledge.
Each opportunity project is seeded with the JD and your optimized resume at init.

#### Claude Code (CLI / IDE)

Automation mode. Claude Code connects to Notion via the MCP server configured
in `.mcp.json` at the project root. This enables the Skills in `skills/` to
run fully autonomously — reading from and writing to your Notion databases
with no browser session required.

**Setup:** See `docs/claude-code-setup.md`.

#### OpenClaw (Always-On Agent)

Autonomous mode. [OpenClaw](https://openclaw.ai) is an open-source AI agent
that runs locally and uses Claude as its backend. It loads the Skills from
this project's `skills/` directory (the SKILL.md format is AgentSkills-compatible)
and can run them on a schedule via cron or heartbeat — processing new jobs
automatically as they appear, with no manual trigger required.

OpenClaw also connects to your existing chat platforms (WhatsApp, Slack,
Discord, etc.), so you can interact with your job search workflow from
wherever you already communicate.

**Setup:** See `docs/openclaw-setup.md`.

---

## Key Design Decisions

**Why Notion?**
Notion's MCP connector lets Claude read and write directly to databases without
any custom backend. It's free, flexible, and most job seekers already use it.
Both Claude Projects (via the built-in Notion integration) and Claude Code
(via the Notion MCP server) can connect to the same workspace.

**Why a Chrome Extension for capture?**
Manual copy-paste of JDs introduces errors and friction. The extension captures
the full raw JD text reliably, which is what Claude needs for accurate
fit assessment and keyword mirroring.

**Why one chat per opportunity?**
Each opportunity gets its own chat within your Job Search project. The entire
interview lifecycle — initialization, mock interviews, interviewer-specific
prep, debriefs — stays in one conversation thread. Claude retains full context
so it can update your cheat sheet after each round and tailor prep for the
next interviewer without you re-explaining anything.

**Why AgentSkills for automation?**
The job review workflow (fit → select → optimize → write-back) is fully
autonomous once configured. The Skills use the AgentSkills-compatible SKILL.md
format, which works in both Claude Code (via MCP) and OpenClaw (via built-in
tools). This means the same skill definitions power scheduled automation
across either platform — no human in the loop, no browser required.

---

## What This System Does Not Do

- Does not auto-apply to jobs on your behalf
- Does not fabricate experience or invent metrics on resumes
- Does not replace your judgment on which roles to pursue
- Does not handle compensation negotiation
