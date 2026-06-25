# Guía Completa de Sets en Python

Un **set** es una colección mutable de elementos **inmutables**, **no ordenados** y **sin datos repetidos**. Son útiles para eliminar duplicados y para operaciones matemáticas de conjuntos (unión, intersección, diferencia).

> 💡 Un set se reconoce por las llaves `{ }` con elementos separados por comas — igual que un diccionario, pero **sin pares clave:valor**. Por ejemplo: `{1, 2, "tres"}`.

---

## Propiedades de los Sets

| Propiedad | Descripción |
|-----------|-------------|
| **Mutable** | Se pueden agregar y eliminar elementos. |
| **No ordenado** | No mantiene el orden de inserción; no se accede por índice. |
| **Sin duplicados** | Si agregás un elemento que ya existe, el set lo ignora. |
| **Elementos inmutables** | Los elementos deben ser de tipo hasheable: `int`, `float`, `str`, `tuple`. No puede contener listas ni otros sets. |

> Ver también: [Guía de Tipos de Datos](./04-python-tipos-de-datos-guia-completa.md) para comparar sets con listas, tuples y diccionarios.

---

## Índice

1. [Crear Sets](#1-crear-sets)
2. [Métodos de Elemento — `add()`, `discard()`, `remove()`, `pop()`](#2-métodos-de-elemento--add-discard-remove-pop)
3. [Copiar y Vaciar — `copy()`, `clear()`](#3-copiar-y-vaciar--copy-clear)
4. [Diferencia — `difference()`, `difference_update()`](#4-diferencia--difference-difference_update)
5. [Intersección — `intersection()`, `intersection_update()`](#5-intersección--intersection-intersection_update)
6. [Unión — `union()`, `update()`](#6-unión--union-update)
7. [Diferencia Simétrica — `symmetric_difference()`, `symmetric_difference_update()`](#7-diferencia-simétrica--symmetric_difference-symmetric_difference_update)
8. [Comparación — `isdisjoint()`, `issubset()`, `issuperset()`](#8-comparación--isdisjoint-issubset-issuperset)
9. [Resumen — Cheatsheet](#9-resumen--cheatsheet)

---

## 1. Crear Sets

```python
mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}

print(mi_set_a, type(mi_set_a))
# → {1, 2, 'tres'} <class 'set'>

# Set vacío — IMPORTANTE: usar set(), no {} (eso crea un dict vacío)
vacio = set()
print(type(vacio))   # → <class 'set'>
print(type({}))      # → <class 'dict'>

# Los duplicados se eliminan automáticamente
con_repetidos = {1, 1, 2, 2, 3}
print(con_repetidos)  # → {1, 2, 3}
```

---

## 2. Métodos de Elemento — `add()`, `discard()`, `remove()`, `pop()`

### `add(item)` — agrega un elemento

```python
mi_set_a = {1, 2, "tres"}
mi_set_a.add(5)
print(mi_set_a)  # → {1, 2, 'tres', 5}

# Agregar un duplicado no hace nada
mi_set_a.add(2)
print(mi_set_a)  # → {1, 2, 'tres', 5}  (sin cambios)
```

### `discard(item)` — remueve un elemento (sin error si no existe)

```python
mi_set_a = {1, 2, "tres"}
mi_set_a.discard("tres")
print(mi_set_a)   # → {1, 2}

mi_set_a.discard("no_existe")  # no lanza error
```

### `remove(item)` — remueve un elemento (lanza `KeyError` si no existe)

```python
mi_set_a = {1, 2, "tres"}
mi_set_a.remove("tres")
print(mi_set_a)   # → {1, 2}

# mi_set_a.remove("no_existe")  → KeyError
```

> 💡 Preferí `discard()` cuando no estás seguro de si el elemento existe.

### `pop()` — elimina y retorna un elemento al azar

```python
mi_set_a = {1, 2, "tres"}
aleatorio = mi_set_a.pop()
print(aleatorio)   # → algún elemento del set (no predecible)
print(mi_set_a)    # → el set sin ese elemento
```

---

## 3. Copiar y Vaciar — `copy()`, `clear()`

### `copy()` — retorna una copia del set

```python
mi_set_a = {1, 2, "tres"}
mi_set_c = mi_set_a.copy()
print(mi_set_c)  # → {1, 2, 'tres'}
```

### `clear()` — remueve todos los elementos

```python
mi_set_a.clear()
print(mi_set_a)  # → set()
```

---

## 4. Diferencia — `difference()`, `difference_update()`

Los sets de referencia para los ejemplos de esta sección:

```python
mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}
```

### `difference(set)` — retorna los elementos **solo en A** (no en B)

```python
mi_set_c = mi_set_a.difference(mi_set_b)
print(mi_set_c)  # → {1, 2}
```

### `difference_update(set)` — remueve de A los elementos comunes con B (modifica A in-place)

```python
mi_set_a.difference_update(mi_set_b)
print(mi_set_a)  # → {1, 2}
```

---

## 5. Intersección — `intersection()`, `intersection_update()`

```python
mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}
```

### `intersection(set)` — retorna los elementos **comunes a A y B**

```python
mi_set_c = mi_set_a.intersection(mi_set_b)
print(mi_set_c)  # → {'tres'}
```

### `intersection_update(set)` — mantiene en A **solo los comunes** con B (modifica A in-place)

```python
mi_set_b.intersection_update(mi_set_a)
print(mi_set_b)  # → {'tres'}
```

---

## 6. Unión — `union()`, `update()`

```python
mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}
```

### `union(set)` — retorna un set nuevo con todos los elementos de A y B (sin duplicados)

```python
mi_set_c = mi_set_a.union(mi_set_b)
print(mi_set_c)  # → {1, 2, 3, 'tres'}
```

### `update(set)` — inserta en A los elementos de B (modifica A in-place)

```python
mi_set_a.update(mi_set_b)
print(mi_set_a)  # → {1, 2, 3, 'tres'}
```

---

## 7. Diferencia Simétrica — `symmetric_difference()`, `symmetric_difference_update()`

```python
mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}
```

### `symmetric_difference(set)` — retorna todos los elementos de A y B **excepto los comunes**

```python
mi_set_c = mi_set_b.symmetric_difference(mi_set_a)
print(mi_set_c)  # → {1, 2, 3}
```

### `symmetric_difference_update(set)` — elimina los comunes y agrega los no compartidos (modifica in-place)

```python
mi_set_b.symmetric_difference_update(mi_set_a)
print(mi_set_b)  # → {1, 2, 3}
```

---

## 8. Comparación — `isdisjoint()`, `issubset()`, `issuperset()`

```python
mi_set_a = {1, 2, "tres"}
mi_set_b = {3, "tres"}
```

### `isdisjoint(set)` — `True` si A y B **no tienen elementos en común**

```python
print(mi_set_a.isdisjoint(mi_set_b))  # → False  (comparten 'tres')
print({1, 2}.isdisjoint({3, 4}))      # → True
```

### `issubset(set)` — `True` si **todos los elementos de A están en B**

```python
print(mi_set_b.issubset(mi_set_a))    # → False
print({1, 2}.issubset({1, 2, 3}))     # → True
```

### `issuperset(set)` — `True` si **A contiene todos los elementos de B**

```python
print(mi_set_a.issuperset(mi_set_b))  # → False
print({1, 2, 3}.issuperset({1, 2}))   # → True
```

---

## 9. Resumen — Cheatsheet

| Método | Acción | Modifica in-place |
|--------|--------|:-----------------:|
| `add(item)` | Agrega un elemento | Sí |
| `discard(item)` | Elimina elemento (sin error si no existe) | Sí |
| `remove(item)` | Elimina elemento (error si no existe) | Sí |
| `pop()` | Elimina y retorna un elemento al azar | Sí |
| `clear()` | Vacía el set | Sí |
| `copy()` | Retorna una copia del set | No |
| `union(B)` | Todos los elementos de A y B | No |
| `update(B)` | Inserta en A los elementos de B | Sí |
| `intersection(B)` | Elementos comunes a A y B | No |
| `intersection_update(B)` | Mantiene en A solo los comunes con B | Sí |
| `difference(B)` | Elementos solo en A | No |
| `difference_update(B)` | Remueve de A los comunes con B | Sí |
| `symmetric_difference(B)` | Todo excepto los comunes | No |
| `symmetric_difference_update(B)` | Elimina comunes, agrega no compartidos | Sí |
| `isdisjoint(B)` | `True` si no comparten elementos | No |
| `issubset(B)` | `True` si A ⊆ B | No |
| `issuperset(B)` | `True` si A ⊇ B | No |
