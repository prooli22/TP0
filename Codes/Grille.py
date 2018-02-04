'''
    Fichier : Classe Grille
    Projet  : TP0
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

from Organisme import Organisme

class Grille:

    organisme = Organisme()

    def __init__(self, i, j):
        self._Grille = [['.' for x in range(j)] for y in range(i)]

    def imprimer(self):
        for i in range(len(self._Grille)):
            for j in range(len(self._Grille[i])):
                print(self._Grille[i][j] + ' ', end='')
            print()
        #print('\n\n\n\n\n')

    def initialiser(self, config):
        for i in range(1, len(config)):
            k = config[i].split(',')
            self._Grille[int(k[1])][int(k[2])] = k[0]

    def _nbVoisins(self, i, j):
        nb_voisins = 0

        '''1  8  7
           2 |x| 6
           3  4  5
        '''

        if(i > 0 and j > 0):
            if(self._Grille[i - 1][j - 1] != self.organisme.Mort):
                nb_voisins += 1

        if(j > 0):
            if(self._Grille[i][j - 1] != self.organisme.Mort):
                nb_voisins += 1

        if(i < len(self._Grille) - 1 and j > 0):
            if(self._Grille[i + 1][j - 1] != self.organisme.Mort):
                nb_voisins += 1

        if(i < len(self._Grille) - 1):
            if(self._Grille[i + 1][j] != self.organisme.Mort):
                nb_voisins += 1

        if(i < len(self._Grille) - 1 and j < len(self._Grille[i]) - 1):
            if(self._Grille[i + 1][j + 1] != self.organisme.Mort):
                nb_voisins += 1

        if(j < len(self._Grille[i]) - 1):
            if(self._Grille[i][j + 1] != self.organisme.Mort):
                nb_voisins += 1

        if(i > 0 and j < len(self._Grille[i]) - 1):
            if(self._Grille[i - 1][j + 1] != self.organisme.Mort):
                nb_voisins += 1

        if(i > 0):
            if(self._Grille[i - 1][j] != self.organisme.Mort):
                nb_voisins += 1

        return nb_voisins

    def simulation(self, regles):
        '''On balaye le tableau au complet un nombre nb_etapes de fois'''
        for i in range(len(self._Grille)):
            for j in range(len(self._Grille[i])):

                nb_voisins = self._nbVoisins(i, j)

                '''Si la cellule du tableau est vide, on regarde si elle peut naitre (a), 
                   dans le bon ordre (B-Y-R-G)'''
                if (self._Grille[i][j] == self.organisme.Mort):
                    # Organisme Blue
                    if (nb_voisins >= regles.B.a):
                        self._Grille[i][j] = self.organisme.B

                    # Organisme Yellow
                    elif (nb_voisins >= regles.Y.a):
                        self._Grille[i][j] = self.organisme.Y

                    # Orgamisme Red
                    elif (nb_voisins >= regles.R.a):
                        self._Grille[i][j] = self.organisme.R

                    # Orgasnisme Green
                    elif (nb_voisins >= regles.G.a):
                        self._Grille[i][j] = self.organisme.G

                else:
                    '''Si la cellule contient un organisme, on regarde s'il survit ou meurt selon 
                       les règles de l'organisme en question, soit entre b et c'''

                    # On met la couleur dans une variable pour ne pas l'accéder à chaque fois
                    couleur = self._Grille[i][j]

                    # Organisme Blue                    
                    if (couleur == self.organisme.B):
                        if(nb_voisins <= regles.B.b or nb_voisins > regles.B.c):
                            self._Grille[i][j] = self.organisme.Mort
                    
                    # Organisme Yellow
                    elif (couleur == self.organisme.Y):
                        if(nb_voisins <= regles.Y.b or nb_voisins > regles.Y.c):
                            self._Grille[i][j] = self.organisme.Mort

                    # Orgamisme Red
                    elif (couleur == self.organisme.R):
                        if(nb_voisins <= regles.R.b or nb_voisins > regles.R.c):
                            self._Grille[i][j] = self.organisme.Mort

                    # Orgasnisme Green
                    elif (couleur == self.organisme.G):
                        if(nb_voisins <= regles.G.b or nb_voisins > regles.G.c):
                            self._Grille[i][j] = self.organisme.Mort