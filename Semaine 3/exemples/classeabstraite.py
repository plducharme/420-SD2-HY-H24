# from <module> import <classe>, <décorateur>, etc
from abc import ABC, abstractmethod


# La classe dérive de ABC
class ClasseAbstraite(ABC):

    # décorateur pour déclarer la méthode abstraite
    @abstractmethod
    def methode_abstraite(self):
        pass





