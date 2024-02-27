import math as m
from datetime import date
import json
from pprint import *
from examplepackage import *

print(m.pi)
sysutils.sysutils.afficher_chemin_python()
print(date.today())

json_string = {"nom": "Alice", "age": 18, "qualite": {"gentil": True}}
pprint(json.dumps(json_string, indent=6))


