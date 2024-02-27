from datetime import date


class Personne:

    # variable de classe
    nom_drapeau = "Apatride"

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    @classmethod
    def set_drapeau_pour_tous(cls, nom_drapeau):
        cls.nom_drapeau = nom_drapeau

    @classmethod
    def from_annee_naissance(cls, nom, annee):
        return cls(nom, date.today().year - annee)

    @staticmethod
    def est_adulte(age):
        return age > 18


alice = Personne('Alice', 19)
print(alice.nom_drapeau)
bob = Personne.from_annee_naissance('Bob', 1990)
print(Personne.est_adulte(bob.age))
# Peut être appelé sur la classe
Personne.set_drapeau_pour_tous("Fleurdelysé")
# Peut être appelé sur une instance (objet)
bob.set_drapeau_pour_tous("Fleurdelysé")
print(alice.nom_drapeau)
print(bob.nom_drapeau)
