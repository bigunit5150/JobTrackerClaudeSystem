# Phase 1: Chrome Extension Setup

## Overview

The Job Post Tracker Chrome extension is the data capture layer of the system.
When you find a job posting you want to save, clicking the extension icon
captures the full job description and saves it directly to your Notion Job
Tracker database — no copy-pasting required.

---

## Installation

1. Install [Job Post Tracker from the Chrome Web Store](https://chromewebstore.google.com/detail/ponffclikgodccpghpammcpjpjeojopj?utm_source=item-share-cb)
2. Click **Add to Chrome** and confirm the installation prompt
3. Click the puzzle piece icon in your Chrome toolbar
4. Find **Job Post Tracker** and click the pin icon to keep it visible

---

## Configuration

The extension requires two values from your Notion workspace.

### Notion Integration Token

1. Go to [notion.so/profile/integrations](https://notion.so/profile/integrations)
2. Click **New integration**
3. Name it (e.g. "Job Search AI") and select your workspace
4. Copy the **Internal Integration Token** — it starts with `secret_`
5. Paste it into the extension popup under "Notion Token"

**Keep this token private.** It grants write access to your Notion workspace.

### Job Tracker Database ID

1. Open your **Job Tracker** database in Notion (full page view)
2. Copy the URL from your browser address bar
3. The database ID is the 32-character string before the `?v=` parameter

Example URL:
```
https://www.notion.so/320037c8790b80049498d26d7d85322c?v=...
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       This is your database ID
```

4. Paste it into the extension popup under "Database ID"

---

## Granting Database Access to Your Integration

After creating your integration, you must explicitly grant it access to
your Job Tracker database:

1. Open your **Job Tracker** database in Notion
2. Click the `...` menu in the top-right corner
3. Select **Connections**
4. Find your integration name and click **Connect**

Without this step, the extension will get a permissions error when trying
to save jobs.

---

## Saving a Job

1. Navigate to any job posting (LinkedIn, Greenhouse, Lever, Workday, etc.)
2. Click the **Job Post Tracker** icon in your Chrome toolbar
3. The extension captures the page title, URL, and job description
4. Click **Save to Notion**
5. The row appears in your Job Tracker with Status: **Bookmarked**

The `Raw JD` field is populated automatically. This is what Claude reads
during Phase 2 review — the richer the JD text, the better Claude's
assessment.

---

## Supported Sites

The extension works on any web page but is optimized for:
- LinkedIn Jobs
- Greenhouse-hosted job pages
- Lever-hosted job pages
- Workday job listings
- Indeed
- Glassdoor
- Company career pages

For sites where auto-extraction is imperfect, you can edit the Raw JD
field in Notion directly before triggering the AI review.

---

## Troubleshooting

**"Could not connect to Notion"**
- Verify your Integration Token is correct (starts with `secret_`)
- Confirm you've granted the integration access to the database (see above)

**"Database not found"**
- Verify your Database ID is the 32-character string from the URL
- Do not include the `?v=` parameter or anything after it

**Raw JD is empty or incomplete**
- Some job boards load content dynamically — scroll to the bottom of the
  job posting before clicking the extension to ensure the full page loads
- Alternatively, paste the JD text directly into the Raw JD field in Notion

---

## GitHub Repository

Extension source code: [bigunit5150/JobTrackerChromeExtension](https://github.com/bigunit5150/JobTrackerChromeExtension)
