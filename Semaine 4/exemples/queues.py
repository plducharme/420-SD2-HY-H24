from collections import deque

lettres_aleatoire = deque('adsfjfghjtyexcvbewq')
print(lettres_aleatoire)

# enlève l'élément au début de la liste
print(lettres_aleatoire.popleft())

# ajouter un élément à la fin
lettres_aleatoire.append('T')
print(lettres_aleatoire)

# recherche d'un élément dans la liste
print('j' in lettres_aleatoire)

# round robin
lettres_aleatoire.rotate(-1)
print(lettres_aleatoire)
