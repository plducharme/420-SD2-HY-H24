from typing import List


class Cours:

    def __init__(self, nom: str, duree_cours: int, duree_lab: int, duree_travaux: int):
        self._nom = nom
        self._duree_cours = duree_cours
        self._duree_lab = duree_lab
        self._duree_travaux = duree_travaux

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom: str):
        self._nom = nom

    @property
    def duree_cours(self) -> int:
        return self._duree_cours

    @duree_cours.setter
    def duree_cours(self, duree_cours: int):
        self._duree_cours = duree_cours

    @property
    def duree_lab(self) -> int:
        return self._duree_lab

    @duree_lab.setter
    def duree_lab(self, duree_lab: int):
        self._duree_lab = duree_lab

    @property
    def duree_travaux(self) -> int:
        return self._duree_travaux

    @duree_travaux.setter
    def duree_travaux(self, duree_travaux: int):
        self._duree_travaux = duree_travaux

    def __repr__(self):
        return f"{self._nom}: {self._duree_cours}/{self._duree_lab}/{self.duree_travaux}"


class Etudiant:

    def __init__(self, nom: str, prenom: str, no_da: int, cours: List[Cours]):
        self._nom = nom
        self._prenom = prenom
        self._no_da = no_da
        self._cours: List[Cours] = cours

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, nom: str):
        self._nom = nom

    @property
    def no_da(self) -> int:
        return self._no_da

    @no_da.setter
    def no_da(self, no_da: int):
        self._no_da = no_da

    @property
    def prenom(self) -> str:
        return self._prenom

    @prenom.setter
    def prenom(self, prenom: str):
        self._prenom = prenom

    @property
    def cours(self) -> List[Cours]:
        return self._cours

    @cours.setter
    def cours(self, cours: List[Cours]):
        self._cours = cours

    def __repr__(self):
        return f"{self._nom} {self._prenom} / {self._no_da} :\n{self.cours}"
