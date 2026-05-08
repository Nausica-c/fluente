import os
import datetime

POSTS_DIR = "_posts"

def slugify(title):
    return title.lower().replace(" ", "-").replace("'", "")

def build_article(title, cluster):

    date = datetime.date.today().isoformat()
    slug = slugify(title)

    content = f"""---
layout: post
title: "{title}"
slug: "{slug}"
cluster: "{cluster}"
date: {date}
---

## {title}

Parte del cluster: **{cluster}**

### Metodo
- pratica quotidiana
- input reale
- esposizione costante

### Errore comune
Studiare troppo teoria senza output.

### Soluzione
Usa un sistema guidato e progressivo.

👉 CTA: Inizia oggi il tuo percorso strutturato.
"""

    return slug, content


def save(slug, content):
    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(f"{POSTS_DIR}/{slug}.md", "w", encoding="utf-8") as f:
        f.write(content)
