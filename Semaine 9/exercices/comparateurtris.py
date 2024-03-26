from typing import List, Dict
import csv
from tri import Tri
from trirapide import TriRapide
from triinsertion import TriInsertion
from trifusion import TriFusion
from triselection import TriSelection
from tribulle import TriBulle
from trishell import TriShell

from molecule import Molecule


from visualisateurresultats import VisualisateurResultats
from PySide6.QtWidgets import QApplication


class DataUtils:

    @staticmethod
    def charger_molecules() -> List[Molecule]:
        molecules: List[Molecule] = []
        with open("./data/masses-moléculaires.csv", "r", encoding="UTF-8") as fichier:
            lecteur_csv = csv.reader(fichier, delimiter=";")
            for ligne in lecteur_csv:
                try:
                    molecules.append(Molecule(ligne[0], ligne[1], float(ligne[2].split(" ")[0])))
                except Exception as e:
                    raise Exception("Erreur lors du parsing de la ligne: " + str(ligne))

        return molecules

    @staticmethod
    def listes_molecules(nombre_elements):
        molecules = DataUtils.charger_molecules()
        return molecules[0: nombre_elements]


class Comparateur:

    def __init__(self, tris):
        self.__resultats = {}
        self.__tris: List[Tri] = tris

    def executer_comparaisons(self, nombre_elements):
        resultats_execution = {}
        for tri in self.__tris:
            print(f"\nListe originale avant d'effectuer le {tri.nom} avec {nombre_elements} éléments")
            liste = DataUtils.listes_molecules(nombre_elements)
            print(liste)
            tri.debut()
            liste_triee = tri.trier(liste)
            tri.fin()
            print(f"Liste résultante après le {tri.nom} avec {nombre_elements} éléments")
            print(liste_triee)

            resultats_execution[tri.nom] = tri.temps_execution()
        self.__resultats[nombre_elements] = resultats_execution

    @property
    def resultats(self) -> Dict:
        return self.__resultats


# Vous pouvez ajouter n'importe quel tri implémentant la classe abstraite Tri à cette liste
comparateur = Comparateur([TriRapide(), TriInsertion(), TriFusion(), TriSelection(), TriBulle(), TriShell()])

comparateur.executer_comparaisons(9)
comparateur.executer_comparaisons(20)
comparateur.executer_comparaisons(75)
comparateur.executer_comparaisons(150)
comparateur.executer_comparaisons(225)
comparateur.executer_comparaisons(300)
comparateur.executer_comparaisons(375)
comparateur.executer_comparaisons(460)

app = QApplication()
vr = VisualisateurResultats(comparateur.resultats)
vr.show()
app.exec()











