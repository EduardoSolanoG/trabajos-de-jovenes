from collections import defaultdict

def ejemplo_defaultdict():
    agrupado = defaultdict(list)
    datos = [("A", 1), ("B", 2), ("A", 3)]
    for clave, valor in datos:
        agrupado[clave].append(valor)
    print("Agrupado:", dict(agrupado))