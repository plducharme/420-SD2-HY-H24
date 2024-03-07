# Si aucun héritage est défini, la classe hérite implicitement de object
# class Parent(object)
class Parent:

    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

    # Méthode retournant le nom
    def get_nom(self):
        return self.get_nom()


class Enfant(Parent):

    # Redéfinition du constructeur hérité
    def __init__(self, nom, prenom, nom_parent):
        # appelle au constructeur de la classe Parent au lieu de réécrire le même code que le constructeur du parent
        super().__init__(nom, prenom)
        self._nom_parent = nom_parent

    # redéfinition de la méthode héritée de la classe Parent
    def get_nom(self):
        return self._nom + ", enfant de " + self._nom_parent


enfant = Enfant("Beauregard", "Alice", "Jeanne Lambert")
print(enfant.get_nom())
