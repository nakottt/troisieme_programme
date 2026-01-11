from spells.mob_spells import mobs_attackes

MOBS = {
    "poule_sauvage": {"nom": "Poule Sauvage", "pv": 30, "attaques": mobs_attackes["poule_sauvage"]},
    "dinde_enragee": {"nom": "Dinde Enragée", "pv": 45, "attaques": mobs_attackes["dinde_enragee"]},
    "gobelin": {"nom": "Gobelin", "pv": 50, "attaques": mobs_attackes["gobelin"]},
    "orc": {"nom": "Orc", "pv": 80, "attaques": mobs_attackes["orc"]},
    "troll": {"nom": "Troll", "pv": 100, "attaques": mobs_attackes["troll"]},
}

def get_mob(key):
    mob = MOBS.get(key)
    if mob:
        return mob.copy()  # pour ne pas modifier l’original
    return None

#liste de mobs à placer sur la map
MOBS_SUR_MAP = [
    get_mob("gobelin"),
    get_mob("orc"),
    get_mob("troll")
]