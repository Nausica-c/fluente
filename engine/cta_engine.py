# 💰 CTA ENGINE — trasforma traffico in conversioni

def get_cta(cluster):
    """
    🎯 restituisce CTA diversa in base al tipo di utente
    """

    ctas = {
        "beginner": {
            "text": "Inizia da zero con un percorso guidato passo-passo",
            "tone": "gentle"
        },

        "metodo": {
    "text": "Scopri un metodo che ti fa finalmente parlare inglese senza studiare ore",
    "tone": "high-intent"
},
        "speaking": {
            "text": "Sblocca finalmente il tuo parlato in inglese",
            "tone": "urgent"
        },

        "viaggi": {
            "text": "Impara a parlare in viaggio senza stress",
            "tone": "practical"
        },

        "business": {
            "text": "Migliora il tuo inglese per lavoro e carriera",
            "tone": "professional"
        },

        "mindset": {
            "text": "Supera il blocco mentale e resta costante",
            "tone": "motivational"
        },

        "grammatica_pratica": {
            "text": "Impara la grammatica senza studiare teoria inutile",
            "tone": "educational"
        },

        "vocabolario": {
            "text": "Impara le parole che servono davvero ogni giorno",
            "tone": "practical"
        },

        "errori": {
            "text": "Smetti di fare gli errori più comuni in inglese",
            "tone": "corrective"
        },

        "curiosita": {
            "text": "Scopri curiosità che rendono l’inglese più facile",
            "tone": "engaging"
        },

        "lifelong_learner": {
            "text": "Mantieni il tuo inglese sempre fluente e naturale",
            "tone": "advanced"
        }
    }

    default_cta = {
        "text": "Inizia a imparare inglese in modo guidato",
        "tone": "neutral"
    }

    return ctas.get(cluster, default_cta)


def format_cta(cta):
    """
    💬 formatta la CTA per l'articolo
    """

    return f"""
---

## 🚀 Inizia ora

👉 {cta['text']}

✔ metodo guidato  
✔ progressione chiara  
✔ risultati reali  
"""
