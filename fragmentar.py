texto = "ABCDEFGHIJKLM"
fragmento = texto[2:6]
print(f"texto[2:6] {fragmento} imprime lo que hay entre la posición 2 y la 6")
fragmento = texto[2:]
print(f"texto[2:] {fragmento} imprime lo que hay entre la posición 2 hasta el final")
fragmento = texto[:5]
print(f"texto[:5] {fragmento} imprime lo que desde el inicio hasta llegar al 5 sin incluirlo")
fragmento = texto[2:10:3]
print(f"texto[2:10:2] {fragmento} imprime lo que hay entre la posición 2 y la 10, tomándolos cada 3 caracteres")
fragmento = texto[::-2]
print(f"texto[2:10:2] {fragmento} imprime la cadena completa al revés tomándolos cada 2 caracteres")