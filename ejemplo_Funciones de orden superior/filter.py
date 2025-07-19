def filtrar_respuestas_correctas(df):
    """Filtar las personas que respondieron correctamente a la pregunta:
    "¿Cúal es la principal característica de Python?"
    """
    return df[df["¿Cuál es la principal característica de Python?"] == "b) Legibilidad y sintaxis clara"]
