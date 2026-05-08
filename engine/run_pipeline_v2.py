import yaml
import os

from engine.content_generator import build_article, save_article
from engine.linking_engine import add_internal_links
from engine.cta_engine import get_cta, format_cta


# 📦 carica clusters
def load_clusters():
    with open("config/clusters.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["clusters"]


def run():
    """
    🚀 ORCHESTRATORE COMPLETO FLUENTEMENTE GROWTH ENGINE 2.0
    """

    clusters = load_clusters()

    print("🚀 Starting FluenteMente Growth Engine 2.0")

    for cluster_name in clusters.keys():

        print(f"\n⚡ Cluster: {cluster_name}")

        # 🔁 genera più articoli per cluster
        for i in range(10):  # puoi aumentare a 100

            # ✍️ 1. crea articolo
            slug, content = build_article(cluster_name)

            # 🔗 2. aggiunge linking SEO
            content = add_internal_links(content, f"{slug}.md")

            # 💰 3. aggiunge CTA monetizzazione
            cta = get_cta(cluster_name)
            content += format_cta(cta)

            # 💾 4. salva file
            save_article(slug + f"-{i}", content)

    print("\n✅ All articles generated successfully!")


if __name__ == "__main__":
    run()
