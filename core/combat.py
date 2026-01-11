import time
from spells.mob_spells import mobs_attackes
from spells.player_spells import classes_attackes
import random
import unicodedata
import re


def _normalize_name(name: str) -> str:
    s = name.lower()
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    s = re.sub(r'[^a-z0-9]+', '_', s).strip('_')
    return s


def pve(nom_joueur, classe_joueur, hp_joueur, mob_nom, mob_pv):
    """Combat entre le joueur et un mob.

    Parameters:
    - `mob_nom`: affichage (ex: 'Poule Sauvage' ou 'poule sauvage')
    - `mob_pv`: points de vie du mob (int)
    """
    hp_monstre = mob_pv

    # trouver les attaques du mob via la table `mobs_attackes`
    key = _normalize_name(mob_nom)
    if key in mobs_attackes:
        mob_attacks = [mobs_attackes[key]]
    else:
        # fallback : essayer de trouver une clé contenant le nom, sinon prendre toutes
        matches = [v for k, v in mobs_attackes.items() if key in k]
        mob_attacks = matches if matches else list(mobs_attackes.values())

    print(f"\nUn {mob_nom} apparaît !")
    time.sleep(1.5)

    while hp_monstre > 0 and hp_joueur > 0:
        print(f"\nVous avez {hp_joueur} PV.")
        print(f"{mob_nom} a {hp_monstre} PV.\n")

        # Affichage attaques du joueur
        print("Attaques disponibles :")
        for i, spell in enumerate(classes_attackes[classe_joueur.lower()]):
            print(f"{i+1}. {spell.__name__}")

        # Choix attaque joueur
        choix = input("Choisissez votre attaque (1, 2 ou 3) : ")
        if choix in ["1", "2", "3"]:
            selected_spell = classes_attackes[classe_joueur.lower()][int(choix)-1]
            hp_monstre = selected_spell(hp_monstre, nom_joueur)
        else:
            print("Choix invalide, recommencez.")
            continue

        if hp_monstre <= 0:
            print(f"Le {mob_nom} est vaincu !")
            break

        # Attaque du mob
        mob_spell = random.choice(mob_attacks)
        hp_joueur = mob_spell(hp_joueur)
        if hp_joueur <= 0:
            print(f"{nom_joueur} est vaincu ! Game Over.")
            break

        time.sleep(1)

    return hp_joueur