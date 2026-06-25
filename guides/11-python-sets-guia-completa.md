# Guía Completa de Sets en Python

Un **set** es una colección mutable de elementos **inmutables**, **no ordenados** y **sin datos repetidos**. Son útiles para eliminar duplicados y para operaciones matemáticas de conjuntos (unión, intersección, diferencia).

> 💡 Los sets se reconocen por las llaves `{ }` con elementos separados por comas — igual que un diccionario, pero **sin pares clave:valor**. Por ejemplo: `{1, 2, "tres"}`.

---

## Propiedades de los Sets

| Propiedad | Valor | Descripción |
|-----------|:-----:|-------------|
| **Mutable** | ✅ | Se pueden agregar y eliminar elementos. |
| **Ordenado** | ❌ | No mantiene el orden de inserción; no se accede por índice. |
| **Admite duplicados** | ❌ | Si agregás un elemento que ya existe, el set lo ignora. |
| **Elementos hasheables** | ✅ | Solo acepta `int`, `float`, `str`, `bool`, `tuple`. No puede contener listas ni diccionarios (son mutables). |

> Ver también: [Guía de Tipos de Datos](./04-python-tipos-de-datos-guia-completa.md) para comparar sets con listas, tuples y diccionarios.

---

## Índice

1. [Crear Sets](#1-crear-sets)
2. [Restricciones — Qué puede y no puede contener](#2-restricciones--qué-puede-y-no-puede-contener)
3. [Operador `in` — Verificar membresía](#3-operador-in--verificar-membresía)
4. [Métodos de Elemento — `add()`, `remove()`, `discard()`, `pop()`](#4-métodos-de-elemento--add-remove-discard-pop)
5. [Vaciar — `clear()`](#5-vaciar--clear)
6. [Operaciones de Conjuntos — `union()`, `intersection()`, `difference()`](#6-operaciones-de-conjuntos--union-intersection-difference)
7. [Resumen — Cheatsheet](#7-resumen--cheatsheet)

---

## 1. Crear Sets

### Con llaves `{ }` — sintaxis literal

```python
otro_set = {1, 2, 3, 4, 5}
print(otro_set, type(otro_set))
# → {1, 2, 3, 4, 5} <class 'set'>
```

### Con `set([lista])` — constructor

```python
mi_set = set([1, 2, 3, 4, 5])
print(mi_set, type(mi_set))
# → {1, 2, 3, 4, 5} <class 'set'>
```

> ⚠️ `set(1, 2, 3)` **no funciona** — Python interpreta que recibe múltiples argumentos. El constructor `set()` recibe **un único iterable**: `set([1, 2, 3])`.

### Set vacío — siempre con `set()`

```python
vacio = set()
print(type(vacio))  # → <class 'set'>

# {} crea un diccionario vacío, no un set
print(type({}))     # → <class 'dict'>
```

### Duplicados — se eliminan automáticamente

```python
set_con_repetidos = {1, 1, 2, 3, 4, 5, 5, 5}
print(set_con_repetidos)
# → {1, 2, 3, 4, 5}  — sin error, solo valores únicos
```

---

## 2. Restricciones — Qué puede y no puede contener

Los elementos de un set deben ser **hasheables** (inmutables). Un set puede contener:

```python
another_set = set([1, 2, "Tres", False, (5, 10)])
print(another_set)
# → {False, 1, 2, 'Tres', (5, 10)}
```

Lo que **no** puede contener:

```python
# Listas y diccionarios son mutables → TypeError: unhashable type
# set_con_mutables = {1, 2, "Tres", False, [1], {"nombre": "Janio"}}
```

| Tipo | ¿Permitido en set? |
|------|--------------------|
| `int`, `float`, `str`, `bool` | ✅ |
| `tuple` | ✅ (si sus elementos también son hasheables) |
| `list` | ❌ — mutable |
| `dict` | ❌ — mutable |
| `set` | ❌ — mutable |

---

## 3. Operador `in` — Verificar membresía

Al igual que en listas y diccionarios, podés preguntar si un elemento está en el set:

```python
another_set = {1, 2, "Tres", False, (5, 10)}

print("Tres" in another_set)   # → True
print(99 in another_set)       # → False
print(99 not in another_set)   # → True
```

> 💡 La verificación con `in` en sets es **O(1)** (tiempo constante), más eficiente que en listas donde es O(n).

---

## 4. Métodos de Elemento — `add()`, `remove()`, `discard()`, `pop()`

### `add(item)` — agrega un elemento; si ya existe, lo omite sin error

```python
s3 = {1, 2, 3, 4, 5}
s3.add(6)
print(s3)  # → {1, 2, 3, 4, 5, 6}

s3.add(4)  # ya existe, no hace nada
print(s3)  # → {1, 2, 3, 4, 5, 6}
```

### `remove(item)` — elimina un elemento; lanza `KeyError` si no existe

```python
s1 = {1, 2, 3}
s1.remove(1)
print(s1)  # → {2, 3}

# s1.remove(6)  → KeyError: 6
```

### `discard(item)` — elimina un elemento; **no lanza error** si no existe

```python
s1 = {2, 3}
s1.discard(1)  # no existe, pero no hay error
print(s1)      # → {2, 3}  (sin cambios)
```

> 💡 Preferí `discard()` cuando no estás seguro de si el elemento existe.

### `pop()` — elimina y retorna un elemento **al azar**

Como los sets no tienen orden, `pop()` elige un elemento aleatorio. Puede usarse para sorteos o selección aleatoria:

```python
s2 = {3, 4, 5}
sorteo = s2.pop()
print(sorteo)  # → algún elemento (no predecible)
print(s2)      # → el set sin ese elemento
```

---

## 5. Vaciar — `clear()`

```python
s2 = {3, 4, 5}
s2.clear()
print(s2)  # → set()
```

---

## 6. Operaciones de Conjuntos — `union()`, `intersection()`, `difference()`

Sets de referencia:

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
```

### `union(set)` — une dos sets eliminando duplicados (retorna set nuevo)

```python
s3 = s1.union(s2)
print(f"union une los 2 sets sin repetidos: {s3}")
# → {1, 2, 3, 4, 5}
```

### `intersection(set)` — elementos comunes a ambos sets

```python
print(s1.intersection(s2))  # → {3}
```

### `difference(set)` — elementos solo en A (no en B)

```python
print(s1.difference(s2))  # → {1, 2}
print(s2.difference(s1))  # → {4, 5}
```

> Para las variantes que modifican el set original (`update()`, `intersection_update()`, `difference_update()`, `symmetric_difference()`) ver el [PDF de métodos de sets](../Sets+-+Métodos.pdf).

---

## 7. Resumen — Cheatsheet

| Operación | Código | Modifica in-place |
|-----------|--------|:-----------------:|
| Crear desde lista | `set([1, 2, 3])` | — |
| Crear literal | `{1, 2, 3}` | — |
| Set vacío | `set()` | — |
| Verificar membresía | `x in s` | No |
| Agregar elemento | `s.add(x)` | Sí |
| Eliminar (con error) | `s.remove(x)` | Sí |
| Eliminar (sin error) | `s.discard(x)` | Sí |
| Eliminar al azar | `s.pop()` | Sí |
| Vaciar | `s.clear()` | Sí |
| Unión | `s1.union(s2)` | No |
| Intersección | `s1.intersection(s2)` | No |
| Diferencia | `s1.difference(s2)` | No |
| Verificar tipo | `type(s)` | — |
