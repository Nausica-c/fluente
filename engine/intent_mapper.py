import random

# 🧠 CERVELLO COMPLETO DEL SISTEMA FLUENTEMENTE

INTENTS = {
    "beginner": [
        "imparare inglese da zero",
        "prime frasi inglese base",
        "capire inglese semplice"
    ],

    "speaking": [
        "parlare inglese senza paura",
        "sbloccare il parlato inglese",
        "fluency speaking practice"
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

    "mindset": [
        "come non mollare imparando inglese",
        "motivazione per studiare lingue",
        "perché non riesco a imparare inglese"
    ],

    "metodo": [
    "come imparare inglese velocemente con metodo",
    "miglior metodo per imparare una lingua",
    "metodo immersione totale inglese",
    "tecnica per imparare inglese senza studiare ore",
    "strategia efficace per imparare lingue"
],

    "grammatica_pratica": [
        "grammatica inglese facile esempi",
        "come usare tempi verbali inglese",
        "regole inglese spiegate semplice"
    ],

    "vocabolario": [
        "parole inglese più usate",
        "vocabolario inglese quotidiano",
        "frasi utili inglese base"
    ],

    "errori": [
        "errori comuni inglese italiani",
        "perché sbaglio inglese",
        "come correggere inglese"
    ],

    "curiosita": [
        "curiosità lingua inglese",
        "perché inglese è così strano",
        "parole inglese strane significato"
    ],

    "lifelong_learner": [
        "come mantenere inglese fluente",
        "livello avanzato inglese",
        "perfezionare inglese ogni giorno"
    ]
}


def get_intent(cluster):
    """
    🧠 trasforma un cluster in un bisogno reale umano
    """
    return random.choice(INTENTS.get(cluster, ["imparare inglese"]))
