with open('proverbes.txt', 'w', encoding="utf8") as writer:
    # Écrire une string dans le fichier
    writer.write('Folle est la brebis qui au loup se confesse\n')

    # Écrire à partir d'une liste de string
    liste = ['Quand le blé est mûr, on le fauche\n',
             'À vaincre sans péril, on triomphe sans gloire\n',
             'Qui vole un oeuf vole un boeuf\n']
    writer.writelines(liste)


# Liste de séquence d'octets à écrire
octets_a_ecrire = [b"Texte en octets", bytes.fromhex("2Ef0 F1f2")]
with open("proverbes.bin", mode="wb") as writer:
    for octets in octets_a_ecrire:
        writer.write(octets)