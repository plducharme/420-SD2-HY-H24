class Fantome:
    # redéfinition d'un destructeur qui sera appelé lorsque détruit (par un appel à del ou par le ramasse-miettes)
    def __del__(self):
        print("Je suis Gozer le Destructeur!")


# Création d'un objet en appelant le constructeur par défaut
gozer = Fantome()
# appel explicite au destructeur pour détruire l'objet et libérer la mémoire
del gozer
