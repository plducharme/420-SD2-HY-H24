def somme(*entiers):
    print('Arguments: ' + str(entiers))
    total = 0
    for x in entiers:
        total += x

    return total


print(somme(5, 9, 12, 2))


def afficher_arguments(**kwargs):
    for k, v in kwargs.items():
        print(k + ':\t' + v)


afficher_arguments(nom='Ducharme', prenom='Pier Luc', grandeur='6 pieds')
