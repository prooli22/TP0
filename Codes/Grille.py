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
                print(' ' + self._Grille[i][j], end='')
            print()
        print('\n\n\n\n\n')

    def initialiser(self, config):
        for i in range(1, len(config)):
            k = config[i].split(',')
            self._Grille[int(k[1])][int(k[2])] = k[0]

    def _nbVoisins(self, i, j, couleur):
        nb_voisins = 0

        '''1  8  7
           2 |x| 6
           3  4  5
        '''
        if (i != 0 & j != 0 ):
            if(self._Grille[i-1][j-1] == couleur):
                nb_voisins += 1

        if(j != 0):
            if(self._Grille[i][j-1] == couleur):
                nb_voisins += 1

        if(i < len(self._Grille) & j != 0):
            if(self._Grille[i+1][j-1] == couleur):
                nb_voisins += 1

        if(i < len(self._Grille)):
            if(self._Grille[i+1][j] == couleur):
                nb_voisins += 1

        if(i < len(self._Grille) & j < len(self._Grille[i])):
            if(self._Grille[i+1][j+1]] == couleur):
                nb_voisins += 1

        if(j < len(self._Grille[i])):
            if(self._Grille[i][j+1] == couleur):
                nb_voisins += 1

        if(i != 0 & j < len(self._Grille[i])):
            if(self._Grille[i-1][j+1] == couleur):
                nb_voisins += 1

        if(i != 0):
            if(self._Grille[i-1][j] == couleur):
                nb_voisins += 1

        return nb_voisins

    def simulation(self, regles):
        '''On balaye le tableau au complet un nombre nb_etapes de fois'''
        for i in range(len(self._Grille)):
            for j in range(len(self._Grille[i])):

                nb_voisins = self._nbVoisins(i,j)
                '''Si la cellule du tableau est vide, on regarde si elle peut naitre (a), 
                   dans le bon ordre (B-Y-R-G)
                   '''
                if (self._Grille[i][j] == '.'):
                    '''Enlever l'ordre pré-défini'''
                    for k in range(0, len(regles)):
                        if (nb_voisins >= int(regles[k].split(',')[1]):
                            self._Grille[i][j]= str(regles[k].split(':')[0])

                '''Si la cellule contient un organisme, on regarde s'il survit ou meurt selon 
                   les règles de l'organisme en question, soit entre b et c
                '''
                elif(self._Grille[i][j] == 'B'):
                    if((nb_voisins < int(regles[0].split(',').[0].split(':')[1]) & (nb_voisins > int(regles[0].split(',').[2]) ):
                        self._Grille[i][j] = '.'

                elif(self._Grille[i][j] == 'Y'):
                    if((nb_voisins < int(regles[1].split(',').[0].split(':')[1]) & (nb_voisins > int(regles[1].split(',').[2]) ):
                        self._Grille[i][j] = '.'

                elif(self._Grille[i][j] == 'R'):
                    if((nb_voisins < int(regles[2].split(',').[0].split(':')[1]) & (nb_voisins > int(regles[2].split(',').[2]) ):
                        self._Grille[i][j] = '.'

                else(self._Grille[i][j] == 'G'):
                    if((nb_voisins < int(regles[3].split(',').[0].split(':')[1]) & (nb_voisins > int(regles[3].split(',').[2]) ):
                        self._Grille[i][j] = '.'
        return

    def simulation_test(self, regles):
        '''On balaye le tableau au complet un nombre nb_etapes de fois'''
        for i in range(len(self._Grille)):
            for j in range(len(self._Grille[i])):

                '''Si la cellule du tableau est vide, on regarde si elle peut naitre (a), 
                   dans le bon ordre (B-Y-R-G)'''
                if (self._Grille[i][j] == self.organisme.Morte):
                    # Organisme Blue
                    if (self._nbVoisins(i, j, self.organisme.B) >= regles.B.a):
                        self._Grille[i][j] = self.organisme.B)

                    # Organisme Yellow
                    elif(self._nbVoisins(i, j, self.organisme.Y) >= regles.Y.a)
                        self._Grille[i][j] = self.organisme.Y)

                    # Orgamisme Red
                    elif(self._nbVoisins(i, j, self.organisme.R) >= regles.R.a)
                        self._Grille[i][j] = self.organisme.R)

                    # Orgasnisme Green
                    elif(self._nbVoisins(i, j, self.organisme.G) >= regles.G.a)
                        self._Grille[i][j] = self.organisme.G)

                '''Si la cellule contient un organisme, on regarde s'il survit ou meurt selon 
                   les règles de l'organisme en question, soit entre b et c'''
                else:

                    # On met la couleur dans une variable pour ne pas l'accéder à chaque fois
                    couleur = self._Grille[i][j]

                    # Organisme Blue                    
                    if(couleur == self.organisme.B):
                        nb_voisinsB = self._nbVoisins(i, j, couleur)
                        if(nb_voisins < regles.B.b & nb_voisins > regles.B.c):
                            self._Grille[i][j] = self.organisme.Morte
                    
                    # Organisme Yellow
                    elif(couleur == self.organisme.Y):
                        nb_voisinsY = self._nbVoisins(i, j, couleur)
                        if(nb_voisins < regles.Y.b & nb_voisins > regles.Y.c):
                            self._Grille[i][j] = self.organisme.Morte

                    # Orgamisme Red
                    elif(couleur == self.organisme.R):
                        nb_voisinsR = self._nbVoisins(i, j, couleur)
                        if(nb_voisins < regles.R.b & nb_voisins > regles.R.c):
                            self._Grille[i][j] = self.organisme.Morte

                    # Orgasnisme Green
                    elif(couleur == self.organisme.G):
                        nb_voisinsG = self._nbVoisins(i, j, couleur)
                        if(nb_voisins < regles.G.b & nb_voisins > regles.G.c):
                            self._Grille[i][j] = self.organisme.Morte