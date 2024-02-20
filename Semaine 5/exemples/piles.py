class Pile:

    def __init__(self):
        self.__pile = []

    def entree(self, nom):
        self.__pile.append(nom)
        print('Entrer dans la fonction ' + nom)

    def sortie(self):
        print('Sortie de ' + self.__pile.pop())


pile = Pile()


def fonction1():
    pile.entree('fonction1')
    fonction2(0)
    pile.sortie()


def fonction2(index):
    pile.entree('fonction2 + idx ' + str(index))
    if index < 10:
        fonction2(index +1)
    pile.sortie()


fonction1()
