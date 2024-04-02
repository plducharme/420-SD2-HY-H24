import heapq

elements = [65, 70, 56, 32, 91, 25, 22, 26, 50, 47]
print(elements)
# transforme une liste en tas
heapq.heapify(elements)
print(elements)
# ajoute au tas
heapq.heappush(elements, 42)
print(elements)
# enleve la racine element du tas
racine = heapq.heappop(elements)
print(f'racine enlevée: {racine}, nouveau tas:\n{elements}')
# remplace la racine par un nouvel élément et réorganise le tas au besoin
heapq.heapreplace(elements, 42)
print(elements)
