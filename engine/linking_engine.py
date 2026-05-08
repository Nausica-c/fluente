import os
import random

POSTS_DIR = "_posts"


def get_all_articles():
    """
    📚 prende tutti gli articoli creati
    """
    if not os.path.exists(POSTS_DIR):
        return []

    return [f for f in os.listdir(POSTS_DIR) if f.endswith(".md")]


def extract_title(filename):
    """
    🧠 trasforma filename in titolo leggibile
    """
    return filename.replace(".md", "").replace("-", " ")


def add_internal_links(content, current_file):
    """
    🔗 aggiunge link ad altri articoli
    """

    articles = get_all_articles()

    # rimuove articolo corrente
    articles = [a for a in articles if a != current_file]

    if len(articles) == 0:
        return content

    # sceglie fino a 3 articoli casuali
    selected = random.sample(articles, min(3, len(articles)))

    links_block = "\n\n### 📚 Articoli correlati\n"

    for a in selected:
        title = extract_title(a)
        url = f"/_posts/{a}"
        links_block += f"- [{title}]({url})\n"

    return content + links_block
