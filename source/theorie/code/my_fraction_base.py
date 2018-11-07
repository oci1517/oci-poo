# fichier my_fractions.py
# auteur : Cédric Donner

# Description : fichier de base pour l'exercice 4.4 sur les fractions
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n



class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    
    def __str__(self):
        # à compléter

    def __repr__(self):
        # à compléter
        pass

    # Par convention, les méthodes qui commencent par un caractère de
    # soulignement ne devraient pas etre appelées depuis l'extérieur
    # de la classe ... On parle de méthode privée
    
    def _reduce(self):
        '''

        Cette méthode réduit la fraction à une fraction irréductible.
        Méthode privée : à ne pas appeler depuis l'extérieur de la
        classe.

        '''
        pass
