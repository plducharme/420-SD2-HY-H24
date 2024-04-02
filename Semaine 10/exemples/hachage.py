import hashlib
import secrets

# L'algorithme de hachage à sens unique MD5sum permet de vérifier l'intégrité d'un fichier ou d'une chaîne de caractères
str1 = ("Un peuple prêt à sacrifier un peu de liberté pour un peu de sécurité ne mérite ni l'une ni l'autre et finit "
        "par perdre les deux")
str2 = ("Un peuple prêt à sacrifier un peu de liberté pour un peu de sécurité ne mérite ni l'une ni l'autre et finit "
        "par perdre les deux")
str3 = ("Un peuple prêt à sacrifier un peu de libarté pour un peu de sécurité ne mérite ni l'une ni l'autre et finit "
        "par perdre les deux")

print(hashlib.md5(str1.encode("utf-8")).hexdigest())
print(hashlib.md5(str2.encode("utf-8")).hexdigest())
print(hashlib.md5(str3.encode("utf-8")).hexdigest())

# La fonction built-in hash() de python peut être utilisé sur n'importe quel type
print(f"hash(): {hash('42 est la réponse')}")

#############################################################################################
# Encryption sécure avec SHA256
# Générer une "sel" (salt) aléatoire pour réduire le risque de collisions
salt = secrets.token_hex(16)

# Le mot de passe à encrypter
mot_de_passe = "mon mot de passe"

# Hachage du mot de passe
hash_hex = hashlib.sha256((mot_de_passe + salt).encode("utf-8")).hexdigest()
print(hash_hex)
# Il faut ensuite persister le sel et le hash_hex dans la BD

