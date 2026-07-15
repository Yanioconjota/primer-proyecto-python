hijos = ["Gomoso Sue", "Condolleza Marie", "Sabina", "Honoria", "Tránsito", "Higinio", "Ufano", "Hilario", "Jacinta", "Cándido", "Teodosia", "Cástulo", "Gervasia", "Epifanio", "Gaudelia", "Eufemio", "Eustaquio", "Brígida", "Melitón", "Leonila", "Nicanor", "Martina", "Régulo", "Teodora", "Teódulo", "Tiburcio", "Celso"]

""" print(f"Tengo {len(mi_lista)} hijos, te presento a: " + ', '.join(mi_lista)) """
print(f"Tengo {len(hijos)} hijos, te presento a: ")
for i, hijo in enumerate(hijos):
    separador = ",\n " if i < len(hijos) - 1 else "\n"
    print(hijo + separador, end="")
    
"""
enumerate() te da el índice i en cada iteración, y cuando i llega al último elemento (len - 1) se usa string vacío en lugar de la coma.
"""

print("--------------------------------")

for nombre in hijos:
  if nombre.startswith("G"):
    print(nombre)
  else:
    print(f"{nombre} no comienza con G")    
    
"""
startswith() te permite verificar si el nombre comienza con la letra "G".
"""

numeros = [1, 2, 3, 4, 5]
valor = 0

for elemento in numeros:
  valor += elemento
  print(f"La suma de los números es: {valor}")

palabra = "Python"
for letra in palabra:
  print(letra)
  
lista = [[1, 2], [3, 4], [5, 6]]
for elemento in lista:
  print(elemento)

for a, b in lista:
  print(a)
  print(b)

diccionario = {"nombre": "Juan", "edad": 20, "ciudad": "Madrid"}
for clave, valor in diccionario.items():
  print(f"{clave}: {valor}")
  
### Ejercicios
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print(f"Hola {alumno}")
    
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for num in lista_numeros:
    suma_numeros += num
    
print(f"La suma de los números es: {suma_numeros}")

print("--------------------------------")

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num
print(f"La suma de los números pares es: {suma_pares}")
print(f"La suma de los números impares es: {suma_impares}")