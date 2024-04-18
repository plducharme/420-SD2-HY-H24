import pickle

dictionnaire = {'The Super Mario Bros. Movie': 30396285, 'John Wick: Chapter 4': 2460347, 'Air': 2322850}

# Serialisation
with open('dict.pickle', 'wb') as pickle_file:
    pickle.dump(dictionnaire, pickle_file)
print('Objet sauvegarde: ' + str(dictionnaire))

# Deserialisation
dictionnaire_charge = None
with open('dict.pickle', 'rb') as pickle_in:
    dictionnaire_charge = pickle.load(pickle_in)
print('Objet charge: ' + str(dictionnaire_charge))

if dictionnaire == dictionnaire_charge:
    print('Equivalent')
