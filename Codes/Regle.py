'''
    Fichier : Classe Regle
    Projet  : TP0
    Cours   : IFT2015 - Stuctures de données
    Auteurs : Olivier Provost (20101738)
              Moïka Sauvé     (20090119)
'''

class Regle:
    def __init__(self, regle):
        self.a = int(regle.split(',')[0].split(':')[1])
        self.b = int(regle.split(',')[1])
        self.c = int(regle.split(',')[2])

class Regles:
    def __init__(self, regles):

        for k in range(len(regles)):
            if(regles[k].split(',')[0].split(':')[0] == 'B'):
                self.B = Regle(regles[k])

            if(regles[k].split(',')[0].split(':')[0] == 'Y'):
                self.Y = Regle(regles[k])

            if(regles[k].split(',')[0].split(':')[0] == 'R'):
                self.R = Regle(regles[k])

            if(regles[k].split(',')[0].split(':')[0] == 'G'):
                self.G = Regle(regles[k])
