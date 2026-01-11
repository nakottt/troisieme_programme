from core.combat import pve
from core.character import choose_race, choose_class, choose_name
from core.character import HP_by_class
from core.map import creer_map, afficher_map, deplacer_joueur
from render.console import boucle_console
from spells.mob_spells import poule_attaque, dinde_attaque

#=====================# CRÉATION DU JOUEUR #======================#
print("Bonjour, créez votre personnage !") 

#====================== #CHOIX RACE #======================#
race = choose_race()

#====================== #CHOIX CLASSE #======================#
classe = choose_class()

#====================== #CHOIX NOM #======================#
player_name = choose_name()

# ======================# JOUEUR (STRUCTURE UNIQUE) # ======================#
player = {
    "nom": player_name,
    "classe": classe,
    "pv": HP_by_class[classe],
    "pv_max": HP_by_class[classe]
}

#======================# PREMIERS COMBATS SCRIPTÉS #======================#
poule = {"nom": "poule sauvage", "pv": 30, "attaque": poule_attaque}
player["pv"] = pve(player["nom"], player["classe"], player["pv"], poule["nom"], poule["pv"])
dinde = {"nom": "dinde enragée", "pv": 45, "attaque": dinde_attaque}
player["pv"] = pve(player["nom"], player["classe"], player["pv"], dinde["nom"], dinde["pv"])

#======================# jeu console #======================#
boucle_console(player)
