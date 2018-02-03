'''
    Fichier : Classe Grille
    Projet  : TP0
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''
import sys
from Grille import Grille


class Cellule:

    def__init__(Grille, x, y):
        self._Cellule = Grille[x][y]


    def isEmpty(self):
        if self._Cellule == '.':
            return true
        else:
            return false
s
    def imprimer(x, y):
        print (cellule[x][y])
