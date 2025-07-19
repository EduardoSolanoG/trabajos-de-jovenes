def pedir_dato(mensaje):
    return input(mensaje)

def pedir_datos_usuario():
    nombre = pedir_dato("¿Cuál es tu nombre? ")
    edad = pedir_dato("¿Cuántos años tienes? ")
    ciudad = pedir_dato("¿En qué ciudad vives? ")
    return {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }

def procesar_datos(datos):
    print("\nResumen de tu información:")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']} años")
    print(f"Ciudad: {datos['ciudad']}")