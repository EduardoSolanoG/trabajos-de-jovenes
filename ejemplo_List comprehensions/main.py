from filtros import es_par
from operaciones import calcular_cuadrado

def generar_lista_cuadrados_pares(inicio, fin):
    """Genera una lista de cuadrados de números pares en el rango dado."""
    return [calcular_cuadrado(n) for n in range(inicio, fin + 1) if es_par(n)]

def main():
    resultado = generar_lista_cuadrados_pares(1, 10)
    print("cuadrados de los números pares del 1 al 10: ", resultado)


if __name__ == "__main__":
    main()