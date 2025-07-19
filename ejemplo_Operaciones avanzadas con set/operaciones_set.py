def mostrar_conjuntos(a, b):
    print(f"Conjunto A: {a}")
    print(f"Conjunto B: {b}")

def operacion_update(a, b):
    a.update(b)
    print(f"Update (A actualizado con B): {a}")

def conjuntos_disjuntos(a, b):
    print(f"¿A y B son disjuntos?: {a.isdisjoint(b)}")

def es_superconjunto(a, b):
    print(f"¿A es superconjunto de B?: {a.issuperset(b)}")

def es_subconjunto(a, b):
    print(f"¿A es subconjunto de B?: {a.issubset(b)}")

def operacion_union(a, b):
    print(f"Unión A | B: {a.union(b)}")

def operacion_interseccion(a, b):
    print(f"Interseccion A & B: {a.intersection(b)}")

def diferencia_simetrica(a, b):
    print(f"Diferencia simetrica A ^ B: {a.symmetric_difference(b)}")

def diferencia(a, b):
    print(f"Diferencia A - B: {a.difference(b)}")