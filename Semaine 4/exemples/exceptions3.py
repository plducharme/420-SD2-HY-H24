

try:
    x = input('Entrez les nombres à diviser:\t')
    div = x.split()
    print(str(int(div[0]) / int(div[1])))

except (ValueError, ZeroDivisionError, RuntimeError) as e:
    print('Mauvaise division')
