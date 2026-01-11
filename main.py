from core.combat import pve
from core.character import choose_race, choose_class, choose_name
from core.character import HP_by_class
from spells.mob_spells import poule_attaque
from core.map import creer_map, afficher_map, deplacer_joueur
from spells.mob_spells import dinde_attaque
from core.mobs import MOBS_SUR_MAP

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

#======================# MAP #======================#
map_data = creer_map()







# # ======================
# # BOUCLE PRINCIPALE
# # ======================
# while joueur["pv"] > 0:
#     afficher_map(map_data)
#     print(f"❤️ PV : {joueur['pv']}/{joueur['pv_max']}")
#     direction = input("Déplacez votre personnage (z/q/s/d) ou 'x' pour quitter : ").lower()

#     if direction == "x":
#         print("Merci d'avoir joué !")
#         break

#     joueur["pv"] = deplacer_joueur(
#         map_data,
#         direction,
#         joueur,
#         mobs
#     )

# print("💀 Fin de l'aventure.")
