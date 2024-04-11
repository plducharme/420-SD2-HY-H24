# Fermeture manuelle d'un fichier
fichier = open('test_fermer.txt', 'w')
try:
    fichier.write('Le contenu a ecrire')
finally:
    fichier.close()

# Fermeture automatique avec "with"
with open('fermer-with.txt', 'w') as fichier:
    fichier.write('Peace sells, but who\'s buying?')

