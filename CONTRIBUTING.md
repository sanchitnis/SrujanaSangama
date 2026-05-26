# Contributing to SrujanaSangama

First, thank you. This marketplace exists to serve the entire REVA University community — students, faculty, and administrators — and every improvement makes a genuine difference to the people who use it.

This guide is for three types of contributors:
- [Students and faculty](#for-students-and-faculty) — no technical knowledge needed
- [Git contributors (developers and faculty)](#for-contributors-who-know-git)
- [Institution administrators — setting up the marketplace](#for-institutions-setting-up-the-marketplace)

---

## Before You Contribute — Read This First

### The spirit of this marketplace

SrujanaSangama is not a generic AI toolbox with REVA branding. Every plugin and workflow reflects a specific commitment: **AI accelerates and scaffolds; humans deliberate, decide, and do the work.** The Socratic no-rewrite rules in the law plugin, the ADDIE-aligned course design in the teaching plugin, the Hitaishin wellbeing principles — these are deliberate design choices rooted in REVA's vision, not arbitrary defaults.

**Before suggesting any change, ask:** Does this help REVA's people — students, faculty, or administrators — do better work, think more clearly, or learn more deeply? Or does it make the AI do more of the work for them? Both have their place, but they are different products.

### Ground rules

1. **Domain accuracy matters more than technical elegance.** A beautifully structured workflow that cites a wrong BCI rule, a wrong NBA criterion, or a wrong Bloom's level does harm. Accuracy over aesthetics, always.

2. **The human-in-the-loop principle is non-negotiable.** No plugin should make final decisions for students, faculty, or administrators. AI drafts, scaffolds, and signals. Humans decide and approve.

3. **Cite your sources.** If you update a legal provision, a regulatory requirement, or an institutional policy — say where you got it. Information without provenance is not trustworthy in an academic context.

4. **Less is more.** The temptation is to add more features, more workflows, more questions. Resist. A smaller plugin that is deeply used beats a comprehensive one that overwhelms the user.

5. **Credit sources.** If you adapt from a published framework, a BCI circular, an NBA criterion document, or an Anthropic plugin — say so. Intellectual honesty is a REVA universal value.

---

## For Students and Faculty

You don't need to know how to code or use Git to contribute meaningfully.

### Ways to contribute

**1. Report an error in any plugin**

If something is factually wrong — a case citation, a statutory provision, an AIBE question, an NBA criterion, a Bloom's taxonomy level — tell us.

Go to: [GitHub Issues](https://github.com/sanchitnis/SrujanaSangama/issues) → Click **New Issue** → Choose the appropriate label:

| Label | Use for |
|---|---|
| `legal-accuracy` | Wrong case, provision, or AIBE content in `law-student-reva` |
| `pedagogy-accuracy` | Wrong Bloom's level, CO-PO logic, or NBA criterion in teaching/admin plugins |
| `content-gap` | An important topic, case, or feature that's missing |
| `user-experience` | Something confusing, unhelpful, or that didn't work the way you expected |
| `question` | You're not sure — just ask |

In your issue, describe:
- Which plugin and which command (`/socratic-drill`, `/course-check`, etc.)
- What it currently says or does
- What it should say or do instead
- Your source, if you have one

**2. Share your experience**

The most valuable contributions from users are specific observations:
- "This workflow worked exactly as I hoped — here's why"
- "This AIBE question had the wrong answer — the correct provision is X"
- "The bench simulation was too gentle / too aggressive for our moot court"
- "As an LL.M. student the research mode didn't behave how I expected"
- "The CO-PO audit caught something my department had missed for two years"
- "The GPS planning workflow doesn't match how REVA's semester structure actually works"

Open an Issue with label `user-experience`. No technical detail needed — just describe what happened and what would have been more useful.

**3. Volunteer as a domain reviewer**

If you have expertise in a specific area — Indian law, NBA/NAAC compliance, instructional design, student wellbeing — you can volunteer to review contributions in that area before they are merged.

Open an Issue with label `reviewer-volunteer` and mention your expertise. Reviewers are the primary quality gate for domain accuracy.

---

## For Contributors Who Know Git

### Setting up your workspace

**Step 1 — Fork the repository**

Go to [github.com/sanchitnis/SrujanaSangama](https://github.com/sanchitnis/SrujanaSangama) and click **Fork** (top right). This creates your own copy to work in safely.

**Step 2 — Clone your fork to your computer**

Open a terminal (Command Prompt, PowerShell, or Terminal) and run:

```bash
git clone https://github.com/YOUR-USERNAME/SrujanaSangama.git
cd SrujanaSangama
```

Replace `YOUR-USERNAME` with your GitHub username.

**Step 3 — Create a branch for your change**

Always work on a branch — never directly on `main`. Use a prefix that identifies which plugin or area you're working on:

```bash
git checkout -b law/fix-bns-transition-flags
git checkout -b teach/improve-irac-session-workflow
git checkout -b admin/update-nba-criteria-checklist
git checkout -b kaizen/gps-semester-alignment
git checkout -b docs/update-contributing-guide
```

Branch prefixes:
| Prefix | Plugin / area |
|---|---|
| `law/` | `law-student-reva` |
| `teach/` | `teaching-learning-reva` |
| `research/` | `research-reva` |
| `admin/` | `academic-admin-reva` |
| `consult/` | `consulting-product-reva` |
| `kaizen/` | `kaizen-wellbeing-reva` |
| `docs/` | Documentation, CONTRIBUTING.md, README files |
| `marketplace/` | `.antigravity-marketplace/marketplace.json` or new plugins |

**Step 4 — Make your changes**

Plugin files you'll most commonly edit:

```
plugins/<plugin-name>/
├── workflows/*.md     ← Workflow logic, questions, feedback formats
├── rules/*.md         ← Core guardrails (requires extra care — see below)
├── README.md          ← User documentation for this plugin
└── package.json       ← Only if adding a new slash command
```

Shared files:
```
CONTRIBUTING.md                                ← This file
README.md                                      ← Marketplace overview
.antigravity-marketplace/marketplace.json      ← Plugin registry
```

**Step 5 — Test your change**

Before submitting, test that your change works in `agy`:

```bash
agy marketplace add local .
```

Then trigger the workflow you changed and verify the output behaves as expected.

**Step 6 — Commit your changes**

```bash
git add .
git commit -m "law: fix BNS S.101 flag in AIBE criminal law MCQs"
```

Commit message format: `[prefix]: [brief description in plain English]`

Examples:
- `law: correct ratio for Kesavananda Bharati case brief`
- `teach: add HOTS check to assessment-check workflow`
- `admin: update NBA criterion 2.1 checklist`
- `docs: expand marketplace setup for Windows UNC paths`

**Step 7 — Push to your fork**

```bash
git push origin your-branch-name
```

**Step 8 — Open a Pull Request**

Go to your fork on GitHub. You'll see a **"Compare & pull request"** button. Click it.

In your PR description:
- What you changed and why
- Which plugin(s) are affected
- What you tested
- Any sources you relied on (links preferred)

Add the appropriate label from the issue labels listed above.

---

### Pull Request Checklist

Before you submit, check:

- [ ] Content is accurate and sourced (link to primary source where possible)
- [ ] Language is accessible to the target user (a 2nd-year BA LLB student for law; a new faculty member for teaching plugins)
- [ ] No workflow now produces a completed draft, model answer, or decision on behalf of the user — the human-in-the-loop principle is intact
- [ ] For `law-student-reva`: no output is missing the `STUDY NOTES — NOT LEGAL ADVICE` label
- [ ] For `law-student-reva`: BNS/BNSS/BSA transition is flagged wherever IPC/CrPC/IEA is discussed (effective 1 July 2024)
- [ ] For `law-student-reva`: all case citations from model knowledge carry `[model knowledge — verify on Indian Kanoon / SCC Online]`
- [ ] Change tested in `agy`, not just reviewed as text
- [ ] Commit message follows the format above

### Guardrails Changes — Special Review Process

Any change to a `rules/*.md` file in any plugin goes through a two-reviewer process before merging. These files are the safety nets that protect users — students from being misled about legal advice, faculty from incorrect regulatory guidance, everyone from AI overreach. Do not weaken them. If you think a guardrail is wrong or too strict, open an Issue and make the case — the community will review it.

---

## For Institutions Setting Up the Marketplace

This section explains how to set up the SrujanaSangama marketplace so that students and faculty at your institution can install any plugin with a single command.

### How the marketplace works

The file `.antigravity-marketplace/marketplace.json` is a **central index** of all available plugins. When a user runs:

```bash
agy marketplace install reva.law-student-reva
```

...the `agy` tool reads this index, finds the plugin's folder path, and installs it automatically. Users never need to know where files live.

### Option A — Use the hosted SrujanaSangama marketplace (simplest)

If your institution has internet access, register the marketplace once on each workstation:

```bash
agy marketplace add srujanasangama https://raw.githubusercontent.com/sanchitnis/SrujanaSangama/main/.antigravity-marketplace/marketplace.json
```

After this, anyone on that workstation can install any plugin:

```bash
# Install a specific plugin
agy marketplace install reva.law-student-reva
agy marketplace install reva.teaching-learning-reva

# See all available plugins
agy marketplace plugins srujanasangama
```

### Option B — Set up a campus network mirror (recommended for institutions)

If your institution has a shared network drive or internal server, host the marketplace locally so it works without internet dependency.

**Step 1 — Clone the repository to your server:**

```bash
git clone https://github.com/sanchitnis/SrujanaSangama.git /path/to/server/SrujanaSangama
```

**Step 2 — Register the local path on each workstation:**

```bash
# On Linux / Mac
agy marketplace add srujanasangama /path/to/server/SrujanaSangama

# On Windows (mapped drive)
agy marketplace add srujanasangama Z:\SrujanaSangama

# On Windows (UNC path)
agy marketplace add srujanasangama \\server-name\shared\SrujanaSangama
```

**Step 3 — Install plugins on each workstation:**

```bash
agy marketplace install reva.law-student-reva
```

**Step 4 — Keep the server copy up to date (for IT administrators):**

Run this on the server periodically (or set up a scheduled task / cron job):

```bash
cd /path/to/server/SrujanaSangama
git pull origin main
```

Students and faculty get the latest plugin versions automatically — they don't need to do anything.

### Option C — Install a single plugin without setting up the full marketplace

If you only want one plugin (e.g., `law-student-reva`) and don't need the rest:

```bash
# Download only the plugin folder using sparse checkout
git clone --depth 1 --filter=blob:none --sparse https://github.com/sanchitnis/SrujanaSangama.git
cd SrujanaSangama
git sparse-checkout set plugins/law-student-reva .antigravity-marketplace

# Register it locally
agy marketplace add local .
agy marketplace install reva.law-student-reva
```

### Verifying your marketplace setup

```bash
# List all registered marketplaces
agy marketplace list

# List available plugins in the SrujanaSangama marketplace
agy marketplace plugins srujanasangama

# Check which plugins are installed
agy plugins list
```

### Adding a new plugin to the marketplace

If you've built a new plugin and want to make it installable through the marketplace:

**Step 1 — Create your plugin folder under `plugins/`:**

```
plugins/
└── your-plugin-name/
    ├── plugin.json       ← required
    ├── mcp.json          ← required
    ├── package.json      ← required
    ├── README.md         ← required (non-technical user guide)
    ├── rules/            ← at least one guardrails file
    └── workflows/        ← at least one workflow
```

**Step 2 — Add an entry to `.antigravity-marketplace/marketplace.json`:**

```json
{
  "id": "reva.your-plugin-name",
  "name": "Human-readable plugin name",
  "version": "1.0.0",
  "path": "plugins/your-plugin-name",
  "description": "One sentence: what it does and who it's for.",
  "standalone": true,
  "tags": ["relevant", "tags"]
}
```

**Step 3 — Open a Pull Request** (see the Git section above). The marketplace entry will not be merged until the plugin passes review.

---

## Questions?

Open a GitHub Issue with label `question`. There are no wrong questions — the only bad outcome is a problem that goes unreported and unfixed.

For urgent issues affecting live use by students or faculty, email the maintainers directly — see the repository's GitHub profile for contact details.
