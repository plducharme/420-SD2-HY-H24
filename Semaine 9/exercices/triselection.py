from typing import List

from molecule import Molecule
from tri import Tri


class TriSelection(Tri):

    def __init__(self):
        super().__init__("Tri par Sélection")

    def trier(self, liste_molecules: List[Molecule]) -> List[Molecule]:
        pass

