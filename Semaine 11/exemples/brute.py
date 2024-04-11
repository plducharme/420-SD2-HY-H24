# ouverture d'un fichier en mode lecture brute, sans mémoire tampon
with open('text.txt', 'rb', buffering=0) as raw_reader:
    print(type(raw_reader))