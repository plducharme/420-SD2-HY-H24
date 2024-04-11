# Écriture dans un fichier
with open('text.txt', mode='w', encoding='UTF8') as fichier_txt:
    fichier_txt.write('Si les cochons avaient des ailes, ça ferait de beaux serins.')
    print(type(fichier_txt))


