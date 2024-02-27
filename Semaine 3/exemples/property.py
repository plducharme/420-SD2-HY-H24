class NombrePositif:

    def __init__(self, valeur):
        self.valeur = valeur

    @property
    def valeur(self):
        print('méthode getter appelée')
        return self._valeur

    @valeur.setter
    def valeur(self, valeur):
        print('méthode setter appelée')
        if valeur < 0:
            raise ValueError('le nombre doit être positif')
        self._valeur = valeur


bon_nombre = NombrePositif(3)
print(bon_nombre.valeur)
bon_nombre.valeur = 4
print(bon_nombre.valeur)

mauvais_nombre = NombrePositif(-1)

