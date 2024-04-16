import os

# Le répertoire courant (cwd: current working directory)
print(f"Répertoire courant: {os.getcwd()}")

# Créer un répertoire
os.mkdir("autre_repertoire")

# liste tous les fichiers et répertoire (avec aucun arguments, le répertoire courant; sinon le répertoire donné en
# paramètre
fichiers = os.listdir()
for fd in fichiers:
    if os.path.isfile(fd):
        print(f"Fichier: {fd}")
    elif os.path.isdir(fd):
        print(f"Répertoire: {fd}")

# change de répertoire
os.chdir("../")
print(f"Répertoire courant: {os.getcwd()}")
