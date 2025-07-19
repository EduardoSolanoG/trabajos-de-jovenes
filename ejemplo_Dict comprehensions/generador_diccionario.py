def generador_cuadrados_dict(inicio, fin):
    """
    Genera un diccionario con números y sus cuadrados.
    :param inicio: número entero de inicio (inclusive)
    :param fin: múmero entero final (inclusive)
    :return: dict {numero: cuadrado}
    """

    return {x: x ** 2 for x in range(inicio, fin + 1)}
