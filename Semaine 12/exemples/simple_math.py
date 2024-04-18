# simple_math.py

class SimpleMath:

    def somme(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def somme_liste(self, data):
        total = 0
        for x in data:
            total += x
        return total

