mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}

print(mi_set_a, type(mi_set_a))

# add() — agrega un elemento
mi_set_a.add(5)
print(mi_set_a)  # → {1, 2, 'tres', 5}

# copy() y clear()
mi_set_c = mi_set_a.copy()
print(mi_set_c)
mi_set_a.clear()
print(mi_set_a)  # → set()

# Reiniciamos para los ejemplos siguientes
mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}

# discard() — remueve un elemento (sin error si no existe)
mi_set_a.discard("tres")
print(mi_set_a)  # → {1, 2}

# remove() — remueve un elemento (arroja error si no existe)
mi_set_a = {1, 2, "tres"}
mi_set_a.remove("tres")
print(mi_set_a)  # → {1, 2}

# pop() — elimina y retorna un elemento al azar
mi_set_a = {1, 2, "tres"}
aleatorio = mi_set_a.pop()
print(aleatorio)

# Reiniciamos
mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}

# difference() — elementos únicamente en A
mi_set_c = mi_set_a.difference(mi_set_b)
print(mi_set_c)  # → {1, 2}

# difference_update() — remueve de A los elementos comunes con B
mi_set_a.difference_update(mi_set_b)
print(mi_set_a)  # → {1, 2}

# Reiniciamos
mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}

# intersection() — elementos comunes a A y B
mi_set_c = mi_set_a.intersection(mi_set_b)
print(mi_set_c)  # → {'tres'}

# intersection_update() — mantiene solo los comunes en A
mi_set_b.intersection_update(mi_set_a)
print(mi_set_b)  # → {'tres'}

# Reiniciamos
mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}

# union() — combina A y B eliminando duplicados
mi_set_c = mi_set_a.union(mi_set_b)
print(mi_set_c)  # → {1, 2, 3, 'tres'}

# update() — inserta en A los elementos de B
mi_set_a.update(mi_set_b)
print(mi_set_a)  # → {1, 2, 3, 'tres'}

# Reiniciamos
mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}

# symmetric_difference() — todo excepto los comunes
mi_set_c = mi_set_b.symmetric_difference(mi_set_a)
print(mi_set_c)  # → {1, 2, 3}

# symmetric_difference_update()
mi_set_b.symmetric_difference_update(mi_set_a)
print(mi_set_b)  # → {1, 2, 3}

# Reiniciamos
mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}

# isdisjoint() — True si no tienen elementos en común
print(mi_set_a.isdisjoint(mi_set_b))  # → False

# issubset() — True si todos los elementos de B están en A
print(mi_set_b.issubset(mi_set_a))    # → False

# issuperset() — True si A contiene todos los elementos de B
print(mi_set_a.issuperset(mi_set_b))  # → False
