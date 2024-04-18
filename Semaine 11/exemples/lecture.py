with open('citations.txt', encoding="utf8") as reader:
    # Lire une ligne
    ligne = reader.readline()
    print(ligne)

    # lire une autre ligne
    ligne = reader.readline()
    # lire jusqu'à l'atteinte de la fin du fichier EOF, ''
    while ligne != '':
        print(ligne, end='')
        ligne = reader.readline()

with open('citations.txt', mode="rt") as reader:
    # Lire en utilisant un itérateur
    for ligne in reader:
        print(ligne, end='')


with open('citations.txt', mode="rt") as reader:
    # Lire toutes les lignes et retourne une liste de lignes
    lignes = reader.readlines()


with open('citations.txt', mode="rb") as reader:
    # lire un nombre d'octets (bytes) du fichier, si -1, lis le fichier en entier
    grosseur_chunk = 512
    chunk = reader.read(grosseur_chunk)
    # On boucle pour lire jusqu'à qu'il n'y a plus rien à lire (chunk sera 0)
    while chunk:
        # Faire quelque avec le chunk
        print(chunk)
        # Lecture du prochain "chunk"
        chunk = reader.read(grosseur_chunk)

