# Arbre binaire de recherche (BST)
class Noeud:

    def __init__(self, valeur):
        # La valeur contenu dans ce noeud d'arbre
        self.__valeur = valeur
        # Le fils de gauche (sera un objet de type Noeud ou None)
        self.__gauche = None
        # Le fils de droite (sera un objet de type Noeud ou None)
        self.__droite = None

    # Getter
    @property
    def valeur(self):
        return self.__valeur

    # Méthode qui insère en effectuant un tri
    # La méthode insertion permet de se comparer (self->noeud courant) avec le noeud que l'on veut inséré (celui en
    # paramètre)
    def insertion(self, noeud):
        # Si le noeud que l'on veut insérer est plus petit que le noeud courant
        if noeud.valeur < self.valeur:
            # Si le fils de gauche n'existe pas, le noeud à inséré devient le fils gauche
            if self.__gauche is None:
                self.__gauche = noeud
            # Si existant, on appelle la méthode insertion() sur le fils de gauche
            else:
                self.__gauche.insertion(noeud)
        # Si le noeud que l'on veut insérer est plus grand que le noeud courant
        else:
            # Si le fils de gauche n'existe pas, le noeud à inséré devient le fils droit
            if self.__droite is None:
                self.__droite = noeud
            # Si existant, on appelle la méthode insertion() sur le fils de droit
            else:
                self.__droite.insertion(noeud)

    # On effectue une recherche en profondeur. Le résultat donnera la liste des valeurs triées en ordre croissant<
    def afficher(self):
        # Si un fils gauche existe, on le visite en appelant afficher()
        if self.__gauche is not None:
            self.__gauche.afficher()
        #  On s'imprime
        print(str(self.valeur))
        # Si un fils droit existe on le visite en appelant afficher()
        if self.__droite is not None:
            self.__droite.afficher()


# Début du programme
# Liste des items à insérer
items = [6, 8, 2, 4, 0, 7, 3, 9]
# La racine n'existe pas encore
racine = None
# On parcourt la liste des items pour les insérer, un par un, par la racine
for item in items:
    # Si aucune racine existe, le noeud devient la racine
    if racine is None:
        # On créé le noeud racine en appelant le constructeur de Noeud avec l'item en paramètre. Le noeud va contenir
        # l'item
        racine = Noeud(item)
    # Sinon, on l'insère par la racine (en créer un Noeud) en appelant la méthode insertion(self, nouveau_noeud)
    else:
        racine.insertion(Noeud(item))
# L'on affiche les items triés en effectuant une recherche en profondeur.
racine.afficher()

