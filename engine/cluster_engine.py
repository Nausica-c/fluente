import random

def generate_titles(cluster, n=100):

    templates = [
        "Come imparare {c} velocemente",
        "Metodo pratico per {c}",
        "Errori comuni in {c}",
        "Strategia avanzata di {c}",
        "Guida completa a {c} per principianti",
        "Perché fallisci con {c} e come risolvere",
        "Il metodo più semplice per {c}"
    ]

    return [
        random.choice(templates).replace("{c}", cluster.replace("_", " "))
        for _ in range(n)
    ]
