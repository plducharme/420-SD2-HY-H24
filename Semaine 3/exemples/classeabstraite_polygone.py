from abc import ABC, abstractmethod


class Polygone(ABC):

    # Méthode abstraite qui devra être implémenté dans une sous-classe
    @abstractmethod
    def afficher_nb_cotes(self):
        pass


class Carre(Polygone):
    # Implémentation de la méthode abstraite
    def afficher_nb_cotes(self):
        print('Carre ' + str(4))

class Triangle(Polygone):
    # Implémentation de la méthode abstraite
    def afficher_nb_cotes(self):
        print('Triangle ' + str(3))


triangle = Triangle()
carre = Carre()

polys = [triangle, carre]

# Code générique car Triangle et Carre doivent implémenter afficher_nb_cotes(self)
for poly in polys:
    poly.afficher_nb_cotes()

