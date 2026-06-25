mi_tuple = (1, 2, 3, 4, (10, 20))
print(mi_tuple, type(mi_tuple), mi_tuple[0])
print(len(mi_tuple))
"""
no soportan asignación de items
mi_tuple[4] = 44
print(mi_tuple)
"""

mi_tuple = list(mi_tuple)
print(mi_tuple, type(mi_tuple))

mi_otro_tuple = (1,2,3)
x, y, z = mi_otro_tuple
print(x, y, z)

t = (1,2,3,4,2)
print(f"Hay {t.count(2)} elemento con el valor 2 en tu tuple")
print(t.index(2))