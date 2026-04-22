# CareerPilot

An AI career coaching platform built on Claude and Notion. Save job postings with a Chrome extension, get AI-optimized resumes for each role, and walk into every interview with a tailored cheat sheet — powered by Claude Projects, Claude Code, or OpenClaw.

---

## How It Works

```
Phase 1 — Save          Phase 2 — Review          Phase 3 — Prepare
─────────────────   →   ──────────────────────   →   ─────────────────────
Chrome Extension        Claude reads each JD         Per-opportunity Claude
saves job postings      evaluates fit, selects        Project generates
directly to Notion      & optimizes resume,           cheat sheets, company
Job Tracker database    writes back to Notion         research, mock interviews
```

---

## Repository Structure

```
ai-job-search-system/
├── README.md                          This file
├── LICENSE
├── .gitignore
├── .mcp.json                          MCP server config (Notion connector)
│
├── docs/
│   ├── overview.md                    Full system architecture
│   ├── claude-code-setup.md           Claude Code + MCP setup guide
│   ├── openclaw-setup.md              OpenClaw agent setup guide
│   ├── phase-1-extension.md           Chrome extension setup reference
│   ├── phase-2-job-review.md          AI job review workflow
│   ├── phase-3-interview-prep.md      Interview prep workflow
│   ├── notion-database-schema.md      All three database schemas
│   └── changelog.md                   Version history
│
├── prompts/
│   ├── system-prompt.md               Master context — upload to Project instructions
│   ├── onboarding.md                  First-time setup (run once)
│   ├── review-jobs.md                 Daily job review trigger
│   ├── interview-prep.md              Full interview lifecycle (init + mock + debrief)
│   ├── setup-validation.md            Post-setup verification checklist
│   └── resume-selection-rules-template.md  Blank rules template (optional)
│
├── skills/
│   ├── job-review-workflow/
│   │   └── SKILL.md                   Claude Code skill: automated job review
│   └── interview-prep-builder/
│       └── SKILL.md                   Claude Code skill: automated prep builder
│
├── config/
│   ├── notion-databases/
│   │   ├── job-tracker-schema.json
│   │   ├── resume-repository-schema.json
│   │   └── interview-prep-hub-schema.json
│   └── resume-selection-rules-template.md
│
├── website/
│   └── onboarding-site-build-prompt.md  Claude Code prompt for kssoftware.net
│
└── scripts/
    ├── scan-bookmarked-jobs.py        Phase 2B: scheduled job scanner
    ├── requirements.txt
    └── README.md
```

---

## Quick Start

1. **Duplicate the Notion Template** — Duplicate the template at [CareerPilot Notion Template](https://www.notion.so/342037c8790b819195a6f4aea08e8bb4) — all three databases and the dashboard are included.
2. **Install the Chrome Extension** — [Job Post Tracker on Chrome Web Store](https://chromewebstore.google.com/detail/ponffclikgodccpghpammcpjpjeojopj?utm_source=item-share-cb)
3. **Set Up Claude Project** — upload `prompts/system-prompt.md` to the project instructions
4. **Run onboarding** — paste `prompts/onboarding.md` to configure resumes and selection rules
5. **Validate your setup** — run `prompts/setup-validation.md` to verify everything is connected
6. **Start saving jobs** — bookmark roles and say "Review bookmarked jobs" in your Claude Project

See how it works: [kssoftware.net/CareerCopilot](https://kssoftware.net/CareerCopilot/how-it-works.html)

---

## Setup Order

| Step | File | How to Use |
|---|---|---|
| 1 | `prompts/system-prompt.md` | Upload to Claude Project **instructions** (not knowledge). Runs silently in every conversation. |
| 2 | `prompts/onboarding.md` | Paste into a chat in your Claude Project. Run once to set up resumes and selection rules. |
| 3 | `prompts/setup-validation.md` | Paste into a chat to verify everything is connected and working. |
| 4 | `prompts/review-jobs.md` | Say "Review bookmarked jobs" — or paste this prompt for the full workflow instructions. |
| 5 | `prompts/interview-prep.md` | Start a new chat per opportunity. Covers init, mock interviews, debriefs, and cheat sheet updates. |
| — | `prompts/resume-selection-rules-template.md` | Optional. Blank template for manual setup if you skip interactive onboarding. |

---

## Prerequisites

- Google Chrome browser
- [Notion account](https://notion.so) (free tier works)
- [Claude account](https://claude.ai) (free for setup; Pro recommended for daily use)
- Your existing resumes in any format (Word, PDF, or text)
- **For Claude Code automation:** [Claude Code CLI](https://claude.ai/code) and Node.js (for the Notion MCP server)
- **For OpenClaw automation:** [OpenClaw](https://openclaw.ai) and an Anthropic API key or Claude subscription

---

## Related Repositories

- **Chrome Extension**: [bigunit5150/JobTrackerChromeExtension](https://github.com/bigunit5150/JobTrackerChromeExtension)
- **LLM Gateway**: [bigunit5150/ModelGatewayProxy](https://github.com/bigunit5150/ModelGatewayProxy)
- **Portfolio Site**: [kssoftware.net](https://kssoftware.net)

---

## License

PolyForm Noncommercial License 1.0.0 — see `LICENSE` for details. Free for personal and noncommercial use; commercial use (including selling) is not permitted.
