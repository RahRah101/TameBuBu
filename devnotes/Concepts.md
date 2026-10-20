# Concepts

A primer for anyone who just found this repo. [Reflections.md](Reflections.md) is where I think out loud, and it assumes you already know the vocabulary. This file gives you that vocabulary: what tamebubu is, the ideas it's built on, and a glossary of the terms and acronyms. You don't need a background in learning science or machine learning to read it.

---

## What tamebubu is, in one paragraph

Flashcard software like Anki figured out how to make facts stick: review each card right before you'd forget it. Tamebubu tries to do the same thing for **procedural skills**, the "can you actually solve the problem" kind of knowledge (mathematics, calculus, circuit analysis, statics). Instead of scheduling cards or topics, it schedules your **gaps**: the specific, recurring mistakes you make while solving problems. Gaps aren't written in advance by an expert. They're discovered from your own work and your own reflection on what went wrong, then tracked, tested and scheduled over time.

---

## The ideas it's built on

**1. Practice beats rereading, and spaced practice beats crammed practice.** Testing yourself (retrieval practice) and spreading study over time (spacing) both improve long-term retention. Mixing different problem types in one session (interleaving) helps on top of that, because you have to pick the right method, not just repeat the last one.

**2. Mistakes are systematic, not random.** Students' procedural errors tend to be consistent "bugs" in how they do a procedure, and those bugs can predict future mistakes. If errors have structure, you can schedule practice around that structure.

**3. Gaps don't line up with topics.** People usually study by "weak topics." But many real gaps live in how things combine (recognizing when to use one technique inside another), not inside a single chapter. So tamebubu tracks gaps, not topics.

**4. Reflection is both learning and data.** Explaining your own mistake to yourself helps you learn (the self-explanation effect). It also tells the system far more than a wrong answer does: a wrong answer is one bit; "I forgot the source was between two non-reference nodes" points at the exact gap.

**5. The learner does the thinking.** Tamebubu isn't an AI tutor that diagnoses you and tells you what to do. You name your gaps; the system tracks, tests and schedules them, and checks your diagnoses against what actually happens later.

**6. No universal schedule exists, so it has to be learned.** The research can't say "review after exactly 3 days." The right timing depends on the person and the material, so the schedule is fitted to your own history, the same way modern flashcard schedulers fit theirs.

---

## How the pieces fit

```
  you attempt an exercise
          |
          v
  you reflect on what went wrong  (optional, but it's what makes this work)
          |
          v
  EXTRACTOR ---- names the gap, with quotes from your work as evidence
          |
          v
  GAP REGISTRY - the map: every gap, and which exercises can trigger it
          |
          v
  LEARNER MODEL  how likely you are to get each gap right, now and later
          |
          v
  SCHEDULER ---- which gaps are due, and when
          |
          v
  PRACTICE PLANNER  what to actually do about each due gap
          |
          v
  next exercise  ->  back to the top
```

---

## Glossary

Grouped by topic. Terms in **bold** inside a definition have their own entry.

### Memory and learning science

