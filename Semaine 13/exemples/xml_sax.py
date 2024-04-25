from etudiant import Etudiant, Cours
import xml.sax


# Dans le cas d'un parser SAX, à chaque Element que le parser va trouver, il va appeler:
# startElement(self, name, attrs) lorsque le tag (balise) XML est rencontré
# characters(self, content) lorsqu'il y a du contenu dans le tag
# endElement(self, name) lorsque la fin du tag est rencontré
class EtudiantsHandler(xml.sax.ContentHandler):

    # On doit tenir les valeurs jusqu'à ce que l'on ait amassé toutes les informations nécessaires
    def __init__(self):
        self._tag_courant = ""
        self._etudiant_nom = ""
        self._etudiant_prenom = ""
        self._etudiant_da = ""
        self._cours_nom = ""
        self._cours_duree_cours = ""
        self._cours_duree_lab = ""
        self._cours_duree_travaux = ""
        self._liste_cours = []
        self._liste_etudiants = []

    def startElement(self, name, attrs):
        self._tag_courant = name
        # On a besoin des attributs du tag seulement dans le cas du tag "inscrit"
        if name == "inscrit":
            self._cours_nom = attrs["nom"]
            self._cours_duree_cours = attrs["dureeCours"]
            self._cours_duree_lab = attrs["dureeLab"]
            self._cours_duree_travaux = attrs["dureeTravaux"]

    def endElement(self, name):
        # Lorsque l'on a atteint la fin d'un tag, on instancie l'objet nécessaire
        match name:
            case "etudiant":
                self._liste_etudiants.append(Etudiant(self._etudiant_nom, self._etudiant_prenom, int(self._etudiant_da),
                                                      self._liste_cours))
                # On réinitialise les propriétés en cas de tag ou attributs manquants
                self._etudiant_nom = ""
                self._etudiant_prenom = ""
                self._etudiant_da = ""
                self._cours_nom = ""
                self._cours_duree_cours = ""
                self._cours_duree_lab = ""
                self._cours_duree_travaux = ""
                self._liste_cours = []

            case "inscrit":
                self._liste_cours.append(Cours(self._cours_nom, int(self._cours_duree_cours), int(self._cours_duree_lab)
                                               , int(self._cours_duree_travaux)))
            # tag inconnu ou non géré
            case _:
                pass
        # On remet le tag_courant à ""
        self._tag_courant = ""

    def characters(self, content):
        match self._tag_courant:
            case "nom":
                self._etudiant_nom = content
            case "prenom":
                self._etudiant_prenom = content
            case "numeroDa":
                self._etudiant_da = content
            case _:
                pass

    @property
    def etudiants(self):
        return self._liste_etudiants


etudiantsHandler = EtudiantsHandler()
xml.sax.parse("etudiants.xml", etudiantsHandler)
for etudiant in etudiantsHandler.etudiants:
    print(etudiant)




