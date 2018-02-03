'''
    Fichier : Classe Grille
    Projet  : TP0
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''
class Regle:

    __init__(self, regles):
    for i in range(0, len(regles)):
        regleDict = {str(regles[i].split(':')[0]) : {"a": int(regle[i].split(',')[1])},
                           {"b" : int(regles[i].split(',')[0].split(':')[1])},
                           {"c"}: int(regles[i].split(',')[2])}
                    }
