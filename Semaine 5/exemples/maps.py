def carre(a):
    return a**2


# création d'un map, notez l'absence de parenthèse à la fonction
m = map(carre, range(0, 20))

# retourne l'objet map
print(m)
# convertir en liste pour voir le contenu facilement
print(list(m))

# Avec une fonction anonyme
f = map(lambda x: x**2, range(0, 20))
print(list(f))


iter1 = [0, 8, 9, 2, 5]
iter2 = [0, 7, 3, 9, 3]

expos = map(lambda x, y: x**y, iter1, iter2)
print(list(expos))
