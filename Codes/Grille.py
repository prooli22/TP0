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




    def regle(nb_etapes, regles):
    '''On balaye le tableau au complet un nombre nb_etapes de fois'''
        for i in range(len(self._Grille)):
            for j in range(len(self._Grille[i])):

                '''Si la cellule du tableau est vide, on regarde si elle peut naitre (a), dans le bon ordre (B-Y-R-G)'''
                if (Grille[i][j] == '. '):
                    for k in range(0, len(regles)):
                        if (Grille[i][j].nbVoisins >= int(regles[k].split(',')[1]):
                            Grille[i][j]= str(regles[k].split(':')[0])

                '''Si la cellule contient un organisme, on regarde s'il survit ou meurt selon les règles de l'organisme en question, soit entre b et c'''
                elif(Grille[i][j] == 'B'):
                    if((Grille[i][j].nbVoisins < int(regles[0].split(',').[0].split(':')[1]) & (Grille[i][j].nbVoisins > int(regles[0].split(',').[2]) ):
                        Grille[i][j] = '. '

                elif(Grille[i][j] == 'Y'):
                    if((Grille[i][j].nbVoisins < int(regles[1].split(',').[0].split(':')[1]) & (Grille[i][j].nbVoisins > int(regles[1].split(',').[2]) ):
                        Grille[i][j] = '. '

                elif(Grille[i][j] == 'R'):
                    if((Grille[i][j].nbVoisins < int(regles[2].split(',').[0].split(':')[1]) & (Grille[i][j].nbVoisins > int(regles[2].split(',').[2]) ):
                        Grille[i][j] = '. '

                else(Grille[i][j] == 'G'):
                    if((Grille[i][j].nbVoisins < int(regles[3].split(',').[0].split(':')[1]) & (Grille[i][j].nbVoisins > int(regles[3].split(',').[2]) ):
                        Grille[i][j] = '. '
