from datos import obtener_numeros
from generador import generar_cuadrados

def main():
    numeros = obtener_numeros()
    cuadrados = generar_cuadrados(numeros)

    print("cuadrados generados: ")
    for cuadrado in cuadrados:
        print(cuadrado)

if __name__ == "__main__":
    main()