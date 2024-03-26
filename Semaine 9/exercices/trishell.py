from typing import List

from molecule import Molecule
from tri import Tri


class TriShell(Tri):

    def __init__(self):
        super().__init__("Tri Shell")

    def trier(self, liste_molecules: List[Molecule]) -> List[Molecule]:
        pass