from typing import List

from molecule import Molecule
from tri import Tri


class TriFusion(Tri):

    def __init__(self):
        super().__init__("Tri Fusion")

    def trier(self, liste_molecules: List[Molecule]) -> List[Molecule]:
        pass