import random


def tri_insertion(tableau):
    # Comme l'on compare l'élément avec ses prédécesseurs, on commence l'index à 1
    for i in range(1, len(tableau)):
        courant = tableau[i]
        print("Élément courant à comparer: " + str(courant))
        p = i
        # Tant que l'élément précédent est plus grand que l'élément courant, on "échange" l'élément courant avec le
        # précédent. On cherche à l'insérer au bon endroit au début de la liste
        while p > 0 and tableau[p-1] > courant:
            tableau[p] = tableau[p - 1]
            p = p - 1
        # On a trouvé l'endroit où l'insérer
        tableau[p] = courant
        print(tableau)


liste = [random.randint(0, 50) for x in range(0, 10)]
print("Début: " + str(liste))
tri_insertion(liste)


