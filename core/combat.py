import time
from spells.mob_spells import poule_attaque
from spells.player_spells import classes_attackes


def pve(nom_joueur, classe_joueur, hp_joueur, nom_monstre, hp_monstre):
    time.sleep(1)
    print (f"Un {nom_monstre} apparaît !")
    time.sleep(1.5)
    while hp_monstre >0 and hp_joueur>0:
            print ("Vous avez", hp_joueur, "points de vie.")
            print (nom_monstre, "a", hp_monstre, "points de vie.")
            time.sleep(1)
            #print ("Attaques disponibles :", [spell.__name__ for spell in classes_attackes[classe_joueur.lower()]])
            print ("Attaques disponibles :")

            for i, spell in enumerate(classes_attackes[classe_joueur.lower()]):
                print (f"{i+1}. {spell.__name__}")

            choix_attaque = input ("Choisissez votre attaque (1 , 2 , ou 3) : ")
            if choix_attaque in ["1", "2", "3"]:
                spell_index = int(choix_attaque) - 1
                selected_spell = classes_attackes[classe_joueur.lower()][spell_index]
                hp_monstre = selected_spell(hp_monstre, nom_joueur)
            else:
                print ("Choix invalide, essayez de nouveau.")
                continue

            if hp_monstre <= 0:
                print (f"Le {nom_monstre} est vaincu !")
                break
            elif hp_joueur <=0:
                 print (f"{nom_joueur} est vaincu ! Game Over.")
                 break
            
            hp_joueur -= poule_attaque(hp_joueur)
    return hp_joueur
        