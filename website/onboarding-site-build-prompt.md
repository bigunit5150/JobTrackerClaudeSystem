# Claude Code Build Prompt: AI Job Search System — Onboarding Website

> **Where to use:** Paste this entire file into a Claude Code chat in VS Code,
> opened against the kssoftware.net GitHub Pages repository.
>
> **What it produces:** 4 new HTML pages in `/job-search-ai/` plus an update
> to `projects/index.html`.

---

## Your Mission

Add a 4-page onboarding section to the kssoftware.net GitHub Pages repository.
The section lives at `/job-search-ai/` and consists of one parent overview page
and three sequential setup sub-pages. This is a public-facing product page
for job seekers, not personal documentation.

**Do not start writing code until you have completed Step 1.**

---

## Step 1: Read These Files First (Required)

Read every file listed below before writing any HTML, CSS, or JS.

### Files to Read
```
css/style.css
js/main.js
index.html
projects/job-tracker.html
projects/index.html
```

### Confirm You Have Extracted
- [ ] All CSS custom properties from `:root` in `css/style.css`
- [ ] The exact nav HTML block (logo lockup, inline SVG, nav-links, mobile toggle)
- [ ] The exact `site-footer` HTML block
- [ ] The Google Fonts `<link>` and preconnect tags
- [ ] The scroll reveal pattern (`.reveal` / `.visible`) from `js/main.js`
- [ ] The sticky nav pattern (`.scrolled` on `#site-nav`) from `js/main.js`
- [ ] The mobile nav toggle pattern from `js/main.js`
- [ ] The existing `projects/` nav link structure (uses `../` relative paths)

Do not guess at any variable name, class name, or markup pattern.
Replicate everything from the actual source files.

---

## Step 2: Design System Rules (Non-Negotiable)

All four new pages must be visually indistinguishable from the existing site.

### CSS Variables (use these, do not hardcode hex values)
```
--bg: #0d1117
--bg-card: #161b22
--bg-subtle: #1c2333
--border: #21262d
--border-mid: #30363d
--border-light: #444c56
--amber: #e8a230
--amber-light: #f5b944
--amber-dim: rgba(232, 162, 48, 0.12)
--amber-glow: rgba(232, 162, 48, 0.05)
--text-1: #f0ede8
--text-2: #b0a99e
--text-3: #6e6860
--text-inv: #0d1117
--max-w: 1080px
--section-gap: 120px
--card-radius: 14px
--radius-sm: 8px
--font-display: 'Fraunces', Georgia, serif
--font-body: 'Plus Jakarta Sans', system-ui, sans-serif
```

### Typography Rules
- Headlines: Fraunces weight 300
- Italic amber accents in headlines: `<em style="font-style:italic; color:var(--amber)">word</em>`
- Body text: Plus Jakarta Sans weight 300 or 400
- Eyebrow labels: Plus Jakarta Sans weight 500, uppercase, letter-spacing, color `--amber`, ~12px

### Logo SVG (use exactly)
```html
<svg width="32" height="32" viewBox="0 0 36 36" fill="none" aria-hidden="true">
  <path d="M18 2L34 18L18 34L2 18Z" stroke="#e8a230" stroke-width="1.8" fill="none"/>
  <path d="M13 22 Q18 11 23 22" stroke="#e8a230" stroke-width="1.6" fill="none" stroke-linecap="round"/>
  <path d="M10 25 Q18 6 26 25" stroke="#e8a230" stroke-width="1" fill="none" stroke-linecap="round" opacity="0.45"/>
  <circle cx="18" cy="22.5" r="2" fill="#e8a230"/>
</svg>
```

### JavaScript
Do NOT create a new JS file. All four pages link to `../js/main.js`.

### Components to Reuse
- Nav, footer, `.reveal`, `.card`, `.eyebrow`, `.section-headline`, `.btn`,
  `.badge`, `.divider`, `.grid-2`, `.grid-3`, `.step-number`, `.container`
- All from existing pages — copy markup exactly, adjust `../` paths

---

## Step 3: File Structure to Create

