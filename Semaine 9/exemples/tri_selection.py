import random


def tri_selection(tableau):

    # Pour chaque emplacement du tableau, on recherche le plus petit élément et on l'échange avec l'élément courant
    for i in range(0, len(tableau)):
        # On garde la valeur et l'emplacement du minimum
        minimum = tableau[i]
        min_index = i

        # itérer sur le reste du tableau pour chercher la plus petite valeur
        for j in range(i, len(tableau)):

            if tableau[j] < minimum:
                # On a trouvé un plus petit élément, ça devient notre nouveau minimum
                minimum = tableau[j]
                min_index = j

        # On a fini de parcourir le reste du tableau; échanger l'élément à l'index i avec le minimum trouvé
        print("Échange du minimum trouvé: " + str(minimum) + " avec " + str(tableau[i]) )
        temp = tableau[i]
        tableau[i] = tableau[min_index]
        tableau[min_index] = temp
        print(tableau)


liste = [random.randint(0, 50) for x in range(0, 10)]
print(liste)
tri_selection(liste)