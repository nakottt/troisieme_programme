



# ======================
# CONSTANTES
# ======================
RACES = ["Humain", "Elfe", "Nain", "Gnome", "Worgen", "Drainei"]
CLASSES = ["Guerrier", "Mage", "Voleur", "Druide", "Chasseur", "Pretre"]

HP_by_class = {
    "Guerrier": 200,
    "Mage": 100,
    "Voleur": 120,
    "Druide": 130,
    "Chasseur": 140,
    "Pretre": 90
}



# ======================
# CRÉATION DU PERSONNAGE
# ======================
                                             #
# print(f"\nVotre personnage s'appelle {nom_joueur}, race {race}, classe {classe}.")      # mettre ces lignes dans main.py
# print(f"{nom_joueur} possède {HP_PAR_CLASSE[classe]} points de vie.\n")                 #


def choose_race():   
    print ("Choisissez une race pour votre personnage :")
    for i, r in enumerate(RACES):
        print(f"{i+1}. {r}")
    race = input("Choisir une race : ")
    while race not in RACES:
        race = input("Race invalide, recommence : ")
    return race

def choose_class():   
    print ("Choisissez une classe pour votre personnage :")
    for i, c in enumerate(CLASSES):
        print(f"{i+1}. {c}")
    classe = input("Choisir une classe : ")
    while classe not in CLASSES:
        classe = input("Classe invalide, recommence : ")
    return classe

def choose_name():   
    player_name = input("Entrez le nom de votre personnage : ")
    return player_name

