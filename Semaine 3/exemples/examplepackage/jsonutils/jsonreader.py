import json


def read_json(filename):
    f = open(filename, 'r')
    return json.loads(f.read())

