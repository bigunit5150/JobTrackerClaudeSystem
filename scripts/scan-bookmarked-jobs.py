"""
scan-bookmarked-jobs.py
Phase 2B: Scheduled scanner for Bookmarked jobs in Notion Job Tracker.

Queries the Notion Job Tracker database for all rows with Status = "Bookmarked"
and triggers Claude API processing for each. Intended to run on a schedule
(cron, GitHub Actions) as the automated alternative to the manual Phase 2 prompt.

Usage:
    python scan-bookmarked-jobs.py

Environment variables required:
    NOTION_TOKEN         - Notion Internal Integration Token
    NOTION_DB_ID         - Job Tracker database ID
    ANTHROPIC_API_KEY    - Claude API key

Optional:
    DRY_RUN=true         - Print found jobs without calling Claude API
    MAX_JOBS=10          - Limit number of jobs to process per run (default: 10)

See scripts/README.md for full setup and scheduling instructions.
"""

import os
import json
import sys
import logging
from datetime import datetime

# ---------------------------------------------------------------------------
# Dependencies: pip install requests anthropic
# ---------------------------------------------------------------------------
try:
    import requests
except ImportError:
    sys.exit("Missing dependency: pip install requests")

try:
    import anthropic
except ImportError:
    sys.exit("Missing dependency: pip install anthropic")


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
NOTION_DB_ID = os.environ.get("NOTION_DB_ID")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"
MAX_JOBS = int(os.environ.get("MAX_JOBS", "10"))

