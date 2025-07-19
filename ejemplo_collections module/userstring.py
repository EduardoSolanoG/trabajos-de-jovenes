from collections import UserString

class MiCadena(UserString):
    def upper(self):
        print("Convirtiendo a Mayúsculas")
        return self.data.upper()

def ejemplo_userstring():
    cadena = MiCadena("Hola mundo cruel")
    print("Cadena original: ", cadena)
    print("Cadena Con mayúsculas: ", cadena.upper())
