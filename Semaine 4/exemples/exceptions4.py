
# # Bonne Pratique
# try:
#     open('filename.txt')
# except FileNotFoundError as e:
#     print('hmmm, le fichier existe pas')
#     raise
# except OSError:
#     print('Erreur OS')
#     raise

# # Mauvaise Pratique
# try:
#     open('filename.txt')
# except Exception:
#     print('Une exception est arrivée')
#
# try:
#     raise NameError('Erreur de nom!!!!!!')
# except NameError:
#     print('Une exception est arrivée')
#     raise

# try:
#     open('filename.tst')
# except OSError:
#     raise RuntimeError('Erreur d\'exécution!')

# class MonException(Exception):
#     # Redéfinir le comportement de l'exception
#     pass
#
# try:
#     raise MonException('Exception lancée!')
# except MonException as e:
#     print('Exception!')
#     raise e


with open('test.txt') as f:
    for ligne in f:
        print(ligne)

