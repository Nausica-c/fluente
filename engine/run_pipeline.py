import yaml

from cluster_engine import generate_titles
from article_generator import build_article, save
from git_publisher import publish


def load_clusters():
    with open("config/clusters.yaml", "r") as f:
        return yaml.safe_load(f)["clusters"]


def run():

    clusters = load_clusters()

    for cluster_name in clusters.keys():

        print(f"\n⚡ Generating cluster: {cluster_name}")

        titles = generate_titles(cluster_name, n=100)

        for title in titles:

            slug, content = build_article(title, cluster_name)
            save(slug, content)

    publish()


if __name__ == "__main__":
    run()
