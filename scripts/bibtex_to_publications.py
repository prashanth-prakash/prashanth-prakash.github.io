# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 18:10:33 2026

@author: prash
"""

import bibtexparser
from pathlib import Path
from datetime import datetime
import re

BIB_FILE = "../publications.bib"
OUT_DIR = Path("../_publications")
OUT_DIR.mkdir(exist_ok=True)

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

with open(BIB_FILE) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

for entry in bib_database.entries:
    title = entry.get("title", "Untitled").replace("{", "").replace("}", "")
    year = entry.get("year", "1900")
    venue = entry.get("journal") or entry.get("booktitle") or ""
    url = entry.get("url") or entry.get("doi", "")
    date = f"{year}-01-01"

    filename = f"{year}-{slugify(title)[:50]}.md"
    path = OUT_DIR / filename
    entry_type = entry.get("ENTRYTYPE", "")

    if entry_type == "article":
        category = "manuscripts"
    elif entry_type == "inproceedings":
        category = "conferences"
    else:
        category = "manuscripts"
    front_matter = f"""---
title: "{title}"
venue: "{venue}"
date: {date}
category: {category}
paperurl: "{url}"
excerpt: ""
---
"""

    path.write_text(front_matter, encoding="utf-8")

print(f"Created {len(bib_database.entries)} publication files.")
