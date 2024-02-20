from collections import ChainMap

peinture = {'La Joconde': 'DaVinci', 'Les Baigneuses': 'Courbet', 'La jeune fille à la perle': 'Vermeer'}
films = {'Full Metal Jacket': 'Kubrick', 'Metropolis': 'Fritz Lang'}

cm = ChainMap(peinture, films)
# affiche la liste de clés-valeurs
for k, v in cm.items():
    print(k, v)

print(cm.maps)
# Recherche dans les dictionnaires excluant le premier
print('Full Metal Jacket' in cm.parents)

