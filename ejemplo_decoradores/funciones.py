# Decorador para validar que la entrada contega solo letras
def solo_letras(func):
    def wrapper(mensaje):
        while True:
            valor = func(mensaje)
            if valor.replace(" ", "").isalpha():
                return valor
            print("Solo se permiten letras. Intenta de nuevo")
    return wrapper

#Decorador para validar que la entreda sea un número entero positivo
def solo_numeros(func):
    def wrapper(mensaje):
        while True:
            valor = func(mensaje)
            if valor.isdigit():
                return valor
            print("Solo se permiten números. Intenta de nuevo")
    return wrapper

#funcion base para pedir datod
def pedir_dato(mensaje):
    return input(mensaje)

# Funciones decoradas
@solo_letras
def pedir_nombre(mensaje):
    return pedir_dato(mensaje)

@solo_letras
def pedir_ciudad(mensaje):
    return pedir_dato(mensaje)

@solo_numeros
def pedir_edad(mensaje):
    return pedir_dato(mensaje)

#Recolectar los datos usando funciones decoradas
def pedir_datos_usuario():
    nombre = pedir_nombre("¿Cuál es tu nombre? ")
    edad = pedir_edad("¿Cuántos años tienes? ")
    ciudad = pedir_ciudad("¿En qué ciudad vives? ")
    return {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }

#mostrar resultado
def procesar_datos(datos):
    print("\n✅ Resumen de tu información:")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']} años")
    print(f"Ciudad: {datos['ciudad']}")
