import random

# 🧠 questo è il cervello che capisce cosa vogliono le persone

INTENTS = {
    "beginner": [
        "imparare inglese da zero",
        "prime frasi inglese base",
        "capire inglese semplice"
    ],
    "viaggi": [
        "parlare in aeroporto in inglese",
        "prenotare hotel in inglese",
        "ordinare cibo all’estero"
    ],
    "business": [
        "inglese per lavoro email",
        "colloquio in inglese frasi",
        "riunioni internazionali inglese"
    ],
    "speaking": [
        "sbloccare il parlato inglese",
        "parlare inglese senza paura",
        "fluency speaking practice"
    ]
}

def get_intent(cluster):
    """
    🧠 prende un cluster e restituisce un bisogno reale
    """
    return random.choice(INTENTS.get(cluster, ["imparare inglese"]))
