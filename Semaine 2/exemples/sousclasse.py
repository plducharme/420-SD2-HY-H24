# Si aucun héritage est défini, la classe hérite implicitement de object
# class Parent(object)
class Parent:

    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

    # Méthode retournant le nom
    def get_nom(self):
        return self._nom


class Enfant(Parent):
    # Pour cet exemple, on va mettre pass pour indiquer une implémentation vide
    # La classe Enfant va hériter les méthodes et les attributs de la classe Parent
    pass


enfant = Enfant("Beauregard", "Alice")
print(enfant.get_nom())
