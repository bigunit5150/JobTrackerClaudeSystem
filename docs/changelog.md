# Changelog

All notable changes to prompts, skills, and configuration files are documented here.

---

## [1.1.0] — 2026-04-02

### Added

- `.mcp.json` — project-level MCP configuration for Notion MCP server
- `docs/claude-code-setup.md` — full setup guide for Claude Code with MCP
- `docs/openclaw-setup.md` — full setup guide for OpenClaw agent with
  cron, heartbeat, and chat integration

### Changed

- `docs/overview.md` — added "Three Ways to Run the System" section covering
  Claude Projects, Claude Code, and OpenClaw execution modes
- `docs/phase-2-job-review.md` — added Option B (Claude Code) and Option C
  (OpenClaw) trigger modes
- `docs/phase-3-interview-prep.md` — added Option B (Claude Code) and
  Option C (OpenClaw) for automated interview prep initialization
- `README.md` — updated description, repo structure, quick start, and
  prerequisites to reflect Claude Code and OpenClaw support
- `docs/notion-database-schema.md` — added "Written by" column to all tables
  clarifying who populates each field (Extension, Claude, User); removed
  Claude Project URL field; updated Cheat Sheet and Post Interview Notes
  descriptions for new workflow
- `prompts/interview-prep-init.md` — rewritten as unified interview lifecycle
  prompt: single chat per opportunity, expanded cheat sheet (self-introduction,
  why this company, key accomplishments/metrics), interviewer-specific cheat
  sheets, living master cheat sheet updated after each round
- `prompts/mock-interview.md` — simplified to quick reference for mock
  interview commands (full workflow now in interview-prep-init.md)
- `skills/interview-prep-builder/SKILL.md` — updated cheat sheet generation
  to include all 8 sections (self-intro, why this company, accomplishments,
  STAR stories, talking points, gaps, questions, comp notes)
- `docs/phase-3-interview-prep.md` — rewritten for single-chat-per-opportunity
  model with interviewer-specific prep and living cheat sheet
- `docs/overview.md` — updated Phase 3 description and data flow diagram
- `prompts/new-user-onboarding.md` — added Phase 3 for uploading reusable
  prompts to project knowledge; all prompts now uploaded to one project
- Moved all prompts to flat `prompts/` directory, removed subdirectories
- Updated all path references across docs and skills

---

## [1.0.0] — 2026-03-29

### Added

- Initial repository structure
- `new-user-onboarding.md` — full guided setup prompt
- `review-bookmarked-jobs.md` — daily review prompt
- `interview-prep-init.md` — opportunity initialization
- `mock-interview.md` — mock interview runner
- `resume-optimization-rules-template.md` — blank rules template
- `skills/job-review-workflow/SKILL.md` — automated review orchestrator skill
- `skills/interview-prep-builder/SKILL.md` — automated prep builder skill
- `config/notion-databases/` — JSON schemas for all three databases
- `config/resume-selection-rules-template.md` — configuration template
- `docs/` — full system documentation
- `scripts/scan-bookmarked-jobs.py` — Phase 2B scheduled scanner stub
- `website/onboarding-site-build-prompt.md` — Claude Code site build prompt

### Notion Infrastructure

- Job Tracker database created
- Resume Repository database created
- Interview Prep Hub database created
- AI Workflow Configuration page created in Career Development Tracker

---

## Versioning Convention

Prompt and skill files include a version header block:

```yaml
---
version: 1.0
last_updated: YYYY-MM-DD
---
```

When a prompt is updated, bump the version, update `last_updated`,
and add an entry to this changelog describing what changed and why.
