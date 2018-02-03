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

    def nbVoisins(self, i, j):
        nbVoisins = 0
        couleur = self._Grille[i][j]

        '''1  8  7
           2 |x| 6
           3  4  5
        '''
        if (i != 0 & j != 0 ):
            if(self._Grille[i-1][j-1] == couleur):
                nbVoisins = nbVoisins + 1

        if(j != 0):
            if(self._Grille[i][j-1] == couleur):
                nbVoisins = nbVoisins + 1

        if(i < len(self._Grille) & j != 0):
            if(self._Grille[i+1][j-1] == couleur):
                nbVoisins = nbVoisins + 1

        if(i < len(self._Grille)):
            if(self._Grille[i+1][j] == ''):
                nbVoisins = nbVoisins + 1

        if(i < len(self._Grille) & j < len(self._Grille[i])):
            if(self._Grille[i+1][j+1]] == ''):
                nbVoisins = nbVoisins + 1

        if(j < len(self._Grille[i])):
            if(self._Grille[i][j+1] == ''):
                nbVoisins = nbVoisins + 1

        if(i != 0 & j < len(self._Grille[i])):
            if(self._Grille[i-1][j+1] == ''):
                nbVoisins = nbVoisins + 1

        if(i != 0):
            if(self._Grille[i-1][j] == ''):
                nbVoisins = nbVoisins + 1

        return nbVoisins


    def regle(self, nb_etapes, regles):
    '''On balaye le tableau au complet un nombre nb_etapes de fois'''
        for i in range(len(self._Grille)):
            for j in range(len(self._Grille[i])):

                '''Si la cellule du tableau est vide, on regarde si elle peut naitre (a), dans le bon ordre (B-Y-R-G)'''
                if (self._Grille[i][j] == '.'):
                    '''Enlever l'ordre pré-défini'''
                    for k in range(0, len(regles)):
                        if (self.nbVoisins(i,j) >= int(regles[k].split(',')[1]):
                            self._Grille[i][j]= str(regles[k].split(':')[0])

                '''Si la cellule contient un organisme, on regarde s'il survit ou meurt selon les règles de l'organisme en question, soit entre b et c'''
                elif(self._Grille[i][j] == 'B'):
                    if((self._Grille[i][j].nbVoisins < int(regles[0].split(',').[0].split(':')[1]) & (self._Grille[i][j].nbVoisins > int(regles[0].split(',').[2]) ):
                        self._Grille[i][j] = '.'

                elif(self._Grille[i][j] == 'Y'):
                    if((self._Grille[i][j].nbVoisins < int(regles[1].split(',').[0].split(':')[1]) & (self._Grille[i][j].nbVoisins > int(regles[1].split(',').[2]) ):
                        self._Grille[i][j] = '.'

                elif(self._Grille[i][j] == 'R'):
                    if((self._Grille[i][j].nbVoisins < int(regles[2].split(',').[0].split(':')[1]) & (self._Grille[i][j].nbVoisins > int(regles[2].split(',').[2]) ):
                        self._Grille[i][j] = '.'

                else(self._Grille[i][j] == 'G'):
                    if((self._Grille[i][j].nbVoisins < int(regles[3].split(',').[0].split(':')[1]) & (self._Grille[i][j].nbVoisins > int(regles[3].split(',').[2]) ):
                        self._Grille[i][j] = '.'


'''
____________________

'''
    Fichier : Classe self._Grille
    Projet  : TP0
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

class self._Grille:

    def __init__(self, i, j):
        self._self._Grille = [['.' for x in range(j)] for y in range(i)]

    def imprimer(self):
        for i in range(len(self._self._Grille)):
            for j in range(len(self._self._Grille[i])):
                print(' ' + self._self._Grille[i][j], end='')
            print()
        print('\n\n\n\n\n')

    def initialiser(self, config):
        for i in range(1, len(config)):
            k = config[i].split(',')
            self._self._Grille[int(k[1])][int(k[2])] = k[0]

    def nbVoisins(self, i, j):
        nbVoisins = 0
        '''1  8  7
           2 |x| 6
           3  4  5
        '''
        if (i != 0 & j != 0 ):
            if(self._Grille[i-1][j-1] == ''):
                nbVoisins = nbVoisins + 1

        if(j != 0):
            if(self._Grille[i][j-1] == ''):
                nbVoisins = nbVoisins + 1

        if(i < len(self._Grille) & j != 0):
            if(self._Grille[i+1][j-1] == ''):
                nbVoisins = nbVoisins + 1

        if(i < len(self._Grille)):
            if(self._Grille[i+1][j] == ''):
                nbVoisins = nbVoisins + 1

        if(i < len(self._Grille) & j < len(self._Grille[i])):
            if(self._Grille[i+1][j+1]] == ''):
                nbVoisins = nbVoisins + 1

        if(j < len(self._Grille[i])):
            if(self._Grille[i][j+1] == ''):
                nbVoisins = nbVoisins + 1

        if(i != 0 & j < len(self._Grille[i])):
            if(self._Grille[i-1][j+1] == ''):
                nbVoisins = nbVoisins + 1

        if(i != 0):
            if(self._Grille[i-1][j] == ''):
                nbVoisins = nbVoisins + 1



    def regle(nb_etapes, regles):
    '''On balaye le tableau au complet un nombre nb_etapes de fois'''
        for i in range(len(self._self._Grille)):
            for j in range(len(self._self._Grille[i])):

                '''Si la cellule du tableau est vide, on regarde si elle peut naitre (a), dans le bon ordre (B-Y-R-G)'''
                if (self._Grille[i][j] == '. '):
                    for k in range(0, len(regles)):
                        if (self._Grille[i][j].nbVoisins >= int(regles[k].split(',')[1]):
                            self._Grille[i][j]= str(regles[k].split(':')[0])

                '''Si la cellule contient un organisme, on regarde s'il survit ou meurt selon les règles de l'organisme en question, soit entre b et c'''
                elif(self._Grille[i][j] == 'B'):
                    if((self._Grille[i][j].nbVoisins < int(regles[0].split(',').[0].split(':')[1]) & (self._Grille[i][j].nbVoisins > int(regles[0].split(',').[2]) ):
                        self._Grille[i][j] = '. '

                elif(self._Grille[i][j] == 'Y'):
                    if((self._Grille[i][j].nbVoisins < int(regles[1].split(',').[0].split(':')[1]) & (self._Grille[i][j].nbVoisins > int(regles[1].split(',').[2]) ):
                        self._Grille[i][j] = '. '

                elif(self._Grille[i][j] == 'R'):
                    if((self._Grille[i][j].nbVoisins < int(regles[2].split(',').[0].split(':')[1]) & (self._Grille[i][j].nbVoisins > int(regles[2].split(',').[2]) ):
                        self._Grille[i][j] = '. '

                else(self._Grille[i][j] == 'G'):
                    if((self._Grille[i][j].nbVoisins < int(regles[3].split(',').[0].split(':')[1]) & (self._Grille[i][j].nbVoisins > int(regles[3].split(',').[2]) ):
                        self._Grille[i][j] = '. '
