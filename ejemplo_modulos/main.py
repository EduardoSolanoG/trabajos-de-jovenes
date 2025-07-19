from Funciones import pedir_datos_usuario, procesar_datos

def main():
    datos_usuario = pedir_datos_usuario()
    procesar_datos(datos_usuario)

if __name__ == "__main__":
    main()