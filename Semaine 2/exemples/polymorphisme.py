class Animal:

    def bouger(self):
        print("Un animal qui bouge")


# Chien hérite de Animal
# La classe va hériter de tous les attributs (variables et méthodes) de la classe Animal
class Chien(Animal):
    pass


# Oiseau hérite de Animal
# La classe va hériter de tous les attributs (variables et méthodes) de la classe Animal
class Oiseau(Animal):

    # Red.finition du comportement de la méthode bouger(self) qui a été héritée
    def bouger(self):
        print("Un oiseau qui vole")


chien = Chien()
chien.bouger()

oiseau = Oiseau()
oiseau.bouger()