# Déclaration d'un dictionnaire vide
vide = {}
# Déclaration d'un dictionnaire
d = {'Nathan': 75, 'Lina': 84, 'Arthur': 69}
# Afficher une valeur à partir d'une clé
print(d['Lina'])
# Retirer une paire clé-valeur
del d['Arthur']
# Ajout par assignation
d['Bart'] = 92
# Afficher le dictionnaire
print(d)
# Afficher la liste des clés
print(list(d))
d['Lina'] = 88
print(d)
# Teste l'appartenance à un dictionnaire
print('Arthur' in d)

# Déclaration d'un dictionnaire en compréhension
a = {x: x**2 for x in (4, 8, 9)}

# Déclaration d'un dictionnaire via le constructeur
y = dict([(1, 8), (3, 90), (4, 44)])


