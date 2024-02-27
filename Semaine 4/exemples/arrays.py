import array

arr = array.array('i', (1, 2, 8, 9, 4))
# Supprimer l'élément à l'indexe 1
del arr[1]
print(arr)

arr.append(42)
print(arr)

arr[0] = 7
print(arr)





