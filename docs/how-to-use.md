# How to Use

## For readers
- Use the left sidebar to navigate by course and module.
- Each module page includes:
  - A distilled summary (my words)
  - Key formulas (with LaTeX)
  - A link to the corresponding code/notebook
  - (If applicable) a short reflection

## For contributors (PRs welcome)
1. Fork the repo and create a branch.
2. Keep notes in your own words; do not paste course PDFs.
3. Add runnable examples where possible.
4. If you add a module, use the scaffolder:

```bash
python scripts/create_module.py --course CS229 --slug 02-logistic-regression --title "Logistic Regression"
```

This creates `courses/CS229/02-logistic-regression/notes.md` and a docs page stub.

## Honor code
Do not share restricted assignment prompts or solutions from active course offerings.
