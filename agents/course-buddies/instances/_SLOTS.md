# Course Buddy — Active Instance Slots

> Slots 01–10 are available for active Course Buddy deployments.
> After running `build.py`, copy the generated `skill.md` to the appropriate slot below
> and update this registry.
>
> **Rule**: Never deploy a generated skill without faculty review.
> **To build**: See [`skills/course-buddy-builder/SKILL.md`](../../../skills/course-buddy-builder/SKILL.md)

---

| Slot | Course Code | Course Name | Stream | Sem | Status | Last Built |
|------|-------------|-------------|--------|:---:|--------|-----------|
| 01 | — | — | — | — | 🔲 Empty | — |
| 02 | — | — | — | — | 🔲 Empty | — |
| 03 | — | — | — | — | 🔲 Empty | — |
| 04 | — | — | — | — | 🔲 Empty | — |
| 05 | — | — | — | — | 🔲 Empty | — |
| 06 | — | — | — | — | 🔲 Empty | — |
| 07 | — | — | — | — | 🔲 Empty | — |
| 08 | — | — | — | — | 🔲 Empty | — |
| 09 | — | — | — | — | 🔲 Empty | — |
| 10 | — | — | — | — | 🔲 Empty | — |

---

## Status Key

| Symbol | Meaning |
|--------|---------|
| 🔲 Empty | No skill assigned to this slot |
| 🟡 Draft | Skill generated but pending faculty review |
| ✅ Active | Faculty-approved and live |
| 🔄 Refresh needed | Skill is stale — run `build.py --refresh` |

---

## How to assign a slot

1. Run the build pipeline:
   ```
   cd skills\course-buddy-builder\tools\course-buddy-builder
   python build.py --course-file templates\[CourseCode]-descriptor.md --output-dir ..\..\..\..\knowledge\
   ```
2. Review the generated `knowledge\instances\[CourseCode]-[ShortName]\skill.md`
3. Copy (or rename) it to this directory as `0N-[CourseCode]-[ShortName].md`
4. Update the slot row above (Status → 🟡 Draft)
5. Faculty approves → update status to ✅ Active
