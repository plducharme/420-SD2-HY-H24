import math
import matplotlib.pyplot as plt


# calcule une constante (i.e. y = k)
def constante(valeur):
    return 1


# calcule une valeur linéaire (i.e. y = x, y = 2x +1)
def lineaire(valeur):
    return valeur


# calcule une valeur quadratique (i.e. y = x^k)
def quad(valeur):
    return valeur**2


# calcule une valeur polynomiale (i.e. y = k^x)
def poly(valeur):
    return 2**valeur


# calcule une valeur factorielle (i.e. y = x!)
def facto(valeur):
    return math.factorial(valeur)


# calcule une valeur logarithmique (i.e. y = log x + k)
def log(valeur):
    return math.log(valeur)


# liste pour les valeurs de x
nombre = []
# liste pour les valeurs calculée de y pour les différentes fonctions
quadra = []
polynomiale = []
factorielle = []
suite_lineaire = []
const = []
logarithme = []

# appels des fonctions pour le calcul, aurait pu être sous forme de liste en compréhension
for i in range(1, 100):
    nombre.append(i)
    quadra.append(quad(i))
    polynomiale.append(poly(i))
    factorielle.append(facto(i))
    suite_lineaire.append(lineaire(i))
    const.append(constante(i))
    logarithme.append(log(i))

# Appel de pyplot pour générer le graphique
# premier argument, la liste des x (techniquement un vecteur)
# deuxième argument, la liste des y (techniquement un vecteur)
# troisième paramètre, le libellé pour cette courbe
plt.plot(nombre, quadra, '-r', label='n^2')
plt.plot(nombre, polynomiale, '-b', label='2^n')
plt.plot(nombre, factorielle, '-g', label='n!')
plt.plot(nombre, suite_lineaire, '-m', label='n')
plt.plot(nombre, const, '-k', label='1')
plt.plot(nombre, logarithme, '-c', label='log(n)')
# libellé de l'axe des x
plt.xlabel('valeur de n')
# libellé de l'axe des y
plt.ylabel('valeur du résultat de la fonction')
# limite du graphique pour l'axe des y
plt.ylim((0, 100))
# Emplacement de la légende
plt.legend(loc="upper left")
# afficher le graphique
plt.show()