```
job-search-ai/
  index.html          Parent overview page
  extension.html      Step 1 — Chrome Extension setup
  notion-setup.html   Step 2 — Notion workspace + database setup
  claude-setup.html   Step 3 — Claude account, project + onboarding prompt
```

All pages use `../css/style.css` and `../js/main.js`.
Page-specific styles go in a `<style>` block in `<head>`, using CSS variables only.

---

## Step 4: Nav Structure for New Pages

```
[Logo] KSSoftware    → ../index.html
How It Works         → #how-it-works
Step 1: Extension    → extension.html
Step 2: Notion       → notion-setup.html
Step 3: Claude       → claude-setup.html
Get Started          → extension.html  (btn btn-primary)
```

---

## Step 5: Page Specifications

---

### PAGE 1: job-search-ai/index.html

**Hero**
- Eyebrow: `AI-POWERED JOB SEARCH`
- H1: `Your job search,` / `on <em>autopilot</em>.`
- Sub: "Save job postings, get AI-optimized resumes, and walk into every
  interview prepared. Three tools that work together inside Claude and Notion."
- CTAs: `Get Started →` (btn-primary → extension.html),
  `See How It Works` (btn-ghost → #how-it-works)
- Hero graphic: concentric diamond SVG from index.html, opacity 0.4, right side

**Stats Row** (`.stats-row`)
- `3` / Tools in the system
- `~20 min` / Setup time
- `0` / Resumes written by hand

**Workflow Diagram** (`id="how-it-works"`)
Three phase nodes connected by arrows. Pure HTML/CSS — no libraries.
- Node style: `--bg-card` fill, `--border-mid` stroke, 4px amber left border
- Arrows: thin amber lines, opacity 0.6
- Phase 1: "📌 Save" / "Bookmark jobs in Notion via Chrome Extension"
- Phase 2: "🤖 Review" / "Claude evaluates fit + optimizes your resume"
- Phase 3: "🎯 Prepare" / "Interview cheat sheets + mock interviews"
- Labels below each: "Step 1", "Step 2", "Step 3" in `--text-3`
- Mobile: stack vertically with downward arrows

**Three-Phase Cards** (`.grid-3`)
- Phase 1: document icon, "Save Jobs Instantly", badge STEP 1
- Phase 2: star icon, "AI-Optimized Resumes", badge STEP 2
- Phase 3: calendar-check icon, "Interview-Ready in Minutes", badge STEP 3
(Copy icons from existing pages)

**Prerequisites Callout** (`.callout-bar`)
Checklist with amber SVG checkmarks:
- Free Notion account (notion.so)
- Google Chrome browser
- Claude account — Free works for setup; Pro recommended for daily use
- Your existing resumes (Word, PDF, or text)

**Setup Step Nav** (`.grid-3`)
Three cards linking to sub-pages. Step number + title + description + arrow link.
Amber bottom border on hover.

---

### PAGE 2: job-search-ai/extension.html

**Hero**
- Eyebrow: `STEP 1 OF 3`
- H1: `Install the` / `Chrome <em>Extension</em>`
- CTA: `Install from Chrome Web Store →` (btn-primary)
  `<!-- TODO: add CWS URL -->`

**Install Steps** (`.steps-grid` + `.step-number` + `.card`)
1. Install from Chrome Web Store
2. Pin the extension to your toolbar
3. Connect your Notion account (with note: complete Step 2 first)
4. Save your first job

**Configuration Reference** (`.grid-2`)
Two cards: Notion Integration Token + Job Tracker Database ID.
Each with monospace code block showing example format:
```css
font-family: 'Courier New', monospace;
background: var(--bg);
border: 1px solid var(--border-mid);
border-radius: var(--radius-sm);
padding: 8px 12px;
color: var(--amber-light);
font-size: 13px;
```

**Supported Job Boards** (`.grid-3` badge-style cards)
LinkedIn, Greenhouse, Lever, Workday, Indeed, Glassdoor, "Any career page"

**Bottom Nav**
← Overview (`index.html`) | Step 2 — Set Up Notion → (`notion-setup.html`, btn-primary)

---

### PAGE 3: job-search-ai/notion-setup.html

**Hero**
- Eyebrow: `STEP 2 OF 3`
- H1: `Set Up Your` / `Notion <em>Workspace</em>`

**Prerequisites callout** (amber left-border card):
"Have a Notion account and the Chrome extension installed before starting."

**Section 1: Create the Three Databases**
Three `<details>` / `<summary>` collapsible cards — one per database.

Style `<details>` as cards:
```css
details { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--card-radius); margin-bottom: 12px; overflow: hidden; }
details[open] { border-color: var(--border-mid); }
summary { padding: 20px 24px; cursor: pointer; font-family: var(--font-body); font-weight: 500; color: var(--text-1); list-style: none; display: flex; justify-content: space-between; align-items: center; }
summary::after { content: '+'; color: var(--amber); font-size: 20px; font-weight: 300; }
details[open] summary::after { content: '−'; }
.details-body { padding: 0 24px 24px; color: var(--text-2); font-size: 15px; line-height: 1.7; }
```

Each card contains:
- One-sentence purpose
- Numbered creation steps
- Two-column property table (name + type)
- Select field option values

Database 1: Job Tracker (Status options: Bookmarked, AI Reviewed, AI Reviewed - Skip,
Applying, Applied, Interviewing, Offer, Closed)

Database 2: Resume Repository (Category: Director, Senior Manager, VP,
AI/Technical Consulting, Other. Active: Yes/No)

Database 3: Interview Prep Hub (Status: Active Prep, Interview Scheduled,
Interview Complete, Offer, Closed. Interview Round: Phone Screen, Recruiter Screen,
Hiring Manager, Panel, Final Round, Offer Stage)

**Section 2: Connect Claude to Notion**
Five vertical step cards with amber dotted connector line:
```css
.steps-connector { position: relative; padding-left: 48px; }
.steps-connector::before { content: ''; position: absolute; left: 19px; top: 32px; bottom: 32px; width: 1px; background: repeating-linear-gradient(to bottom, var(--amber) 0px, var(--amber) 4px, transparent 4px, transparent 10px); opacity: 0.3; }
```
Steps: Open Claude Settings → Integrations → Connect Notion →
Authorize workspace → Verify connected

**Section 3: Find Your Database IDs**
`.grid-2` cards: Integration Token (with steps) + Database ID (with steps).
Amber warning callout: keep token private.

**Bottom Nav**
← Step 1 — Extension | Step 3 — Configure Claude → (btn-primary)

---

### PAGE 4: job-search-ai/claude-setup.html

**Hero**
- Eyebrow: `STEP 3 OF 3`
- H1: `Configure` / `<em>Claude</em> for Your Search`

**Why a Claude Project** (`.callout-bar`):
Explain persistent project context — all three phases live in one project.

**Section 1: Create Your Claude Project**
Four step cards:
1. Go to claude.ai → Projects → New Project
2. Verify Notion is connected in the project
3. Upload resume files (Word, PDF, or text)
4. Run the onboarding prompt below

**Onboarding Prompt Container**
HTML structure:
```html
<div class="prompt-container">
  <div class="prompt-header">
    <span class="prompt-label">ONBOARDING PROMPT — PASTE INTO CLAUDE</span>
    <button class="copy-btn" onclick="copyPrompt()" id="copy-btn" aria-label="Copy prompt to clipboard">
      [copy SVG icon] Copy Prompt
    </button>
  </div>
  <pre class="prompt-body" id="onboarding-prompt">FULL PROMPT TEXT HERE</pre>
</div>
```

CSS:
```css
.prompt-container { background: var(--bg); border: 1px solid var(--border-mid); border-radius: var(--card-radius); overflow: hidden; margin: 32px 0; }
.prompt-header { display: flex; justify-content: space-between; align-items: center; padding: 12px 20px; background: var(--bg-subtle); border-bottom: 1px solid var(--border); }
.prompt-label { font-family: var(--font-body); font-size: 11px; font-weight: 500; letter-spacing: 0.08em; color: var(--amber); text-transform: uppercase; }
.copy-btn { display: flex; align-items: center; gap: 6px; background: transparent; border: 1px solid var(--border-mid); border-radius: var(--radius-sm); color: var(--text-2); font-family: var(--font-body); font-size: 13px; padding: 6px 12px; cursor: pointer; transition: color 0.2s, border-color 0.2s; }
.copy-btn:hover { color: var(--amber); border-color: var(--amber); }
.copy-btn.copied { color: #4caf50; border-color: #4caf50; }
.prompt-body { padding: 24px; font-family: 'Courier New', Courier, monospace; font-size: 13px; line-height: 1.7; color: var(--text-2); white-space: pre-wrap; word-break: break-word; max-height: 480px; overflow-y: auto; margin: 0; scrollbar-width: thin; scrollbar-color: var(--border-mid) transparent; }
```

Copy button JS (inline `<script>` at bottom of page):
```javascript
function copyPrompt() {
  const text = document.getElementById('onboarding-prompt').textContent;
  navigator.clipboard.writeText(text).then(() => {
    const btn = document.getElementById('copy-btn');
    btn.classList.add('copied');
    btn.innerHTML = '[checkmark SVG] Copied!';
    setTimeout(() => {
      btn.classList.remove('copied');
      btn.innerHTML = '[copy SVG] Copy Prompt';
    }, 2500);
  });
}
```

**Full prompt text to embed in `#onboarding-prompt`:**
(Copy verbatim from `new-user-onboarding.md` — the full prompt
text inside the ``` code fence. Do not summarize or truncate.)

**Section 2: What Happens Next** (`.grid-3`)
- "Daily Use" — save jobs, say "Review bookmarked jobs"
- "Before Each Interview" — new chat per opportunity, run init prompt
- "Resume Changes" — update Notion row, tell Claude to reload

**Completion Callout** (`.callout-bar`, `--amber-dim` background):
"You're all set. Questions? keith@kssoftware.net"

**Bottom Nav**
← Step 2 — Notion Setup | View your Job Tracker in Notion → (btn-primary, new tab)

---

## Step 6: Update projects/index.html

Add a card for "AI Job Search System":
- Badge: `AI SYSTEM`
- Title: AI Job Search System
- Body: "Three-tool workflow: Chrome extension saves postings, Claude optimizes
  resumes and evaluates fit, and interview prep cheat sheets are generated automatically."
- Link: "View Setup Guide →" → `job-search-ai/index.html`

Use exact card markup from existing project cards.

---

## Step 7: Quality Checklist

### Structural
- [ ] All 4 pages exist in `job-search-ai/`
- [ ] All asset paths use `../` prefix
- [ ] `projects/index.html` updated with new card

### Design Consistency
- [ ] No hardcoded hex values — CSS variables only
- [ ] Same Google Fonts URL as existing pages
- [ ] Logo SVG matches exactly
- [ ] Nav and footer HTML match existing pages exactly
- [ ] `.reveal` on all animatable sections

### Functionality
- [ ] All internal links work
- [ ] Chrome Web Store link has `<!-- TODO: add CWS URL -->` placeholder
- [ ] Copy-to-clipboard works with "Copied!" confirmation state
- [ ] `<details>` expand/collapse works without JS
- [ ] Mobile nav works (inherited from main.js)
- [ ] Smooth scroll works on "See How It Works"
- [ ] Onboarding prompt text is complete and untruncated

### Accessibility
- [ ] All SVGs have `aria-hidden="true"` or descriptive `aria-label`
- [ ] Copy button has `aria-label`
- [ ] WCAG AA color contrast on all text

---

## Commit Message

```
feat: add AI job search system onboarding pages

- Add job-search-ai/ section with 4 pages (overview + 3 setup steps)
- Covers Chrome extension install, Notion database setup, Claude configuration
- Includes copy-to-clipboard onboarding prompt on claude-setup.html
- Updates projects/index.html with new AI Job Search System card
```
