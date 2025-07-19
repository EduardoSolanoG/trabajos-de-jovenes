from collections import namedtuple

def ejemplo_namedtuple():
    Persona = namedtuple('Persona', ['nombre', 'edad'])
    persona1 = Persona(nombre="Cintya", edad=24)
    print(f"Nombre: {persona1.nombre}, Edad: {persona1.edad}")
