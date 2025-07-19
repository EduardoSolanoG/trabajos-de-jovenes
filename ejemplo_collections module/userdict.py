from collections import UserDict

class MIDiccionario(UserDict):
    def __setitem__(self, key, value):
        print(f"Agregando clave: {key}, valor: {value}")
        super().__setitem__(key, value)

def ejemplo_userdict():
    dic = MIDiccionario()
    dic["x"] = 10
    print("Diccionario: ", dic)
