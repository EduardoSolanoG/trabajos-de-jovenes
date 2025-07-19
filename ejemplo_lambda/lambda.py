personas = [("Ana", 19), ("Eduardo", 30), ("Cintya", 24), ("Pedro", 27)]


personas_ordenadas = sorted(personas, key=lambda persona: persona[1])


print("lista original:")
print(personas)


print("\nLista ordenada por edad:")
print(personas_ordenadas)