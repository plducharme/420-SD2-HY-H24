# class indique que l'on déclare une classe suivie du nom de la classe
class Voiture:

    # Variable de classe, variable qui est commune à tous les objets instanciés de cette classe, existe au niveau de la
    # classe
    nombre_de_roues = 4

    def __init__(self, marque, modele):
        # déclaration de variables d'instance (ex: self.marque) et assignation à ce qui est passé en paramètres
        # (ex: marque)
        self.marque = marque
        self.modele = modele

    def vroom(self):
        # impression des variables d'instance
        print(self.marque + "\t" + self.modele + "\tvroom!")


# Création d'une instance de la classe en appelant le constructeur __init__(self, marque. modele)
challenger = Voiture("Dodge", "Challenger")
# appel d'une méthode de l'objet
challenger.vroom()
