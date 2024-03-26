import math
import random


def tri_fusion(tableau):
    print(f"Division du tableau {tableau}")
    # diviser le tableau en sous-tableau
    longueur = len(tableau)
    # Si la longueur est 1, on ne peut plus diviser le tableau
    if longueur < 2:
        return
    # trouver le milieu pour diviser (plancher de la division)
    milieu = math.floor(longueur / 2) #équivalent à "longueur // 2"
    # On utilise les "splice" pour couper notre liste (tableau) en sous-listes
    tableau_gauche = tableau[0:milieu]
    tableau_droite = tableau[milieu:longueur]
    print(f'Tableaux divisés: Gauche: {tableau_gauche}\tDroite: {tableau_droite}\tTableau Original: {tableau}')
    # Appelle récursivement pour continuer à diviser puis fusionner
    tri_fusion(tableau_gauche)
    tri_fusion(tableau_droite)
    fusion(tableau_gauche, tableau_droite, tableau)


def fusion(tableau_gauche, tableau_droite, tableau):
    print(f'Fusion de Gauche: {tableau_gauche}\tDroite: {tableau_droite}\tTableau Original: {tableau}')
    longueur_gauche = len(tableau_gauche)
    longueur_droite = len(tableau_droite)
    # i: index du tableau de gauche, j: index du tableau de droite, k: index du tableau original
    i, j, k = 0, 0, 0
    # fusionner en triant les deux petits tableaux tant qu'il y a des éléments à comparer dans les 2 sous-tableaux
    while i < longueur_gauche and j < longueur_droite:
        # L'élément le plus petit entre le tableau de gauche et de droite sera celui sélectionné pour le
        # tableau original
        if tableau_gauche[i] <= tableau_droite[j]:
            tableau[k] = tableau_gauche[i]
            i += 1
        else:
            tableau[k] = tableau_droite[j]
            j += 1
        k += 1
    # Ajouter les éléments restants dans une des deux listes (i.e. un des deux sous-tableaux n'a plus d'élément à
    # comparer, on ajoute le reste de ses éléments au tableau original
    while i < longueur_gauche:
        tableau[k] = tableau_gauche[i]
        i += 1
        k += 1
    while j < longueur_droite:
        tableau[k] = tableau_droite[j]
        j += 1
        k += 1
    print(f"Après fusion: Tableau original: {tableau}")


liste = [random.randint(0, 50) for x in range(0, 10)]
tri_fusion(liste)
