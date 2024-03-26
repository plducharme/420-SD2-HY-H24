import random


def tri_rapide(tableau, debut, fin):
    if debut >= fin:
        return
    pivot = partition(tableau, debut, fin - 1)
    # On appelle le tri sur le tableau à gauche du pivot (pivot inclus)
    tri_rapide(tableau, debut, pivot)
    # On appelle le tri sur le tableau à droite du pivot
    tri_rapide(tableau, pivot + 1, fin)


def partition(tableau, debut, fin):
    print('partion: ' + str(tableau) + ' debut: ' + str(debut) + ' fin: ' + str(fin) + " pivot: " + str(tableau[fin]))
    # On choisit le pivot comme le dernier élément du tableau
    pivot = tableau[fin]
    # index est l'index de la borne de gauche
    index = debut
    # On parcourt le tableau (ou sous-tableau) pour que les éléments plus petits que le pivot soient au début du tableau
    for i in range(debut, fin):
        print("Comparaison de " + str(tableau[i]) + " avec le pivot: " + str(pivot))
        if tableau[i] <= pivot:
            print("Échange de " + str(tableau[i]) + " et " + str(tableau[index]))
            temp = tableau[i]
            tableau[i] = tableau[index]
            tableau[index] = temp
            index += 1
            print("Nouveau tableau après échange: " + str(tableau))
    # On échange le pivot (qui est à la fin) avec le plus grand élément trouvé (à l'index)
    print("Échange du pivot avec le plus grand élément trouvé " + str(tableau[index]))
    temp = tableau[index]
    tableau[index] = pivot
    tableau[fin] = temp
    print('pivot: ' + str(tableau[index]) + ' index: ' + str(index))
    print(str(tableau))
    # retourne l'index du pivot
    return index


liste = [random.randint(0, 50) for x in range(0, 10)]
tri_rapide(liste, 0, len(liste))