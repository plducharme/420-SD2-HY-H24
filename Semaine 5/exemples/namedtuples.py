from collections import namedtuple
# Créer un namedtuple (sous-classe)
Point = namedtuple('Point', ['x', 'y'])
# Initialiser un Point
p1 = Point(12, 30)
print(p1)
Point3D = namedtuple('Point3D', Point._fields + ('z', ))
p2 = Point3D(23, 45, 12)
print(p2.x, p2.y, p2.z)
# Avec la méthode _make
liste = [8, 9, 3]
p3 = Point3D._make(liste)
print(p3)
# Avec le constructeur avec un unpacked d'un dictionnaire
d = {'x': 4, 'y': 8, 'z': 2}
p4 = Point3D(**d)
print(p4)

