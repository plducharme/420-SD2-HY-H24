class Levier:
    """Classe utilitaire pour le calcul de force de leviers.

        Cette classe a été écrite pour montrer un exemple de docstrings. Elle permet de calculer des forces
        selon le type de levier

        Properties created with the ``@property`` decorator should be documented
        in the property's getter method.

        Attributes:
            type_levier (int): Type de levier à calculer. Les types sont définis par des variables de classe
            LEVIER_BILATERAL (int): Variable définissant un type de levier bilatéral.

        """

    LEVIER_BILATERAL = 0

    def __init__(self, type_levier: int):
        self.type_levier = type_levier

    def calcul_force(self, masse_objet: float, rayon_masse: float, rayon_bras: float):
        """Méthode permettant de calculer la force nécessaire pour lever un objet.

                Note:
                    Ne jamais inclure self dans les arguments.

                Args:
                    masse_objet: La masse de l'objet en kg.
                    rayon_masse: Le rayon jusqu'au centre de gravité de l'objet.
                    rayon_bras: Le rayon jusqu'au bras.

                Returns:
                    La force nécessaire, None si incapable de calculer.

                """

        if self.type_levier == Levier.LEVIER_BILATERAL:
            return masse_objet * 9.8 * rayon_masse / rayon_bras
        else:
            return None
