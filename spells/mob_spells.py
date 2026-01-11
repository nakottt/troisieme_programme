import random

# spell poule sauvage 

def poule_attaque(hp_joueur):
    degats = random.randint(10,12)
    hp_joueur -= degats
    print ("La poule picore et inflige", degats, "points de dégats.")
    return hp_joueur