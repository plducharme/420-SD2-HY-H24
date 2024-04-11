with open('citations.txt') as reader:
    # Lire une ligne
    ligne = reader.readline()
    print(ligne)

    # lire toutes les lignes
    ligne = reader.readline()
    # lire jusqu'a l'atteinte de la fin du fichier EOF, ''
    while ligne != '':
        print(ligne, end='')
        ligne = reader.readline()

with open('citations.txt') as reader:
    # Lire en utilisant un iterateur
    for ligne in reader:
        print(ligne, end='')


with open('citations.txt') as reader:
    # Lire toutes les lignes et retourne une liste de lignes
    lignes = reader.readlines()


with open('citations.txt') as reader:
    # lire le nombre de bytes du fichier, si -1, lis le fichier en entier
    reader.read(15)


