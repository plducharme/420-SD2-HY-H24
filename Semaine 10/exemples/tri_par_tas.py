class TriTas:

    @staticmethod
    def trier(tableau):
        # On commence par transformer le tableau en tas (à partir du dernier père)
        # len(tableau) // 2 - 1 est l'index du dernier père
        for i in range(len(tableau) // 2 - 1, -1, -1):
            TriTas.tamisage_max(tableau, len(tableau), i)
        print(f'tableau en tas:\t{tableau}')

        # On classe les elements en permutant la racine (le plus grand elements) à la dernière position non triée
        # Puis on retamise par la racine le reste du tableau (en commençant par la nouvelle racine)
        for i in range(len(tableau)-1, 0, -1):
            (tableau[i], tableau[0]) = (tableau[0], tableau[i])
            print(f'Tableau après permutation {tableau}\ti: {i}')
            TriTas.tamisage_max(tableau, i, 0)
            print(f'Tableau après retamisage {tableau}\ti: {i}')

    @staticmethod
    # tamisage_max = tasser_max
    def tamisage_max(tableau, taille, index):
        maximum = index
        index_fils_gauche = 2 * index + 1
        index_fils_droit = 2 * index + 2

        # Compare le pere avec le fils gauche pour deter
        if index_fils_gauche < taille and tableau[index_fils_gauche] > tableau[maximum]:
            maximum = index_fils_gauche
        if index_fils_droit < taille and tableau[index_fils_droit] > tableau[maximum]:
            maximum = index_fils_droit
        if maximum != index:
            # On a trouvé le plus grand fils plus grand que le père; On les permute
            (tableau[index], tableau[maximum]) = (tableau[maximum], tableau[index])
            TriTas.tamisage_max(tableau, taille, maximum)


liste = [65, 70, 56, 32, 91, 25, 22, 26, 50, 47]
print(f'Tableau originale:\t{liste}')
TriTas.trier(liste)
print(f'\nRésultat: {liste}')
