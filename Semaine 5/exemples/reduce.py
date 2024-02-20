from functools import reduce


def ajout(x, y):
    return x + y


liste = (0, 2, 5, 7, 9)

# Réduction de l'itérable liste en une valeur simple
r = reduce(ajout, liste)
# Convertir en liste pour faciliter l'impression
print(r)
# Équivalent
r2 = reduce(lambda x, y: x + y, liste)
print(r2)

