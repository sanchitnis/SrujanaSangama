# Deployment & Adoption Loop

> **Intent:** Get a working domain into faculty hands and help them actually start using it.
> **Owner:** Sanjay Chitnis, with REVA IT for shared-folder distribution.
> **Cadence:** Per domain release.
> See [`LOOPS.md`](../LOOPS.md) for how this loop relates to the other six.

---

## Why This Loop Exists

A Verifier-passed PR merged into the shared `SrujanaSangama` folder doesn't automatically mean a faculty member knows it exists, knows how to use it, or trusts it enough to try. This loop is the deliberate work of closing that gap — what would be called "marketing" in a commercial product, but is better named **faculty enablement and change management** here, since the audience is internal, the relationship is ongoing, and the goal is adoption and trust rather than a sale.

---

## What Happens When a Domain or Command Is Ready

1. **Update `specification/IMPLEMENTATION-STATUS.md`** — this is the trigger for everything downstream. A domain or command isn't "released" until its status there changes to Implemented, per the existing rule in `AGENTS.md` §8 and `CONTRIBUTING.md`'s PR checklist.
2. **Update `README.md`** — per `AGENTS.md` §8, README only ever describes what's Implemented. This loop is responsible for making sure that update actually happens promptly, not just eventually.
3. **Write a short release note** — what's new, who it's for, and the one command to try first. Lives at `deployment/release-notes/YYYY-MM-DD-<topic>.md`. This is the artifact this loop is actually accountable for producing; README and IMPLEMENTATION-STATUS.md updates are mechanical, the release note is where faculty enablement actually happens.
4. **Choose a rollout shape** appropriate to the domain:
   - **Quiet rollout** — update the docs and release note, let early adopters find it (appropriate for a small refinement to an existing domain).
   - **Targeted rollout** — reach out directly to the specific role most affected (e.g., IQAC coordinators, when `/aqar-generate` ships), pointing them at the relevant Step 6 row in `design.md`'s Workspace Setup table.
   - **Announced rollout** — a wider note (department meeting, email, or whatever channel REVA normally uses for faculty-facing announcements) for a new domain that changes what a large group of people can do.
5. **Confirm the shared OneDrive folder is actually synced** for whoever needs the update — this loop owns the practical "did REVA IT's distribution actually reach people" check, not just the content of what was built.

---

## Adoption Support, Not Just Announcement

Getting a faculty member from "I heard about this" to "I used it successfully once" is this loop's real measure of success, not just publishing a release note. In practice this means:

- Keeping the **Workspace Setup — Step by Step** section in `design.md` and the **Where Things Stand** section in `README.md` honest and current, since that's the self-serve path most faculty will actually use.
- Being available, directly, for the first few people trying a newly released domain — early friction reported straight back to this loop is cheaper to fix than friction discovered later through the Telemetry Loop.
- Treating the first month after a release as part of the deployment work, not as "done, moving on" — this is the period the Telemetry & Feedback Loop most needs early signal from.

---

## How This Loop Connects to the Others

- Receives a merged, Verifier-passed PR from Loop 5.
- Hands live usage to Loop 7, which starts collecting signal from the moment of rollout.
- Feeds back to Loop 2 (Business & Institutional Analysis) if rollout surfaces an institutional-level blocker (e.g., REVA IT can't sync the folder to a particular school's machines) — that's an institutional problem, not a product or implementation one.
