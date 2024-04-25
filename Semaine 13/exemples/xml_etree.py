import xml.etree.ElementTree as ET
from typing import List
from etudiant import Etudiant, Cours

# Dans le cas du etree, un arbre de "Element" est construit
#
# Pour chaque Element, il y a les propriétés
# tag: le nom du tag XML
# attrib: dictionnaire des attributs du tag XML
# text: Le contenu du tag XML sous forme de string
#
#
class EtudiantETParser:

    def __init__(self):
        self._arbre = None
        self._racine = None

    def parse_etudiants(self, chemin_fichier: str) -> List[Etudiant]:
        # parse le fichier XML
        self._arbre = ET.parse(chemin_fichier)
        # Retourne la rabcine
        self._racine = self._arbre.getroot()
        liste_etudiants = []
        # iter(tag) retourne la liste des Element enfant au tag
        for etudiant in self._racine.iter("etudiant"):
            liste_etudiants.append(EtudiantETParser.handle_etudiant(etudiant))
        return liste_etudiants

    @staticmethod
    def handle_etudiant(etudiant) -> Etudiant:
        # On peut aller le chercher explicitement ou on pourrait parcourir les enfants et regarder leur "tag"
        nom = None
        prenom = None
        numero_da = None
        cours = []

        for enfant in etudiant:
            match enfant.tag:
                case "nom":
                    nom = enfant.text
                case "prenom":
                    prenom = enfant.text
                case "numeroDa":
                    numero_da = enfant.text
                case "cours":
                    cours = EtudiantETParser.handle_cours(enfant)
        return Etudiant(nom, prenom, numero_da, cours)

    @staticmethod
    def handle_cours(cours) -> List[Cours]:
        liste_cours = []
        for enfant in cours:
            cours_inscrit = Cours(nom=enfant.attrib["nom"], duree_cours=int(enfant.attrib["dureeCours"]), duree_lab=int(enfant.attrib["dureeLab"]), duree_travaux=int(enfant.attrib["dureeTravaux"]))
            liste_cours.append(cours_inscrit)
        return liste_cours


etudiants = EtudiantETParser().parse_etudiants("etudiants.xml")
for etudiant in etudiants:
    print(etudiant)