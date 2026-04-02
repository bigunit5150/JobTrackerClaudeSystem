# AI Job Search System

An AI-powered job search workflow built on Claude and Notion. Save job postings with a Chrome extension, get AI-optimized resumes for each role, and walk into every interview with a tailored cheat sheet — automated through Claude Projects, Claude Code, or OpenClaw.

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
│   ├── new-user-onboarding.md         Guided first-time setup prompt
│   ├── review-bookmarked-jobs.md      Daily job review prompt
│   ├── interview-prep-init.md         Per-opportunity prep prompt
│   ├── mock-interview.md              Mock interview runner prompt
│   └── resume-optimization-rules-template.md  Blank rules template
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

1. **Install the Chrome Extension** — [Job Post Tracker on Chrome Web Store](https://chromewebstore.google.com/detail/ponffclikgodccpghpammcpjpjeojopj?utm_source=item-share-cb)
2. **Set up Notion** — follow `docs/phase-1-extension.md` and create the three databases defined in `config/notion-databases/`
3. **Configure Claude** — create a Claude Project and run the prompt in `prompts/new-user-onboarding.md`
4. **Start saving jobs** — bookmark roles and say "Review bookmarked jobs" in your Claude Project
5. **Optional: Set up Claude Code** — follow `docs/claude-code-setup.md` to enable automated workflows via the CLI
6. **Optional: Set up OpenClaw** — follow `docs/openclaw-setup.md` for always-on autonomous processing via [OpenClaw](https://openclaw.ai)

Full setup guide: [kssoftware.net/CareerCopilot](https://kssoftware.net/CareerCopilot)

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
