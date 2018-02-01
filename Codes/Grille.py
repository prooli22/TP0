'''
    Fichier : Classe Grille
    Projet  : TP0
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

class Grille:

    def __init__(self, i, j):
        self._Grille = [['.' for x in range(j)] for y in range(i)]

    def imprimer(self):
        for i in range(len(self._Grille)):
            for j in range(len(self._Grille[i])):
                print(' ' + self._Grille[i][j], end='')
            print()
        print('\n\n\n\n\n')

    def initialiser(self, config):
        for i in range(1, len(config)):
            k = config[i].split(',')
            self._Grille[int(k[1])][int(k[2])] = k[0]
