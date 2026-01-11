from core.map import creer_map, afficher_map, deplacer_joueur
from core.mobs import MOBS_SUR_MAP



# ======================# BOUCLE PRINCIPALE # ======================#

def boucle_console(player):
    map_data = creer_map()
    MOBS_on_map = MOBS_SUR_MAP
    
    while player["pv"] > 0:
        afficher_map(map_data)
        print(f"❤️ PV : {player['pv']}/{player['pv_max']}")
        direction = input("Déplacez votre personnage (z/q/s/d) ou 'x' pour quitter : ").lower()

        if direction == "x":
            print("Merci d'avoir joué !")
            break

        player["pv"] = deplacer_joueur(
            map_data,
            direction,
            player,
            MOBS_on_map
        )
    print("💀 Fin de l'aventure.")