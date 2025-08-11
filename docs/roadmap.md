$content = @'
# Roadmap — Self-Study Phases

A phased plan to progress from foundations to advanced AI, agents, and robotics, with social-impact breathing space.

## Phase 1 — Core Foundations
(Get the math, probability, and basic CS building blocks out of the way, while doing something social-impact focused on the side)

- Main Tech Courses:
  - CS103A – Mathematical Foundations of Computing – Logic, proofs, sets.
  - CS109 – Probability for Computer Scientists – Essential for ML & robotics reasoning.
- Breather / Social Good:
  - CS21Si – AI for Social Good – Project-based, socially relevant applications.

## Phase 2 — Intro to AI & Hands-On Systems
(Learn AI principles while building real systems)

- Main Tech Courses:
  - CS221 – Artificial Intelligence: Principles and Techniques – Search, MDPs, Bayesian inference.
  - CS123 – A Hands-On Introduction to Building AI-Enabled Systems – Build working AI applications.
- Breather / Social Good:
  - CS25 – Transformers United V5 – Engaging talks, guest lectures, cutting-edge transformer work without heavy math load.

## Phase 3 — Deep Learning Core
(Move into deep neural networks and their applications)

- Main Tech Courses:
  - CS224N – Natural Language Processing with Deep Learning – Build NLP systems with transformers.
  - CS224R – Deep Reinforcement Learning – RL methods for agents and robotics.
- Breather / Social Good:
  - CS329X – Human-Centered LLMs – Design LLMs for usability, safety, and ethics.

## Phase 4 — Advanced AI Theory & Agents
(Push into higher-level AI reasoning and self-improving systems)

- Main Tech Courses:
  - CS234 – Reinforcement Learning – Policy gradients, deep Q-networks, exploration.
  - CS336 – Language Modeling from Scratch – From dataset prep to training large models.
- Breather / Social Good:
  - CS329A – Self-Improving AI Agents – How to make agents learn from experience autonomously.

## Phase 5 — Robotics-Specific Mastery
(Apply AI knowledge to physical autonomous systems)

- Main Tech Courses:
  - Principles of Robot Autonomy II – Planning, perception, and coordination in robots.
  - CS224G – Reinforcement Learning Winter 2025 – Robotics-oriented RL applications.
- Breather / Social Good:
  - CS221N – Natural Language Processing with… (more specialized NLP; tie into social robotics)

## Phase 6 — Specialized & Mathematical Depth
(Get niche skills for research and optimization)

- Main Tech Courses:
  - CS239 – Eigenvalue Computations – For large-scale optimization & scientific computing.
  - CS224W – Machine Learning with Graphs – Graph ML for social networks, knowledge graphs.
- Breather / Social Good:
  - CS21Si – Return for a new project focus, integrating robotics/AI from earlier phases.

---

## Tracking (checklist)
- [ ] CS103A — Mathematical Foundations of Computing
- [ ] CS109 — Probability for Computer Scientists
- [ ] CS221 — AI: Principles and Techniques
- [ ] CS123 — Hands-On AI-Enabled Systems
- [ ] CS224N — NLP with Deep Learning
- [ ] CS224R — Deep RL
- [ ] CS234 — Reinforcement Learning
- [ ] CS336 — Language Modeling from Scratch
- [ ] CS224W — Machine Learning with Graphs
- [ ] CS239 — Eigenvalue Computations
- [ ] Principles of Robot Autonomy II
- [ ] CS224G — RL (Robotics)
- [ ] CS25 — Transformers United (V5)
- [ ] CS329X — Human-Centered LLMs
- [ ] CS329A — Self-Improving AI Agents
- [ ] CS21Si — AI for Social Good (Phase 1)
- [ ] CS21Si — AI for Social Good (Phase 6 revisit)

## How to use this roadmap
- Draft deep notes and experiments in `courses/<COURSE>/<MODULE>/`.
- Distill key insights and formulas into `docs/courses/<COURSE>/<MODULE>.md`.
- Update this page’s checklist with links to your new module pages.
- Keep a weekly reflection in the repo README or a docs page of your choice.
'@
New-Item -ItemType Directory -Force docs | Out-Null
Set-Content -Path docs/roadmap.md -Value $content -Encoding UTF8