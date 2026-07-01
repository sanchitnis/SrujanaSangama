# REVA Law Student Study Companion

> **Your AI study partner for REVA Law School — Socratic drilling, AIBE prep, moot court training, and more.**
> **It never writes the answer for you. That's the point.**

---

## What Is This?

This is an AI plugin for **REVA University Law School students** — B.A. LL.B. (Hons.), BBA LL.B. (Hons.), LL.M., and Ph.D. in Legal Studies.

Think of it as a tireless study partner who:
- **Asks you questions** instead of giving you answers (Socratic method)
- **Drills you on cases** and pushes back when your reasoning is sloppy
- **Grades your IRAC answers** and tracks where you keep making the same mistake
- **Preps you for AIBE** — the All India Bar Examination — with MCQs, timed simulations, and subject analysis
- **Simulates a moot court bench** that asks hard questions about your arguments
- **Reviews your legal drafts** (pleadings, petitions, notices) for structural gaps — without rewriting them

**What it doesn't do:** Write your essay, your brief, your memorial, or your IRAC answer for you. If you want that, use a general AI chatbot. This plugin is for the *struggle* — because that's how you actually learn law.

> All outputs from this plugin are labeled **STUDY NOTES — NOT LEGAL ADVICE**. This is a study tool, not a legal consultation service.

---

## Who Is This For?

| Programme | Works for you? |
|---|---|
| B.A. LL.B. (Hons.) | ✅ Yes — all features |
| BBA LL.B. (Hons.) | ✅ Yes — all features |
| LL.M. | ✅ Yes — research-mode adjustments for academic writing |
| Ph.D. in Legal Studies | ✅ Yes — research and thesis writing focus |

---

## How to Install

You don't need to be technical. Follow these steps exactly.

### Step 1 — Check that you have the `agy` tool

Open a terminal (Command Prompt or PowerShell on Windows, Terminal on Mac) and type:

```
agy --version
```

If you see a version number, you're ready. If you see an error, ask your lab instructor or IT support to install **Google Antigravity CLI** (`agy`) on your computer.

### Step 2 — Get the plugin files

You have two options:

**Option A — If your institution has set up the REVA Marketplace (recommended):**

```
agy marketplace install reva.law-student-reva
```

That's it. The plugin installs automatically.

