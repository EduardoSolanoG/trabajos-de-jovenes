from collections import deque

def ejemplo_deque():
    cola = deque()
    cola.append("primer")
    cola.append("segundo")
    cola.append("cero")
    print("cola: ", list(cola))
    cola.pop()
    print("Despues del pop:", list(cola))
