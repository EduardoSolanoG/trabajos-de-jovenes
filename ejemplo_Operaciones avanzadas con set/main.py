import operaciones_set as ops

def main():
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    ops.mostrar_conjuntos(A,B)
    print()

    ops.operacion_union(A, B)
    ops.operacion_interseccion(A, B)
    ops.diferencia(A, B)
    ops.diferencia_simetrica(A, B)
    ops.conjuntos_disjuntos(A, B)
    ops.es_superconjunto(A, {1, 2})
    ops.es_subconjunto({1, 2}, A)

    print("\nDemostrando 'update' con copia")
    C = A.copy()
    ops.operacion_update(C, B)


if __name__ == "__main__":
    main()