**Option B — Manual install (if marketplace isn't set up yet):**

1. Download or clone this repository to your computer.
   - If you know Git: `git clone https://github.com/sanchitnis/SrujanaSangama.git`
   - If you don't know Git: Ask a classmate or lab instructor to do this step for you, or download the ZIP file from GitHub and extract it.

2. Navigate to the plugin folder — it's at `plugins/law-student-reva/` inside the downloaded folder.

3. Tell `agy` where to find it:
   ```
   agy marketplace add local path/to/SrujanaSangama
   ```
   Replace `path/to/SrujanaSangama` with the actual location on your computer.

### Step 3 — Verify installation

```
agy plugins list
```

You should see `reva.law-student-reva` in the list.

---

## First Time Setup — Do This Before Anything Else

Once installed, run the setup interview. It takes 2–15 minutes and makes every other command smarter and more specific to you.

```
/cold-start-interview
```

The setup asks you:
- Which programme and year you're in
- Which subjects you're studying this semester
- Your AIBE target date (if you're preparing for AIBE)
- Whether you prefer to be **drilled** (Socratic) or **explained to** first
- Which subjects are strong/weak/terrifying
- Your upcoming exam and moot court dates

> **You can do a quick 2-minute version** (just the basics) and come back for the full setup later. Just answer "quick" when it asks.

---

## Commands — What You Can Do

Every command starts with `/`. Type it in the `agy` chat window.

| Command | What it does |
|---|---|
| `/cold-start-interview` | Set up your profile — do this first |
| `/socratic-drill [topic]` | Get drilled on a legal topic. It asks, you answer. |
| `/case-brief [case name]` | Brief a case in IRAC, FILAC, or Indian format |
| `/outline-builder [subject]` | Build a subject outline — you fill it in, not the AI |
| `/aibe-prep` | AIBE MCQs, timed simulation, subject analysis |
| `/flashcards [subject]` | Generate and drill flashcards (Leitner method) |
| `/study-plan` | Build or view your semester / AIBE study plan |
| `/session [subject] [n]` | Focused N-question session; updates your plan |
| `/irac-practice` | Paste your IRAC answer — get it graded |
| `/moot-court-trainer` | Bench simulation, memorial review, precedent drill |
| `/legal-writing` | Paste your draft — get structural feedback |
| `/exam-forecast [subject]` | Forecast what's likely on your next exam |

---

## Detailed Command Guide

### `/socratic-drill [topic]`

The AI asks you a question about a legal topic. You answer. It tells you what's right, what's weak, and what you missed — then asks a follow-up.

**Example:**
```
/socratic-drill Right to Privacy
```
> "A government agency collects biometric data from citizens without consent and without statutory backing. A citizen challenges this before the Supreme Court. What constitutional provisions are in play, and what is the first argument you'd frame?"

It won't give you the answer. That's deliberate.

---

### `/aibe-prep`

Three modes:

```
/aibe-prep Constitutional Law --mcq
```
→ Generates 10 AIBE-pattern MCQs on Constitutional Law. Answer them, then get explanations.

```
/aibe-prep --timed
```
→ Simulates a full 100-question AIBE session. 3 hours 30 minutes. No explanations during the test — only after.

```
/aibe-prep --analysis
```
→ After a session, gives you a subject-wise breakdown: which of the 45 AIBE subjects you're strong in, which are critical gaps, what to focus on next.

> **Important:** AIBE now tests BNS, BNSS, and BSA — not the old IPC, CrPC, and Evidence Act. The plugin flags these transitions so you're not caught out.

---

### `/moot-court-trainer`

Four modes — pick what you need:

```
/moot-court-trainer --memorial
```
→ Paste your written memorial. Get structural feedback on every section — issues, arguments, prayer, citations. **It will not rewrite it.** You revise, come back, repeat.

```
/moot-court-trainer --bench
```
→ The AI becomes a 3-judge bench. You argue your side. The bench interrupts, challenges your ratio, asks you to distinguish cases, and doesn't accept vague submissions. Uncomfortable on purpose.

```
/moot-court-trainer --opposing
```
→ The AI argues the other side. You rebut. Good preparation for when you don't know what your opponent will say.

```
/moot-court-trainer --precedent
```
→ Rapid-fire: the AI names a case, you give the ratio and citation from memory. No notes. Your score tells you which cases you actually know vs. which ones you think you know.

---

### `/irac-practice`

Type `/irac-practice`, then paste your IRAC or FILAC answer to any problem question.

The plugin grades you on:
- Did you identify the right issue(s)?
- Is your rule statement accurate and cited?
- Did you actually apply the rule to the facts, or just restate them?
- Does your conclusion answer the question?

Each element is scored 1–5. After a few sessions, it tracks your patterns — "you consistently miss secondary issues" or "your application section is mechanical."

**It will not rewrite your answer.** When you ask it to, it will explain why it won't — and offer more targeted feedback instead.

---

### `/legal-writing`

Type `/legal-writing`, then paste your draft — plaint, writ petition, legal notice, affidavit, PIL, vakalatnama, written statement, or academic memo (for LL.M./Ph.D.).

The plugin checks it against the mandatory requirements for that type of document (e.g., Order VII Rule 1 CPC for a plaint) and gives you a structural quality assessment.

**Strictest no-rewrite rule in the plugin.** It identifies what's wrong and why. You fix it.

---

## Frequently Asked Questions

**Q: Can I ask it to just give me the answer to my assignment?**
A: No. That's not what this plugin is for. If you need a model answer, use a general AI chatbot. This plugin makes you think. The discomfort is intentional.

**Q: Will it work for my LLM dissertation?**
A: Yes — when the plugin detects you're an LL.M. or Ph.D. student, it shifts to research mode. `/legal-writing` shifts to academic memo feedback. `/socratic-drill` goes deeper into doctrinal analysis and critique.

**Q: Does it know about the new BNS/BNSS/BSA laws?**
A: Yes. It flags everywhere that IPC/CrPC/Evidence Act have been replaced by BNS/BNSS/BSA (effective 1 July 2024) and notes the transition. It also flags which code AIBE currently tests — verify with the BCI website since AIBE syllabus updates can lag behind legislative changes.

**Q: Are case citations reliable?**
A: No citation from this plugin should be used without verification. Every case cited from AI knowledge is tagged `[model knowledge — verify on Indian Kanoon / SCC Online]`. Always cross-check before using a citation in an exam answer, memorial, or submission.

**Q: I pasted a real legal problem from my family's case. What happens?**
A: The plugin will pause and redirect you to speak with a practicing advocate or the REVA Legal Aid Clinic. This plugin is for studying, not for handling real matters.

**Q: Can I use the plugin's outputs in my graded assignments?**
A: Check REVA's academic integrity policy first. The plugin always labels its outputs as AI-assisted study material. Never submit something as your own work if it was produced by AI without disclosing that.

---

## What "STUDY NOTES — NOT LEGAL ADVICE" Means

Every output from this plugin carries this label. It means:
- This is educational content to help you learn law, not professional legal advice.
- Do not rely on it for real legal situations involving yourself, your family, or a client.
- For real legal problems, consult a practicing advocate or legal aid service.

---

## Getting Help

If something isn't working:
1. Run `/cold-start-interview` again — many issues are resolved by a complete profile.
2. Ask a classmate or your faculty advisor.
3. Open an issue on GitHub — see [CONTRIBUTING.md](CONTRIBUTING.md) for how.

---

## Acknowledgements

This plugin is adapted for REVA University from the [claude-for-legal law-student plugin](https://github.com/anthropics/claude-for-legal/tree/main/law-student) by Anthropic, which pioneered the "learning mode, not answer mode" philosophy for legal education AI tools. The core pedagogical principle — that AI should scaffold your thinking, not replace it — is theirs. The Indian law adaptation, AIBE first-class features, and Moot Court Trainer are built for REVA Law School.
