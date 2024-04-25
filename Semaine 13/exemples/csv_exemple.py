import csv

# Lecture d'un fichier CSV directement
with open('exemple.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for ligne in csv_reader:
        # On peut utiliser l'index des colonnes
        print(f'{ligne[0]} | {ligne[1]} | {ligne[2]} | {ligne[3]}')

# Lecture automatique dans un Dictionnaire
with open('exemple.csv', 'r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)
    for ligne in csv_dict_reader:
        # Avec DictReader, si le fichier contient des entêtes, on peut les utiliser comme clés
        print(f'{ligne["nom"]} | {ligne["prenom"]} | {ligne["age"]} | {ligne["ville"]}')

# Ecriture directe d'un csv
with open('personne.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    personnes = [['Lymberger', 'Mathieu', 37, 'St-Lambert'], ['Hendriks', 'Chris', 50, 'Ottawa']]
    for personne in personnes:
        csv_writer.writerow(personne)

# Ecriture via un Dictionnaire
with open('personne2.csv', 'w', newline='') as csv_file:
    champs = ['nom', 'prenom', 'age', 'ville']
    csv_dict_writer = csv.DictWriter(csv_file, fieldnames=champs)
    csv_dict_writer.writeheader()
    csv_dict_writer.writerow({'nom': 'Leduc', 'prenom': 'Stephane', 'age': 48, 'ville': 'St-Eustache'})
    csv_dict_writer.writerow({'nom': 'Busseau', 'prenom': 'Stephane', 'age': 54, 'ville': 'St-Hubert'})

# Exemple d'un fichier csv utilisant ";" comme séparateur
with open("chien.csv", "r") as csv_file:
    csv_dict = csv.DictReader(csv_file, delimiter=";")
    for ligne in csv_dict:
        print(f'{ligne["Nom"]} | {ligne["Race"]} | {ligne["Couleur"]}')
