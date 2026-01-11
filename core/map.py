import random
from core.combat import pve

def creer_map():
    return [
        list("###########"),
        list("#P..HO....#"),
        list("#..##.....#"),
        list("#..TO..B..#"),
        list("#......GC.#"),
        list("###########")
    ]

def afficher_map(map_data):
    for ligne in map_data:
        print(" ".join(ligne))

def trouver_joueur(map_data):
    for y, ligne in enumerate(map_data):
        for x, case in enumerate(ligne):
            if case == "P":
                return x, y

def deplacer_joueur(map_data, direction, joueur, mobs):
    x, y = trouver_joueur(map_data)

    directions = {
        "z": (0, -1),
        "s": (0, 1),
        "q": (-1, 0),
        "d": (1, 0)
    }

    if direction not in directions:
        return joueur["pv"]

    dx, dy = directions[direction]
    nx, ny = x + dx, y + dy

    if ny < 0 or ny >= len(map_data) or nx < 0 or nx >= len(map_data[0]):
        return joueur["pv"]

    case = map_data[ny][nx]

    if case == "#":
        print("🚫 Mur")
        return joueur["pv"]

    # déplacement
    map_data[y][x] = "."
    map_data[ny][nx] = "P"

    # herbes = combat aléatoire
    if case == "G" and random.random() < 0.3:
        mob = random.choice(mobs)
        joueur["pv"] = pve(
            joueur["nom"],
            joueur["classe"],
            joueur["pv"],
            mob["nom"],
            mob["pv"]
        )

    if case == "C":
        print("💊 Centre : PV restaurés")
        joueur["pv"] = joueur["pv_max"]

    if case == "B":
        boss = mobs[-1]
        joueur["pv"] = pve(
            joueur["nom"],
            joueur["classe"],
            joueur["pv"],
            boss["nom"],
            boss["pv"]
        )
    if case == "H":
        Goblin = mobs[-2]
        joueur["pv"] = pve(
            joueur["nom"],
            joueur["classe"],
            joueur["pv"],
            Goblin["nom"],
            Goblin["pv"]
        )
    if case == "O":
        Orc = mobs[-2]
        joueur["pv"] = pve(
            joueur["nom"],
            joueur["classe"],
            joueur["pv"],
            Orc["nom"],
            Orc["pv"]
        )
    if case == "T":
        Troll = mobs[-1]
        joueur["pv"] = pve(
            joueur["nom"],
            joueur["classe"],
            joueur["pv"],
            Troll["nom"],
            Troll["pv"]
        )

    return joueur["pv"]