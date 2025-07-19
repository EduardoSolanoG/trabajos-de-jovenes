def ordenar_nombres(df):
    """
    Ordena alfabéticamente los nombres completos del DataFrame.
    """
    nombres = df['nombre completo'].dropna().tolist()
    nombres_ordenados = sorted(nombres, key=lambda nombre: nombre.lower())
    return nombres_ordenados
