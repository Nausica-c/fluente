from engine.intent_mapper import get_intent
import datetime
import os
import random

POSTS_DIR = "_posts"

# 🧠 piccole strutture per rendere articoli più vari
EXAMPLES = [
    "Esempio pratico:",
    "Situazione reale:",
    "Immagina questo:",
    "Caso concreto:"
]

STEPS = [
    "Ascolta e ripeti frasi reali",
    "Usa subito nella vita quotidiana",
    "Impara in contesto, non parole isolate",
    "Ripeti ogni giorno per 10 minuti"
]


def slugify(text):
    return text.lower().replace(" ", "-").replace("'", "")


def build_article(cluster):
    """
    ✍️ crea un articolo SEO completo partendo da un cluster
    """

    intent = get_intent(cluster)

    title = intent.capitalize()
    slug = slugify(title)

    date = datetime.date.today().isoformat()

    example = random.choice(EXAMPLES)

    steps = "\n".join([f"- {s}" for s in random.sample(STEPS, 3)])

    content = f"""---
layout: post
title: "{title}"
cluster: "{cluster}"
date: {date}
---

## {title}

### {example}
Questo è esattamente ciò che devi saper fare se vuoi migliorare velocemente.

### Situazione reale
{intent}.  
Questa è una delle situazioni più comuni per chi studia inglese.

### Metodo pratico
{steps}

### Errore comune
Studiare liste di parole senza usarle nella vita reale.

### Soluzione
Imparare attraverso situazioni reali e ripetizione attiva.

### Perché funziona
Perché il cervello ricorda meglio ciò che usa in contesto reale.

👉 CTA: Inizia oggi il tuo percorso guidato e accelera l’apprendimento.
"""

    return slug, content


def save_article(slug, content):
    """
    💾 salva articolo in _posts
    """

    os.makedirs(POSTS_DIR, exist_ok=True)

    path = os.path.join(POSTS_DIR, f"{slug}.md")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
