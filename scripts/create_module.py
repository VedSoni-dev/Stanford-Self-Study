#!/usr/bin/env python3
import argparse, os, textwrap

TEMPLATE = textwrap.dedent("""\
# {number} — {title}

**Learning goals**
- …

**Key formulas**
- …

**Notebook**
- `courses/{course}/{slug}/example_project.ipynb`

**Reflection**
- …
""")

NOTES = """# Notes — {title}

(Your distilled notes here.)
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True, help="e.g., CS229")
    ap.add_argument("--slug", required=True, help="e.g., 02-logistic-regression")
    ap.add_argument("--title", required=True, help='e.g., "Logistic Regression"')
    ap.add_argument("--number", default="", help='e.g., "02"')
    args = ap.parse_args()

    course = args.course
    slug = args.slug
    title = args.title
    number = args.number or slug.split("-")[0]

    # docs page
    docs_dir = f"docs/courses/{course}"
    os.makedirs(docs_dir, exist_ok=True)
    docs_page = os.path.join(docs_dir, f"{slug}.md")
    with open(docs_page, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(number=number, title=title, course=course, slug=slug))

    # course source
    src_dir = f"courses/{course}/{slug}"
    os.makedirs(src_dir, exist_ok=True)
    with open(os.path.join(src_dir, "notes.md"), "w", encoding="utf-8") as f:
        f.write(NOTES.format(title=title))
    open(os.path.join(src_dir, "example_project.ipynb"), "w").close()
    os.makedirs(os.path.join(src_dir, "hw_solution"), exist_ok=True)

    print(f"Created module {course}/{slug}")

if __name__ == "__main__":
    main()