- **Spaced repetition / SRS (spaced repetition system):** reviewing material at increasing intervals, timed so each review lands right before you'd forget. Anki is the best-known SRS.
- **Spacing effect:** studying spread over time beats the same amount of study crammed together.
- **Retrieval practice / testing effect:** pulling something out of memory (solving, recalling) strengthens it more than rereading it.
- **Interleaving:** mixing different problem types in one session instead of doing a block of one type. Harder while you practice, better on the test.
- **Blocked practice:** the opposite of interleaving. Ten of the same problem type in a row.
- **Desirable difficulty:** a difficulty that slows you down now but improves long-term learning (spacing, interleaving, testing). Only "desirable" if you can still succeed.
- **Declarative vs. procedural knowledge:** knowing *that* (a formula, a definition) vs. knowing *how* (applying it to solve a problem). Flashcards handle declarative well; tamebubu targets procedural.
- **Self-explanation effect:** learners who explain material or their own mistakes to themselves learn more.
- **Generation effect:** material you produce yourself (like writing your own exercise) is remembered better than material you just read.
- **Worked example:** a fully solved problem you study instead of solving. Helps beginners.
- **Faded example:** a worked example with some steps blanked out for you to complete. A bridge from worked examples to full problems.
- **Expertise reversal effect:** what helps a beginner (worked examples, lots of guidance) stops helping, or even hurts, once you're more skilled.
- **Isolated-interacting elements effect:** learning the pieces one at a time first, then all together, can beat getting everything at once.
- **Kolb cycle:** a model of learning from experience: do something, reflect on it, form an idea, try again. Tamebubu's loop is a Kolb cycle on a timer.
- **Bloom's taxonomy:** levels of thinking, from simple recall up to applying, analyzing and creating. Used here as the "order" of an exercise.

### Tamebubu's own terms

- **Gap:** a specific, recurring error pattern in how you solve problems, e.g. "forgets the inner derivative in the chain rule" or "misses supernodes." The unit tamebubu schedules.
- **Slip:** a one-off mistake (a dropped sign, a typo) that doesn't reflect a real gap. A slip shouldn't trigger more practice.
- **Blind automation:** getting fluent at one *shape* of problem without actually fixing the gap, so you fail as soon as the problem looks different. Reaching "automatic" before you've really understood.
- **Emergent gaps:** gaps discovered from learners' actual mistakes and reflections, as opposed to a list an expert wrote in advance.
- **Candidate gap / promoted gap:** a candidate is a gap the extractor just named. It's promoted into the model only if it actually improves predictions of your future mistakes; otherwise it's merged or dropped.
- **Scope:** whether a gap belongs to one learner or is shared across learners.
- **Gap registry:** the list of all known gaps, their descriptions and evidence, and which exercises can trigger them. The map.
- **Learner model:** the statistical model estimating how likely you are to get each gap right, now and in the future.
- **Scheduler:** decides which gaps are due, based on the learner model and a target success rate.
- **Practice planner:** decides what to do about a due gap: a bank exercise, a variant, a worked example, writing your own problem, and so on.
- **Extractor:** the language-model step that reads your work and reflection and names the gap, quoting the parts of your work that show it (**evidence spans**).
- **Reflection:** your own account of what went wrong on a failed attempt, and why.
- **Evidence tiers:** how much the system can learn from an attempt. Reflection plus work is strong evidence, work alone is medium, a bare answer is weak.
- **Variant:** the same problem with different numbers, so you can't just remember the answer.
- **Least-similar trigger:** the exercise that still triggers your gap but looks the most different from where you first made it. Catches blind automation.
- **Skill drill / exercise / problem / challenge:** exercise types from least to most integrative. A drill isolates one technique and takes seconds; a challenge combines many ideas and can take hours.
- **Origin set:** the exercises where you actually made a given gap.
- **Exposure set:** all the exercises that *could* trigger that gap.
- **Clean probe:** an attempt where the gap could have happened and didn't. The evidence that you're improving.
- **Probe distance:** how different an exercise looks from the ones where you made the gap, measured on solution structure.
- **Maturity stages (Fresh, Consolidating, Stable):** how established your fix for a gap is. Fresh gaps get near, simple practice; Stable gaps get far, integrative practice.
- **Surface-bound / transfers:** a gap is surface-bound if you pass similar problems but fail different-looking ones; it transfers if you pass both.
- **Solution-structure embedding:** comparing exercises by *how they're solved*, not how they're worded. "Differentiate sin(x²)" and "differentiate x²·sin(x)" look alike but are solved differently.
- **Harness:** the domain-specific machinery around the core (how a circuits answer gets checked, how a calculus solution gets parsed). Swappable per subject.
- **Horizontal:** tamebubu's core isn't a calculus app or a circuits app. Subjects plug in.
- **Slow loop:** background work that doesn't need to happen immediately: promoting and merging gaps, finding new exercises for a gap, refitting the model.

