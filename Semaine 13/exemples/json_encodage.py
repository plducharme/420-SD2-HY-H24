import json

twwh3 = {'nom': 'Total War: Warhammer 3', 'isCoop': True, 'anneeParution': 2022, "tags": ["twwh3", "wh3", "fantasy"]}
# transforme le dictionnaire Python en une string json
jeu_json = json.dumps(twwh3)
print(jeu_json)

# Encode le dictionnaire Python vers un fichier json
with open('twwh3.json', 'w') as json_file:
    json.dump(twwh3, json_file)
# Encode le dictionnaire Python vers un fichier json avec une indentation
with open("twwh3_indent.json", "w") as json_file:
    json.dump(twwh3, json_file, indent=4)

