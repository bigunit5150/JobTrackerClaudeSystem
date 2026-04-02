# Changelog

All notable changes to prompts, skills, and configuration files are documented here.

---

## [1.0.0] — 2026-03-29

### Added
- Initial repository structure
- `prompts/onboarding/new-user-onboarding.md` — full guided setup prompt
- `prompts/job-review/review-bookmarked-jobs.md` — daily review prompt
- `prompts/interview-prep/interview-prep-init.md` — opportunity initialization
- `prompts/interview-prep/mock-interview.md` — mock interview runner
- `prompts/resume/resume-optimization-rules-template.md` — blank rules template
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
```
---
version: 1.0
last_updated: YYYY-MM-DD
---
```

When a prompt is updated, bump the version, update `last_updated`,
and add an entry to this changelog describing what changed and why.
