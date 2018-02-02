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
from Grille import Grille

def main():
    # S'il n'y a pas d'arguments on met 10 par défaut.
    try:
        nb_etapes = sys.argv[1]
    except IndexError:
        nb_etapes = 10

    config = open('config.txt', 'r').read().splitlines()
    regles = open('rules.txt', 'r').read().splitlines()

    hauteur = int(config[0].split(',')[0])
    largeur = int(config[0].split(',')[1])

    # À PARTIR D'ICI TU PEUX MODIFIER
    grille = Grille(hauteur, largeur)
    grille.imprimer()

    grille.initialiser(config)
    grille.imprimer()

main()
