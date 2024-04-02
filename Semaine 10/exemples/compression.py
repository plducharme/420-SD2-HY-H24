import gzip

# créer un fichier gzip
contenu = b'Voici le contenu a compresser'
with gzip.open('contenu.txt.gz', 'wb') as f:
    f.write(contenu)

# lire le fichier compresse
with gzip.open('contenu.txt.gz', 'rb') as f:
    contenu_fichier = f.read()
print(f'Décompressé:  {contenu_fichier} ')

# compression d'une chaîne de caractères
non_compresse = b'Le contenu original qui devra etre compresse'
print(f'contenu:   {non_compresse}')
compresse = gzip.compress(non_compresse)
print(f'compression:  {compresse}')

# decompression
decomp = gzip.decompress(compresse)
print(f'décompression:   {decomp}')

