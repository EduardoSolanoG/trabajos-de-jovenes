from functools import reduce

def contar_respuestas_correctas(df):
    """
    Usa reduce para contar respuestas correctas a una pregunta especifica.
    """
    respuestas = df["¿Cuál es la principal característica de Python?"].dropna().tolist()
    return reduce(lambda acc, r: acc + (1 if r == "b) Legibilidad y sintaxis clara" else 0), respuestas, 0)
