from collections import ChainMap

def ejemplo_chainmap():
    dict1 = {"a": 1, "b": 2}
    dict2 = {'b': 3, 'c': 4}
    combinado = ChainMap(dict1, dict2)
    print("Chainmap: ", dict(combinado))
