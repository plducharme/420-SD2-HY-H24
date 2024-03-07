class Aigle:

    def voler(self):
        print("Swoosh!!")


class Licorne:

    def galoper(self):
        print("Gallope!")


# La classe Pegase hérite de Aigle et Licorne
# Elle va hériter des attributs (méthodes et variables) de Aigle puis de ceux de Licorne.
class Pegase(Aigle, Licorne):

    def crier(self):
        print("Zoom Zoom Zoom!")


p = Pegase()
p.galoper()
p.voler()
p.crier()
