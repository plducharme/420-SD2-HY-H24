from abc import ABC, abstractmethod
from typing import List
from molecule import Molecule
from time import perf_counter_ns


class Tri(ABC):

    def __init__(self, nom):
        self.__nom = nom
        self.__debut = None
        self.__fin = None

    @property
    def nom(self):
        return self.__nom

    @abstractmethod
    def trier(self, liste_molecules: List[Molecule]) -> List[Molecule]:
        pass

    def debut(self):
        self.__debut = perf_counter_ns() / 1000000

    def fin(self):
        self.__fin = perf_counter_ns() / 1000000

    def temps_execution(self):
        return self.__fin - self.__debut


