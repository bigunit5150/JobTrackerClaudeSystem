# Claude Code Setup

This guide covers setting up Claude Code to run the automated skills in this
project. Claude Code connects to your Notion workspace via an MCP server,
giving the skills direct read/write access to your databases.

---

## Prerequisites

- [Claude Code](https://claude.ai/code) installed (CLI, VS Code extension, or JetBrains plugin)
- Node.js 18+ (required to run the Notion MCP server)
- Notion workspace with the three databases already created (see `docs/notion-database-schema.md`)

---

## Step 1: Create a Notion Integration

1. Go to [notion.so/profile/integrations](https://www.notion.so/profile/integrations)
2. Click **New integration**
3. Name it something like "Claude Code Job Search"
4. Set the type to **Internal**
5. Copy the **integration secret** (starts with `ntn_`)

---

## Step 2: Grant Database Access

Your integration needs explicit access to each database it will read or write.

For each of your three databases (Job Tracker, Resume Repository, Interview Prep Hub):

1. Open the database page in Notion
2. Click the **...** menu in the top right
3. Select **Connections** (or **Add connections**)
4. Search for and add your "Claude Code Job Search" integration

---

## Step 3: Set Your Environment Variable

Add your Notion token to your shell profile so Claude Code can use it:

```bash
# Add to ~/.zshrc, ~/.bashrc, or ~/.zprofile
export NOTION_TOKEN="ntn_YOUR_TOKEN_HERE"
```

Then reload your shell:

```bash
source ~/.zshrc
```

Do not commit your token to the repository. The `.mcp.json` file references
`${NOTION_TOKEN}` from your environment, keeping the secret out of version
control.

---

## Step 4: Verify the MCP Connection

The project includes a `.mcp.json` file that configures the Notion MCP server
automatically. When you open this project in Claude Code, the server starts
on demand.

To verify:

```bash
# From the project root
claude "List the databases available in my Notion workspace"
```

Claude should be able to see your Job Tracker, Resume Repository, and
Interview Prep Hub databases. If it cannot, check that:

- `NOTION_TOKEN` is set in your current shell
- The integration has been connected to each database (Step 2)
- Node.js is installed and `npx` is available

---

## MCP Configuration

The `.mcp.json` file at the project root defines the Notion MCP server:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_TOKEN": "${NOTION_TOKEN}"
      }
    }
  }
}
```

This is a **project-scoped** configuration. Claude Code will prompt you to
approve the MCP server the first time you use it in this project.

### Scope Options

| Scope | File | Shared | Use case |
| --- | --- | --- | --- |
| Project | `.mcp.json` (repo root) | Yes (version controlled) | Default for this repo |
| Local | `~/.claude.json` (per-project key) | No | Override token per machine |
| User | `~/.claude.json` (global key) | No | Use across all projects |

To add the server at user scope instead (available in all projects):

```bash
claude mcp add notion --scope user -- npx -y @notionhq/notion-mcp-server
```

---

## Available Skills

Once the MCP connection is active, you can run these skills:

### job-review-workflow

Processes all Bookmarked jobs in your Job Tracker autonomously.

```bash
claude "Run the job-review-workflow skill"
```

What it does:
1. Loads your Resume Selection Rules from Notion
2. Reads all active resume variants
3. Fetches every job with Status = "Bookmarked"
4. For each job: runs fit assessment, selects and optimizes a resume, writes back to Notion

See `skills/job-review-workflow/SKILL.md` for full details.

### interview-prep-builder

Initializes interview prep for a specific opportunity.

```bash
claude "Run the interview-prep-builder skill for [NOTION ROW URL]"
```

What it does:
1. Reads the job details and optimized resume from the Job Tracker row
2. Creates an Interview Prep Hub row
3. Researches the company via web search
4. Generates a cheat sheet with STAR stories, talking points, and questions
5. Writes everything back to Notion

See `skills/interview-prep-builder/SKILL.md` for full details.

---

## Claude Projects vs Claude Code

Both modes connect to the same Notion workspace and databases. Choose based
on what you need:

| | Claude Projects | Claude Code |
| --- | --- | --- |
| **Interface** | Browser (claude.ai) | CLI / IDE |
| **Notion access** | Built-in integration | MCP server (`.mcp.json`) |
| **Best for** | Interactive review, mock interviews, onboarding | Automated workflows, batch processing, scheduled runs |
| **Context** | Project knowledge persists across chats | Fresh context per session (reads from Notion each time) |
| **Human in the loop** | Yes | Optional |

**Recommended workflow:** Use Claude Projects for onboarding, interactive job
review, and interview prep. Use Claude Code for batch processing and automation
once you trust the workflow.

---

## Troubleshooting

**"MCP server not found" or Notion tools not available**
- Restart Claude Code after creating `.mcp.json`
- Check that Node.js and `npx` are installed: `npx --version`
- Approve the MCP server when prompted on first use

**"Unauthorized" or cannot read databases**
- Verify `NOTION_TOKEN` is set: `echo $NOTION_TOKEN`
- Confirm the integration is connected to each database in Notion (Step 2)
- Check the token hasn't been revoked at notion.so/profile/integrations

**Slow MCP server startup**
- First run downloads `@notionhq/notion-mcp-server` via npx. Subsequent runs
  use the cached version and start faster.
