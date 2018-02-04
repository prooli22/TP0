'''
    Fichier : main
    Projet  : TP0
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

import sys
from termcolor import colored, cprint
from Grille import Grille
from Regle import Regles

def main():

    animation = False
    couleur = False

    try:
        if(sys.argv[1] == '-animation'):
            animation = True

        elif(sys.argv[1] == '-couleur'):
            couleur = True
        
        else:
            nb_etapes = int(sys.argv[1])

    except IndexError:
        print("Veuillez entrer un argument avant l'exécution, fin du programme.")
        return

    # Pour les tests      
    #nb_etapes = int(open('arg.txt', 'r').read())

    config = open('config.txt', 'r').read().splitlines()
    regles = open('rules.txt', 'r').read().splitlines()

    hauteur = int(config[0].split(',')[0])
    largeur = int(config[0].split(',')[1])

    grille = Grille(hauteur, largeur)
    grille.initialiser(config)
    regle = Regles(regles)

    if(animation or couleur):
        while(True):
            grille.simulation(regle)
            grille.imprimer(couleur)
            input('\nAppuyez sur la touche <Enter> pour simuler une autre étape ...')
            print('\n\n\n\n\n')

    else:
        for sim in range(nb_etapes):
            grille.simulation(regle)
    
        grille.imprimer(couleur)

main()

# Pour les tests
def test(arg):
    main()