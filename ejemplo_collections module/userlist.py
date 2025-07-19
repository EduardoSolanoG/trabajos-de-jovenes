from collections import UserList

class MiLista(UserList):
    def append(self, item):
        print(f"Agregando: {item}")
        super().append(item)

def ejemplo_userlist():
    lista = MiLista()
    lista.append(5)
    lista.append(10)
    print("Lista: ", lista)
