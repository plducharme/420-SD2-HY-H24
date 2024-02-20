# Arbre binaire de base
class Noeud:

    def __init__(self, valeur):
        self.__valeur = valeur
        self.__gauche = None
        self.__droite = None

    @property
    def valeur(self):
        return self.__valeur

    def insertion(self, noeud):
        if noeud.valeur < self.valeur:
            if self.__gauche is None:
                self.__gauche = noeud
            else:
                self.__gauche.insertion(noeud)
        else:
            if self.__droite is None:
                self.__droite = noeud
            else:
                self.__droite.insertion(noeud)

    def afficher(self):
        if self.__gauche is not None:
            self.__gauche.afficher()
        print(str(self.valeur))
        if self.__droite is not None:
            self.__droite.afficher()


items = [6, 8, 2, 4, 0, 7, 3, 9]
racine = None
for i in items:
    if racine is None:
        racine = Noeud(i)
    else:
        racine.insertion(Noeud(i))
racine.afficher()

