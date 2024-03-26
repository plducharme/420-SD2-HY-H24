class Molecule:
    def __init__(self, nom, formule_chimique, masse_moleculaire):
        self.__nom = nom
        self.__formule_chimique = formule_chimique
        self.__masse_moleculaire = masse_moleculaire

    @property
    def nom(self):
        return self.__nom

    @property
    def formule_chimique(self):
        return self.__formule_chimique

    @property
    def masse_moleculaire(self):
        return self.__masse_moleculaire

    def __repr__(self):
        return self.__nom + "{" + self.__formule_chimique + " | " + str(self.__masse_moleculaire) + "}"
