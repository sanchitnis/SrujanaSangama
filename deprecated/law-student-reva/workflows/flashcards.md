# /flashcards [subject] [--generate | --drill | --session n | --export]

**Usage:**
- `/flashcards Contract Law --generate` — generate flashcards for a subject
- `/flashcards Contract Law --drill` — drill existing flashcards (Leitner-style)
- `/flashcards --session 20` — focused 20-card mixed-subject session
- `/flashcards Contract Law --export` — export flashcards as markdown file

---

## Profile Check

- Read subjects from student profile — match to subject in request
- Check if flashcards already exist for this subject in the session context

---

## Mode: `--generate` — Create Flashcards

Generate flashcards for the requested subject. Three card types:

### Card Type 1 — Term / Definition
```
FRONT: [Legal term or doctrine]
BACK:  [Precise legal definition, with statutory source if applicable]
```
Example:
```
FRONT: Consideration (Indian Contract Act)
BACK:  "When, at the desire of the promisor, the promisee or any other person has done or abstained from doing, or does or abstains from doing, or promises to do or to abstain from doing something, such act or abstinence or promise is called consideration." — S.2(d), Indian Contract Act, 1872
```

### Card Type 2 — Section / Effect
```
FRONT: [Statute name] Section [X]
BACK:  [What it provides, in plain language]
```
Example:
```
FRONT: BNS Section 101
BACK:  Culpable homicide amounting to murder. Punishment: death or imprisonment for life + fine. [Previously IPC S.302 — legislative update 1 July 2024]
```

### Card Type 3 — Case / Ratio
```
FRONT: [Case name] — [year] [court]
BACK:  Ratio: [one-sentence binding legal principle]
       Citation: [full citation] [model knowledge — verify on Indian Kanoon / SCC Online]
```
Example:
```
FRONT: Mohori Bibee v. Dharmodas Ghose — 1903 PC
BACK:  Ratio: A contract by a minor is void ab initio and not merely voidable.
       Citation: ILR (1903) 30 Cal 539 [model knowledge — verify]
```

### How Many Cards

- Default: 15 cards per session (5 of each type)
- If the student uploads notes or a syllabus: generate cards anchored to their actual topics
- Label each card with: subject, type, Leitner bucket (starts at Bucket 1 for all new cards)

---

## Mode: `--drill` — Leitner Drill

**Leitner bucket system:**
- **Bucket 1** (daily): cards the student got wrong or is unsure about
- **Bucket 2** (every 2 days): cards the student got right once
- **Bucket 3** (every week): cards the student got right consistently

### Drill Protocol

For each card:
1. Show the FRONT only. Wait.
2. Student says their answer (or "blank" if they don't know).
3. Reveal the BACK.
4. Ask: "Did you get it? Fully / Partially / No"
5. Move the card:
   - **Fully correct** → promote one bucket (B1 → B2, B2 → B3)
   - **Partially correct or unsure** → stay in current bucket
   - **Wrong** → return to Bucket 1

After the drill session:
```
SESSION SUMMARY — [Subject] Flashcards
Cards drilled: [N]
Bucket 1 (still shaky): [N cards — titles]
Bucket 2 (improving): [N cards — titles]
Bucket 3 (solid): [N cards — titles]
Next review: [Bucket 1 — tomorrow | Bucket 2 — [date] | Bucket 3 — [date]]
```

---

## Mode: `--session n` — Focused Session

Drill a mixed set of `n` cards from across all subjects, prioritising Bucket 1 cards.

> "Running a [n]-card session. I'll pick from your highest-priority cards first. Ready?"

---

## Mode: `--export` — Export as Markdown

Export all flashcards for the subject as a clean markdown file the student can save, print, or import into Anki or Notion.

Format:
```markdown
# [Subject] Flashcards
Generated: [date]

## Card 1 — Term
**Q:** [FRONT]
**A:** [BACK]

## Card 2 — Section
...
```

---

## Citation Rule

All case citations on flashcard backs must carry:
```
[model knowledge — verify on Indian Kanoon / SCC Online]
```

All legislative references that involve IPC/CrPC/IEA must carry:
```
[Legislative update — check BNS/BNSS/BSA equivalent]
```
