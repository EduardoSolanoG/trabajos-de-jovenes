def extraer_nombres(df):
    """
    Extraer los nombres completos usando map.
    """
    return list(map(str.strip, df["nombre completo"].dropna()))
