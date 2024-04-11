with open('proverbes.txt', 'w') as writer:
    # Écrire une string dans le fichier
    writer.write('Folle est la brebis qui au loup se confesse\n')

    # Écrire a partir d'une sequence de string
    liste = ['Quand le blé est mûr, on le fauche\n',
             'À vaincre sans péril, on triomphe sans gloire\n',
             'Qui vole un oeuf vole un boeuf\n']
    writer.writelines(liste)
