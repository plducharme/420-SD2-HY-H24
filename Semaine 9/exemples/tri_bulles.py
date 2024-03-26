import random


def tri_bulles(tableau):

    for i in range(0, len(tableau)-1):
        print("Passe: " + str(i+1))
        deja_trie = True
        # parcours les éléments de gauche à droite et les échanges au besoin
        for j in range(0, len(tableau)-1-i):
            print("Comparaison de " + str(tableau[j]) + " avec " + str(tableau[j+1]))
            if tableau[j+1] < tableau[j]:
                print(str(tableau[j+1]) + " est plus petit que "+ str(tableau[j]) + " , on échange les deux éléments")
                temp = tableau[j]
                tableau[j] = tableau[j+1]
                tableau[j+1] = temp
                # On a échangé un élément, donc le tri n'est pas terminé
                deja_trie = False
                print(tableau)

        print(tableau)
        # on a fait une passe complète sans changer d'éléments, le tableau est déjà trié
        if deja_trie is True:
            return


liste = [random.randint(0, 50) for x in range(0, 10)]
print(liste)
tri_bulles(liste)