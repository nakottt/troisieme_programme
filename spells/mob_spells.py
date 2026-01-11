import random

# spell poule sauvage 

def poule_attaque(hp_joueur):
    degats = random.randint(10,12)
    hp_joueur -= degats
    print ("La poule picore et inflige", degats, "points de dégats.")
    return hp_joueur

# spell dinde enragée

def dinde_attaque(hp_joueur):
    degats = random.randint(12,15)
    hp_joueur -= degats
    print ("La dinde enragée donne un coup de bec et inflige", degats, "points de dégats.")
    return hp_joueur

# spell gobelin

def gobelin_attaque(hp_joueur):
    degats = random.randint(15,18)
    hp_joueur -= degats
    print ("Le gobelin attaque avec sa massue et inflige", degats, "points de dégats.")
    return hp_joueur

# spell orc

def orc_attaque(hp_joueur):
    degats = random.randint(18,22)
    hp_joueur -= degats
    print ("L'orc frappe avec sa hache et inflige", degats, "points de dégats.")
    return hp_joueur

# spell troll

def troll_attaque(hp_joueur):
    degats = random.randint(20,25)
    hp_joueur -= degats
    print ("Le troll écrase avec ses poings et inflige", degats, "points de dégats.")
    return hp_joueur

mobs_attackes = {
    "poule_sauvage": poule_attaque,
    "dinde_enragee": dinde_attaque,
    "gobelin": gobelin_attaque,
    "orc": orc_attaque,
    "troll": troll_attaque
}