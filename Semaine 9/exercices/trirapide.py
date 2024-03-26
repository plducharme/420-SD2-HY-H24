from typing import List
from molecule import Molecule
from tri import Tri


class TriRapide(Tri):

    def __init__(self):
        super().__init__("Tri Rapide")

    def trier(self, liste_molecules: List[Molecule]):
        TriRapide.tri_rapide(liste_molecules, 0, len(liste_molecules))
        return liste_molecules

    @staticmethod
    def tri_rapide(tableau: List[Molecule], debut: int, fin: int):
        pass

    @staticmethod
    def partition(tableau: List[Molecule], debut, fin):
        pass
