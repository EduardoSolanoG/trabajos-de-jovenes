import pandas as pd
from filter import (filtrar_respuestas_correctas)
from map import extraer_nombres
from reduce import contar_respuestas_correctas
from sorted import ordenar_nombres

def cargar_csv(ruta):
    try:
        return pd.read_csv(ruta)
    except FileNotFoundError:
        print(f"⚠️ Archivo no encontrado en: {ruta}")
        return None
    except Exception as e:
        print(f"⚠️ Error al cargar el archivo: {e}")
        return None

def main():
    ruta = "respuestas_del_cuentionario_Respuestas_de_formulario.csv"  # Asegúrate de tener el archivo en la misma carpeta
    df = cargar_csv(ruta)
    if df is None:
        return

    print("=== FILTER ===")
    if 'nombre completo' in df.columns:
        filtrados = filtrar_respuestas_correctas(df)
        print(f"Participantes que respondieron correctamente: {len(filtrados)}")
        for nombre in filtrados['nombre completo']:
            print("-", nombre)
    else:
        print("Columna 'nombre completo' no encontrada.")

    print("\n=== MAP ===")
    if 'nombre completo' in df.columns:
        nombres = extraer_nombres(df)
        print("Nombres extraídos:")
        for nombre in nombres:
            print("-", nombre)
    else:
        print("Columna 'nombre completo' no encontrada.")

    print("\n=== REDUCE ===")
    total_correctas = contar_respuestas_correctas(df)
    print(f"Total de respuestas correctas: {total_correctas}")

    print("\n=== SORTED ===")
    if 'nombre completo' in df.columns:
        nombres_ordenados = ordenar_nombres(df)
        print("Nombres ordenados alfabéticamente:")
        for nombre in nombres_ordenados:
            print("-", nombre)
    else:
        print("Columna 'nombre completo' no encontrada.")

if __name__ == "__main__":
    main()