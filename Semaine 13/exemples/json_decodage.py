# Import du module json
import json

# lecture à partir d'un fichier
with open('exemple.json', 'rt') as acteurs_json:
    liste_acteurs = json.load(acteurs_json)
    # Impression du premier acteur de la liste
    print(liste_acteurs['acteurs'][0])
    # Impression du premier enfant du deuxième acteur
    print(liste_acteurs["acteurs"][1]["enfants"][0])

# Lecture a partir d'une string
film_obj = json.loads('{"nom": "Le declin de l\'empire americain", "realisateur": "Denys Arcand"}')
print(film_obj['nom'] + '\t|\t' + film_obj['realisateur'])


