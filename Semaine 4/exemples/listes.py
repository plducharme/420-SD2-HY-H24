instruments = ['guitare', 'basse', 'mandoline', 'banjo', 'piano', 'guitare']
# compter le nombre de 'guitare'
print(instruments.count('guitare'))

# index de banjo
print(instruments.index('banjo'))

# index de guitare à partir de la position 2
print(instruments.index('guitare', 2))

# renverse l'ordre de la liste
instruments.reverse()
print(instruments)

# ajoute un élément à la fin de la liste
instruments.append('cornemuse')
print(instruments)

cubes = [x**3 for x in range(12)]
print(cubes)
# équivalent
cubes = list(map(lambda x: x**3, range(12)))

tuples_liste =[(x, y) for x in [4, 6, 9, 12] for y in [3, 8, 15, 11, 7] if x < y]
print(tuples_liste)

