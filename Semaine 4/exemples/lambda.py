def mult(n):
    return lambda x: x * n


doubleur = mult(2)
print(doubleur(4))

tripleur = mult(3)
print(tripleur(4))

carre = lambda v: v * v
print(carre(4))


class Personne:
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    @property
    def nom(self):
        return self.__nom

    @property
    def age(self):
        return self.__age


anna = Personne('Anna', 18)
bernard = Personne('Bernard', 16)
carla = Personne('Carla', 21)

personnes = [anna, bernard, carla]
personnes.sort(key=lambda x: x.age, reverse=True)
for personne in personnes:
    print(personne.nom + '\t' + str(personne.age))
