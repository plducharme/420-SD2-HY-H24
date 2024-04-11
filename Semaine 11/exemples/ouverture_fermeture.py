# fichier = open('citations.txt')
import sys

files = [open(f"./tmp/files-{n}.txt", "w") for n in range(10000)]

# Peut potentiellement générer un fichier corrompu
fichier = open('tst.txt', 'w')
fichier.write("Ceci est un test d'intégrité de fichier!")
sys.exit(1)