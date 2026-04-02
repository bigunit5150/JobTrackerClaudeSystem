# OpenClaw Setup

This guide covers setting up [OpenClaw](https://openclaw.ai) to run the
automated skills in this project. OpenClaw is an open-source AI agent that
runs locally, uses Claude as its backend, and can process your job search
workflows autonomously on a schedule or via chat.

---

## Prerequisites

- Node.js 22+ (24 recommended)
- An Anthropic API key or Claude subscription
- Notion workspace with the three databases already created
  (see `docs/notion-database-schema.md`)
- A Notion integration token (see Step 2 below)

---

## Step 1: Install OpenClaw

```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon
```

During onboarding, choose Anthropic as your model provider and provide your
API key when prompted. Alternatively, if you have a Claude subscription:

```bash
# Generate a setup token from the Claude CLI
claude setup-token
# Then paste it into OpenClaw
openclaw models auth setup-token --provider anthropic
```

---

## Step 2: Create a Notion Integration

1. Go to [notion.so/profile/integrations](https://www.notion.so/profile/integrations)
2. Click **New integration** and name it (e.g. "OpenClaw Job Search")
3. Set the type to **Internal**
4. Copy the **integration secret** (starts with `ntn_`)
5. Grant access: open each database (Job Tracker, Resume Repository,
   Interview Prep Hub) in Notion, click **...** > **Connections**, and
   add your integration

---

## Step 3: Configure the Workspace

Point OpenClaw's agent workspace to this project so it picks up the skills:

```bash
openclaw config set agents.defaults.workspace "$(pwd)"
```

Or edit `~/.openclaw/openclaw.json` directly:

```json5
{
  agents: {
    defaults: {
      model: { primary: "anthropic/claude-sonnet-4-6" },
      workspace: "/path/to/JobTrackerClaudeSystem"
    }
  }
}
```

---

## Step 4: Set the Notion Token

Add your Notion integration secret so the skills can access your databases:

```bash
openclaw config set env.NOTION_TOKEN "ntn_YOUR_TOKEN_HERE"
```

Or add it to your shell profile:

```bash
# Add to ~/.zshrc or ~/.bashrc
export NOTION_TOKEN="ntn_YOUR_TOKEN_HERE"
```

---

## Step 5: Configure the Notion Skill

Enable the Notion MCP server as a skill dependency in OpenClaw's config:

```json5
{
  skills: {
    entries: {
      "job-review-workflow": {
        enabled: true,
        env: { "NOTION_TOKEN": "${NOTION_TOKEN}" }
      },
      "interview-prep-builder": {
        enabled: true,
        env: { "NOTION_TOKEN": "${NOTION_TOKEN}" }
      }
    }
  }
}
```

---

## Step 6: Verify

```bash
# Check that skills are loaded
openclaw "List the skills available in my workspace"

# Test Notion access
openclaw "Read my Notion Job Tracker database and tell me how many rows it has"
```

---

## Scheduling Automated Job Reviews

OpenClaw supports cron-based scheduling to process Bookmarked jobs
automatically. You can set this up via chat or configuration.

### Via Chat

Tell your OpenClaw agent:

```text
Set up a cron job to run the job-review-workflow skill every day at 9am.
Process all Bookmarked jobs in my Notion Job Tracker.
```

### Via Configuration

Add to `~/.openclaw/openclaw.json`:

```json5
{
  cron: {
    enabled: true,
    maxConcurrentRuns: 1
  }
}
```

Then ask OpenClaw to create the scheduled task, or use the HEARTBEAT.md
file in your workspace to define recurring checks.

### Via Heartbeat

Create a `HEARTBEAT.md` file in your workspace root:

```markdown
Check my Notion Job Tracker for any jobs with Status = "Bookmarked".
If there are new Bookmarked jobs, run the job-review-workflow skill
to process them.
```

OpenClaw's heartbeat runs every 30 minutes by default. Adjust the interval:

```bash
openclaw config set heartbeat.every "1h"
```

---

## Chat Integration

One of OpenClaw's strengths is that you can interact with your job search
workflow from any chat platform. After connecting a channel (WhatsApp,
Slack, Discord, etc.), you can:

- Say "Review my bookmarked jobs" to trigger the job-review-workflow skill
- Say "Prep me for [Company] [Role]" to trigger interview-prep-builder
- Ask "How many jobs did you review today?" to check status
- Get notified when new jobs are processed

Set up a channel:

```bash
# Example: connect WhatsApp
openclaw channels setup whatsapp

# Example: connect Slack
openclaw channels setup slack
```

See the [OpenClaw channels docs](https://docs.openclaw.ai/channels/) for
all supported platforms.

---

## Claude Code vs OpenClaw

Both can run the same skills against the same Notion databases. Choose
based on your workflow:

| | Claude Code | OpenClaw |
| --- | --- | --- |
| **Runs when** | You invoke it | Always on (daemon) |
| **Trigger** | Manual CLI command | Cron, heartbeat, chat message |
| **Chat access** | Terminal only | WhatsApp, Slack, Discord, etc. |
| **Memory** | Fresh each session | Persistent across sessions |
| **Best for** | On-demand batch runs | Fully autonomous operation |
| **Notion access** | MCP server (`.mcp.json`) | exec/web_fetch tools |

You can use both. For example, use OpenClaw for daily automated reviews
and Claude Code for one-off tasks or debugging.

---

## Troubleshooting

**Skills not loading**

- Verify workspace path: `openclaw config get agents.defaults.workspace`
- Check that `skills/` directory exists at that path
- Run `openclaw doctor` to diagnose configuration issues

**Cannot access Notion**

- Verify token is set: `openclaw config get env.NOTION_TOKEN`
- Confirm the integration is connected to each database in Notion
- Test manually: `openclaw "Read my Notion Job Tracker"`

**Agent not using Claude**

- Verify provider: `openclaw config get agents.defaults.model`
- Should show `anthropic/claude-sonnet-4-6` or similar
- Check API key: `openclaw models auth status`

**Heartbeat not running**

- Verify daemon is running: `openclaw status`
- Check heartbeat config: `openclaw config get heartbeat`
- Review logs: `openclaw logs`
