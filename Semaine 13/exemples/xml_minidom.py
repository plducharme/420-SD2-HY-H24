from typing import List
from xml.dom.minidom import Document, Element
import xml.dom.minidom as minidom
from etudiant import Etudiant, Cours


# minidom créer un DOM en mémoire représentant le document
# Il contient des "Element" qui sont une sous classe de "Node" (noeud)
class EtudiantParser:


    @staticmethod
    def parse_etudiants(chemin_fichier: str) -> List[Etudiant]:
        # parse le fichier en entier pour créer un DOM
        document_xml: Document = minidom.parse(chemin_fichier)
        etudiants: List[Etudiant] = []
        # On va chercher tous les Element etudiant
        etudiants_noeuds = document_xml.getElementsByTagName("etudiant")
        for etudiant_noeud in etudiants_noeuds:
            etudiants.append(EtudiantParser.handle_etudiant(etudiant_noeud))
        return etudiants

    @staticmethod
    def handle_etudiant(etudiant_noeud: Element) -> Etudiant:
        # On va aller chercher les valeurs contenues dans chaque Element
        # Le contenu texte est dans la propriété "data" du premier enfant
        nom = etudiant_noeud.getElementsByTagName("nom")[0].firstChild.data
        prenom = etudiant_noeud.getElementsByTagName("prenom")[0].firstChild.data
        no_da = etudiant_noeud.getElementsByTagName("numeroDa")[0].firstChild.data
        cours_inscrits = []
        for cours_noeud in etudiant_noeud.getElementsByTagName("cours")[0].getElementsByTagName("inscrit"):
           cours_inscrits.append(EtudiantParser.handle_cours(cours_noeud))
        return Etudiant(nom, prenom, no_da, cours_inscrits)

    @staticmethod
    def handle_cours(cours_noeud: Element) -> Cours:
        # On va chercher la valeur des attributs
        nom = cours_noeud.getAttribute("nom")
        duree_cours = cours_noeud.getAttribute("dureeCours")
        duree_lab = cours_noeud.getAttribute("dureeLab")
        duree_travaux = cours_noeud.getAttribute("dureeTravaux")
        return Cours(nom, int(duree_cours), int(duree_lab), int(duree_travaux))


parser = EtudiantParser()
etudiants = parser.parse_etudiants("etudiants.xml")
for etudiant in etudiants:
    print(etudiant)
