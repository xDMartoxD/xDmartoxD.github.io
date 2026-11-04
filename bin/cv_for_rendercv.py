#!/usr/bin/env python3
"""Convert _data/cv.yml (shared with the website's CV page) into RenderCV's stricter schema.

The website reads cv.label, cv.summary and award `title`/`awarder` keys, which RenderCV
rejects, and the email is stored as `pdf_email` so the web page doesn't publish it. This
writes a RenderCV-ready copy without touching the original:

    python bin/cv_for_rendercv.py _data/cv.yml _data/cv.rendercv.yml
"""

import sys

import yaml


def convert(data: dict) -> dict:
    cv = data["cv"]
    for key in ("label", "image"):
        cv.pop(key, None)

    # The address is kept out of the web page (as pdf_email) but belongs on the PDF.
    pdf_email = cv.pop("pdf_email", None)
    if pdf_email:
        cv["email"] = pdf_email

    sections = cv.get("sections", {})
    summary = cv.pop("summary", None)
    if summary:
        sections = {"Summary": [" ".join(summary.split())], **sections}

    # The web page reads JSON Resume's `studyType` and `score`, which RenderCV ignores.
    for school in sections.get("Education", []):
        if "studyType" in school:
            school["degree"] = school.pop("studyType")
        score = school.pop("score", None)
        if score:
            school["highlights"] = [score, *school.get("highlights", [])]

    # Award entries use `title`, which RenderCV reads as a publication needing authors.
    for award in sections.get("Awards", []):
        if "title" in award:
            award["name"] = award.pop("title")
        if "awarder" in award:
            award["location"] = award.pop("awarder")
        award.pop("authors", None)

    cv["sections"] = sections
    return data


def main() -> None:
    source, target = sys.argv[1], sys.argv[2]
    with open(source, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    with open(target, "w", encoding="utf-8") as f:
        yaml.safe_dump(convert(data), f, allow_unicode=True, sort_keys=False)


if __name__ == "__main__":
    main()