### Modeling and statistics

- **Knowledge tracing (KT):** a family of models that estimate what a student knows from their history of right and wrong answers.
- **BKT (Bayesian Knowledge Tracing):** the classic KT model: each skill is either learned or not, with probabilities for learning, guessing and slipping. Doesn't model forgetting.
- **DKT (Deep Knowledge Tracing):** KT with a neural network. Powerful, but needs lots of data and its internal "concepts" have no names.
- **DAS3H:** the KT model tamebubu is most similar to. A logistic regression using learner ability, item difficulty, skill difficulty, and how often you've practiced each skill recently. It models forgetting by counting practice in time windows. Name from its features: Difficulty, Ability, Skill, Student Skill practice History.
- **DASH:** DAS3H's predecessor, with one skill per item.
- **Time windows / kernels:** how DAS3H counts recent practice (last hour, day, week, month). Tamebubu wants smooth decay curves (kernels) instead of hard cutoffs, because forgetting fades gradually.
- **Q-matrix:** a table of which exercises exercise which skills (here: which exercises can trigger which gaps). Each entry is called q.
- **Fractional q:** instead of a yes/no, each entry is a number from 0 to 1: how strongly that exercise tests that gap.
- **Beta posterior:** a way to store "how sure are we that exercise X tests gap Y" as two counts that grow with evidence. An initial guess counts for a little; real attempts quickly outweigh it.
- **Prior:** the starting guess before data comes in. "Labels are just priors rather than verdicts": an LLM's first label gets corrected by real data.
- **Attributed counting:** when you fail, only the gap actually responsible gets the blame, not every gap the exercise touches.
- **Reflection term:** an extra feature in the model counting your reflected failures. If its weight comes out positive, reflecting measurably helps.
- **Top-down / bottom-up:** two ways to build the Q-matrix. Top-down: name the gap from your reflection and work. Bottom-up: (the software) finds clusters of exercises you fail together statistically, then name them.
- **Confirmed / folk theory / blind spot / noise:** what happens when top-down and bottom-up are compared. A blind spot (the data shows a pattern you can't name) is the most valuable.
- **Held-out prediction:** testing a model on data it wasn't fitted on. A gap earns its place only if it improves predictions on held-out attempts.
- **Ablation:** turning off one part of a model to see how much it mattered.
- **Learning Factors Analysis (LFA):** a method for deciding whether splitting or merging skills makes a model better, with a penalty for complexity.
- **SPARFA:** a method that discovers latent concepts and the Q-matrix together from response data.

### Tools and prior systems

- **Anki:** the most popular open-source flashcard app.
- **FSRS (Free Spaced Repetition Scheduler):** the modern scheduler used in Anki. Fits a memory model to each user's review history.
- **DSR (Difficulty, Stability, Retrievability):** the three numbers FSRS tracks per card.
- **Math Academy:** an adaptive math platform built on a large, hand-made graph of skills and prerequisites. The opposite of emergent gaps.
- **Eedi:** a math platform where multiple-choice wrong answers are mapped to specific misconceptions.
- **BUGGY / Repair Theory / Mind Bugs:** 1970s–90s research (Brown, Burton, VanLehn) showing that children's subtraction errors are systematic bugs that can be modeled and predicted.
- **CAS (computer algebra system):** software that does symbolic math.
- **LLM (large language model):** used here to read work, extract gaps and describe solution structure. Never trusted to do the math; a CAS checks that.

---

## Where to go next

- **[Reflections.md](Reflections.md):** the decision log: what I chose, what I rejected, why, and what's still open. Start with "The core claim."
- **[Specs.md](Specs.md):** the architecture as built.
- The references at the bottom of Reflections.md, if you want the research behind any of the above.
