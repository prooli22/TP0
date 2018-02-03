'''
    Fichier : main
    Projet  : TP0
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

import sys
from Grille import Grille
from Regle import Regles

def main():
    # S'il n'y a pas d'arguments on met 10 par défaut.
    try:
        nb_etapes = int(sys.argv[1])
    except IndexError:
        nb_etapes = 10

    config = open('config.txt', 'r').read().splitlines()
    regles = open('rules.txt', 'r').read().splitlines()

    hauteur = int(config[0].split(',')[0])
    largeur = int(config[0].split(',')[1])

    grille = Grille(hauteur, largeur)
    regle = Regles(regles)
    
    grille.initialiser(config)

    for sim in range(nb_etapes):
        grille.simulation(regle)
    
    grille.imprimer()

main()
