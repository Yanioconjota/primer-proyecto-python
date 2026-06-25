mi_set = set([1,2,3,4,5])
#mi_set = set(1,2,3,4,5) - Python entiende que recibe 5 argumentos
print(mi_set, type(mi_set))

#Al no declarar "clave": "valor", Python entiende que es un set
otro_set = {1, 2, 3, 4, 5}
print(otro_set, type(otro_set))

# print(mi_set[0]) al no poseer un orden no son subscribibles
# mi_set[0] = 5 Tampoco soportan asignación de items

set_con_repetidos = {1, 1, 2, 3, 4, 5, 5, 5}
# No mostrará error. Solo mostrará valores únicos
print(set_con_repetidos)

another_set = set([1, 2, "Tres", False, (5, 10)])
print(another_set)

# los sets no permiten ni listas, ni diccionarios ya que son elementos mutables
# set_con_mutables = {1, 2, "Tres", False, [1], {"nombre": "Janio"}}

# Al igual que en las listas y diccionarios podemos preguntar si un elemento está o no en el set
print("Tres" in another_set)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(f"el método union, une los 2 sets sin repetidos {s3}")

s3.add(6)
s3.add(4)
# Si el elemento no existe lo agrega, si existe lo omite sin error
print(s3)

# s1.remove(6) con remove, si el elemento no existe da error

s1.remove(1)
print(s1)

# Con discard, no remueve un elemento que no existe y devuelve el set original
s1.discard(1)
print(s1)

# Como los sets no tienen orden elige un elemento aleatorio, puede ser útil para elegir un número al azar
sorteo = s2.pop()
print(sorteo)

# Clear limpia el set completo
s2.clear()
print(s2)