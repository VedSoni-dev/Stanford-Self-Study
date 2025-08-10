# Stanford Self-Study (Vedant)

Public, structured notes + code as I self-learn top Stanford AI/ML/Robotics courses.
The goal isn’t to mirror PDFs — it’s to **distill**, **apply**, and **build**.

## Why this exists
- Open-source, disciplined learning in public
- Distilled notes (my words) + minimal formulas that matter
- Small, runnable examples to prove understanding
- Portfolio signal for research & internships

## What’s inside
- `docs/` → Public website (MkDocs Material) with LaTeX
- `courses/` → Course folders with modules: `notes.md`, `example_project.ipynb`, `hw_solution/`
- `scripts/create_module.py` → Scaffolds new modules quickly
- `notebooks/` → Scratch work / experiments

## Courses (growing)
- [ ] CS229 – Machine Learning
- [ ] CS231n – Convolutional Neural Networks for Visual Recognition
- [ ] CS224N – Natural Language Processing with Deep Learning (planned)
- [ ] CS238 – Decision Making under Uncertainty (planned)

## Study log
- **Week 1:** Set up repo & site. Re-derived normal equation; fit LR on toy data.
- **Week 2:** Logistic regression from scratch; gradient check passed.

## Credits & Fair Use
- Links to original course pages and materials are included in each course index.
- All summaries and solutions are my own work. Please follow each course’s honor code.

## Local dev
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
mkdocs serve
```

## Deploy (GitHub Pages)
Push to main; CI publishes to gh-pages. Site URL:
https://<YOUR_GITHUB_USERNAME>.github.io/stanford-self-study
