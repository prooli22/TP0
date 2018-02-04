'''
    Fichier : Classe Organisme
    Projet  : TP0
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

from termcolor import colored, cprint

class Organisme:

    def __init__(self):
        self.B = 'B'
        self.Y = 'Y'
        self.R = 'R'
        self.G = 'G'
        self.Vide = '.'

        self.cB = colored('#', 'blue')
        self.cY = colored('#', 'yellow')
        self.cR = colored('#', 'red')
        self.cG = colored('#', 'green')


