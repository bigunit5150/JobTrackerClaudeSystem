# Scripts

## scan-bookmarked-jobs.py

Phase 2B automation: queries Notion for Bookmarked jobs and sends each
to Claude for fit assessment and resume optimization.

This is the scheduled alternative to the manual Phase 2 prompt. Use it
once the manual workflow is validated and you want hands-free processing.

---

## Setup

### 1. Install dependencies

```bash
cd scripts
pip install -r requirements.txt
```

### 2. Set environment variables

Create a `.env` file in the `scripts/` directory (never commit this):

```bash
NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_DB_ID=320037c8790b80049498d26d7d85322c
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Or export them in your shell:

```bash
export NOTION_TOKEN=secret_...
export NOTION_DB_ID=...
export ANTHROPIC_API_KEY=sk-ant-...
```

### 3. Test with a dry run

```bash
DRY_RUN=true python scan-bookmarked-jobs.py
```

This will find and list all Bookmarked jobs without calling the Claude API
or modifying any Notion rows.

### 4. Run for real

```bash
python scan-bookmarked-jobs.py
```

---

## Scheduling Options

### Option A — cron (macOS / Linux)

Run daily at 8 AM:

```bash
crontab -e
# Add this line:
0 8 * * * cd /path/to/scripts && python scan-bookmarked-jobs.py >> /tmp/job-scan.log 2>&1
```

### Option B — GitHub Actions

Add this workflow to your repository at `.github/workflows/scan-jobs.yml`:

```yaml
name: Scan Bookmarked Jobs

on:
  schedule:
    - cron: '0 15 * * *'  # Daily at 8 AM PT (15:00 UTC)
  workflow_dispatch:        # Allow manual trigger from GitHub UI

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r scripts/requirements.txt

      - name: Run job scanner
        run: python scripts/scan-bookmarked-jobs.py
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          NOTION_DB_ID: ${{ secrets.NOTION_DB_ID }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

Add your secrets in: GitHub repo → Settings → Secrets and variables → Actions.

### Option C — Notion Automation + Webhook (Real-time)

For immediate processing when a job is saved:

1. In Notion, open your Job Tracker database
2. Click **...** → **Automations** → **+ New automation**
3. Trigger: "Property is edited" → Status → equals → Bookmarked
4. Action: "Send webhook" → paste your webhook URL

The webhook receiver (Make, n8n, or a custom endpoint) then calls the
Claude API with the specific page ID. This is the most seamless option
but requires a webhook hosting setup.

---

## Environment Variables Reference

| Variable | Required | Description |
|---|---|---|
| `NOTION_TOKEN` | Yes | Notion Internal Integration Token (`secret_...`) |
| `NOTION_DB_ID` | Yes | Job Tracker database ID (32 hex characters) |
| `ANTHROPIC_API_KEY` | Yes | Claude API key (`sk-ant-...`) |
| `DRY_RUN` | No | Set to `true` to list jobs without processing. Default: `false` |
| `MAX_JOBS` | No | Max jobs to process per run. Default: `10` |

---

## Known Limitations

- The script calls Claude API once per job — costs approximately $0.01-0.03
  per job depending on JD length and resume length
- Notion's `rich_text` property type is capped at 2000 characters in API
  responses; very long resumes may be truncated in the Notion row
- Resume Selection Rules are not yet read from Notion in this version —
  the Claude prompt is generic. A future version will fetch and inject
  your rules document automatically