NOTION_VERSION = "2022-06-28"
NOTION_BASE = "https://api.notion.com/v1"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Notion helpers
# ---------------------------------------------------------------------------
def notion_headers():
    return {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def get_bookmarked_jobs(limit: int = MAX_JOBS) -> list[dict]:
    """Query Job Tracker for all rows with Status = Bookmarked."""
    url = f"{NOTION_BASE}/databases/{NOTION_DB_ID}/query"
    payload = {
        "filter": {
            "property": "Status",
            "select": {"equals": "Bookmarked"},
        },
        "page_size": limit,
    }
    response = requests.post(url, headers=notion_headers(), json=payload)
    response.raise_for_status()
    return response.json().get("results", [])


def extract_text_property(page: dict, prop_name: str) -> str:
    """Extract plain text from a Notion page property."""
    props = page.get("properties", {})
    prop = props.get(prop_name, {})
    prop_type = prop.get("type", "")

    if prop_type == "title":
        items = prop.get("title", [])
    elif prop_type == "rich_text":
        items = prop.get("rich_text", [])
    elif prop_type == "select":
        select = prop.get("select")
        return select.get("name", "") if select else ""
    elif prop_type == "url":
        return prop.get("url", "") or ""
    else:
        return ""

    return "".join(item.get("plain_text", "") for item in items)


def update_job_row(page_id: str, ai_notes: str, resume: str, status: str):
    """Write AI Notes, Resume, and Status back to a Notion job row."""
    url = f"{NOTION_BASE}/pages/{page_id}"
    payload = {
        "properties": {
            "AI Notes": {
                "rich_text": [{"type": "text", "text": {"content": ai_notes[:2000]}}]
            },
            "Resume": {
                "rich_text": [{"type": "text", "text": {"content": resume[:2000]}}]
            },
            "Status": {
                "select": {"name": status}
            },
        }
    }
    response = requests.patch(url, headers=notion_headers(), json=payload)
    response.raise_for_status()
    return response.json()


# ---------------------------------------------------------------------------
# Claude API
# ---------------------------------------------------------------------------
def build_review_prompt(role_title: str, company: str, raw_jd: str) -> str:
    """Build the job review prompt for a single job."""
    return f"""You are reviewing a job posting for a job seeker. Using the Resume Selection Rules 
stored in their Notion Resume Repository, evaluate this role and produce an optimized resume.

JOB DETAILS:
Role Title: {role_title}
Company: {company}

JOB DESCRIPTION:
{raw_jd[:4000]}

---

Follow these steps:

1. FIT ASSESSMENT
   Evaluate: compensation (flag if not mentioned), role level, location, top 5 JD requirements 
   mapped to candidate experience (Strong / Partial / Gap). Assign: Green / Yellow / Red.

2. IF RED: Write a brief explanation and respond with JSON:
   {{"fit": "Red", "ai_notes": "...", "resume": "", "status": "AI Reviewed - Skip"}}

3. IF GREEN OR YELLOW:
   a. Select the appropriate resume variant based on the JD signals
   b. Optimize it for this role (rewrite bullets, adjust summary, mirror JD language)
   c. Never fabricate experience or invent metrics
   d. Respond with JSON:
   {{
     "fit": "Green" or "Yellow",
     "ai_notes": "FIT: ...\\nRESUME SELECTED: ...\\nREASON: ...\\nTOP STRENGTHS:\\n1. ...\\n2. ...\\n3. ...\\nGAPS:\\n1. ...\\nRECOMMENDATION: ...",
     "resume": "[full optimized resume text]",
     "status": "AI Reviewed"
   }}

Respond with valid JSON only. No markdown, no preamble.
"""


def review_job_with_claude(role_title: str, company: str, raw_jd: str) -> dict:
    """Call Claude API to review a single job. Returns parsed result dict."""
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": build_review_prompt(role_title, company, raw_jd),
            }
        ],
    )

    raw = message.content[0].text.strip()

    # Strip markdown code fences if present
    if raw.startswith("```"):
        lines = raw.split("\n")
        raw = "\n".join(lines[1:-1]) if lines[-1] == "```" else "\n".join(lines[1:])

    return json.loads(raw)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    # Validate environment
    missing = [v for v in ("NOTION_TOKEN", "NOTION_DB_ID", "ANTHROPIC_API_KEY") if not os.environ.get(v)]
    if missing:
        sys.exit(f"Missing required environment variables: {', '.join(missing)}")

    log.info(f"Starting job review scan {'(DRY RUN)' if DRY_RUN else ''}")

    # Fetch bookmarked jobs
    jobs = get_bookmarked_jobs()
    log.info(f"Found {len(jobs)} Bookmarked job(s)")

    if not jobs:
        log.info("Nothing to process. Exiting.")
        return

    results = {"green": [], "yellow": [], "red": [], "skipped": [], "errors": []}

    for job in jobs:
        page_id = job["id"]
        role_title = extract_text_property(job, "Role Title")
        company = extract_text_property(job, "Company")
        raw_jd = extract_text_property(job, "Raw JD")

        log.info(f"Processing: {role_title} @ {company}")

        # Skip if no JD
        if not raw_jd.strip():
            log.warning(f"  Skipping — Raw JD is empty")
            results["skipped"].append(f"{role_title} @ {company}")
            if not DRY_RUN:
                update_job_row(
                    page_id,
                    ai_notes="Raw JD not populated — add JD text to process this role",
                    resume="",
                    status="AI Reviewed - Skip",
                )
            continue

        if DRY_RUN:
            log.info(f"  DRY RUN — would send to Claude API")
            continue

        # Call Claude
        try:
            result = review_job_with_claude(role_title, company, raw_jd)
            fit = result.get("fit", "Unknown")
            ai_notes = result.get("ai_notes", "")
            resume = result.get("resume", "")
            status = result.get("status", "AI Reviewed")

            update_job_row(page_id, ai_notes, resume, status)
            log.info(f"  Result: {fit} → {status}")

            tier = fit.lower()
            if tier in results:
                results[tier].append(f"{role_title} @ {company}")
            else:
                results["skipped"].append(f"{role_title} @ {company}")

        except json.JSONDecodeError as e:
            log.error(f"  Failed to parse Claude response: {e}")
            results["errors"].append(f"{role_title} @ {company}")
        except Exception as e:
            log.error(f"  Error processing job: {e}")
            results["errors"].append(f"{role_title} @ {company}")

    # Summary
    log.info("=" * 50)
    log.info(f"SCAN COMPLETE — {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    log.info(f"  Green:   {len(results['green'])}")
    log.info(f"  Yellow:  {len(results['yellow'])}")
    log.info(f"  Red:     {len(results['red'])}")
    log.info(f"  Skipped: {len(results['skipped'])}")
    log.info(f"  Errors:  {len(results['errors'])}")

    if results["green"] or results["yellow"]:
        log.info("\nRecommended to apply:")
        for job in results["green"] + results["yellow"]:
            log.info(f"  ✓ {job}")

    if results["errors"]:
        log.warning("\nFailed (check logs above):")
        for job in results["errors"]:
            log.warning(f"  ✗ {job}")


if __name__ == "__main__":
    main()
