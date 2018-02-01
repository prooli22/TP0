'''
    Fichier : main
    Projet  : TP0
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)


from Cellule import Cellule
from Organisme import Organisme
from Regle import Regle
'''

import sys
#from Grille import Grille

def main():
    nb_etapes = sys.argv[1]
    config = open('config.txt', 'r')
    regles = open('rules.txt', 'r')

    print(config.read())
    print(regles.read())

main()
