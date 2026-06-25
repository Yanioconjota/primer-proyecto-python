# Guía Completa de Listas en Python

Una **lista** es una secuencia ordenada de objetos. Esos objetos pueden ser de cualquier tipo: strings, integers, floats, booleanos, e incluso otras listas. Son uno de los tipos de datos más usados en Python.

> 💡 En Python, una lista se reconoce por los corchetes `[ ]`. Por ejemplo: `["C", "C++", "Python", "Java"]`.

---

## Propiedades de las Listas

| Propiedad | Descripción |
|-----------|-------------|
| **Mutables** | Sus elementos pueden modificarse después de creada la lista. |
| **Ordenadas** | Los elementos mantienen el orden en que fueron agregados. |
| **Admiten duplicados** | Pueden contener el mismo valor más de una vez. |
| **Indexadas** | Se puede acceder a cada elemento por su posición (`[índice]`). |
| **Tienen longitud** | Se puede medir con `len()`. |
| **Concatenables** | Se pueden unir con el operador `+`. |

> Ver también: [Guía de Tipos de Datos](./04-python-tipos-de-datos-guia-completa.md) para comparar listas con tuplas, diccionarios y sets.

---

## Índice

1. [Crear Listas](#1-crear-listas)
2. [Acceder a Elementos — Indexado](#2-acceder-a-elementos--indexado)
3. [Extraer Partes — Slicing](#3-extraer-partes--slicing)
4. [Longitud con `len()`](#4-longitud-con-len)
5. [Concatenar Listas](#5-concatenar-listas)
6. [Agregar Elementos — `append()`](#6-agregar-elementos--append)
7. [Eliminar Elementos — `pop()`](#7-eliminar-elementos--pop)
8. [Ordenar — `sort()`](#8-ordenar--sort)
9. [Invertir — `reverse()`](#9-invertir--reverse)
10. [Resumen — Cheatsheet](#10-resumen--cheatsheet)

---

## 1. Crear Listas

Una lista se crea con corchetes `[ ]`, separando cada elemento con una coma.

```python
lista_1 = ["C", "C++", "Python", "Java"]
lista_2 = ["PHP", "SQL", "Visual Basic"]

# Una lista puede mezclar tipos de datos
mixta = ["hola", 42, 3.14, True]

# Lista vacía
vacia = []
```

Para verificar el tipo de dato:

```python
mi_lista = ["a", "b", "c"]
print(type(mi_lista))
# → <class 'list'>
```

---

## 2. Acceder a Elementos — Indexado

Cada elemento tiene un índice que empieza en `0`. También se puede usar índices negativos para contar desde el final.

```python
lista_1 = ["C", "C++", "Python", "Java"]

print(lista_1[0])    # → C
print(lista_1[2])    # → Python
print(lista_1[-1])   # → Java  (último elemento)
```

---

## 3. Extraer Partes — Slicing

La sintaxis es `lista[inicio:fin:paso]`. El índice `fin` no está incluido.

```python
lista_1 = ["C", "C++", "Python", "Java"]

print(lista_1[1:3])
# → ['C++', 'Python']

print(lista_1[0:2])
# → ['C', 'C++']

print(lista_1[::2])
# → ['C', 'Python']  (cada dos elementos)
```

> 💡 El slicing funciona igual que en los strings: `[inicio:fin:paso]`.

---

## 4. Longitud con `len()`

Retorna la cantidad de elementos de la lista.

```python
lista_1 = ["C", "C++", "Python", "Java"]

print(len(lista_1))
# → 4
```

---

## 5. Concatenar Listas

El operador `+` une dos listas en una nueva.

```python
lista_1 = ["C", "C++", "Python", "Java"]
lista_2 = ["PHP", "SQL", "Visual Basic"]

print(lista_1 + lista_2)
# → ['C', 'C++', 'Python', 'Java', 'PHP', 'SQL', 'Visual Basic']
```

> ⚠️ La concatenación no modifica las listas originales; genera una nueva.

---

## 6. Agregar Elementos — `append()`

Agrega un elemento **al final** de la lista, modificándola en el lugar.

```python
lista_1 = ["C", "C++", "Python", "Java"]

lista_1.append("R")
print(lista_1)
# → ['C', 'C++', 'Python', 'Java', 'R']
```

---

## 7. Eliminar Elementos — `pop()`

Elimina el elemento en el índice indicado y **retorna el valor eliminado**.

```python
lista_1 = ["C", "C++", "Python", "Java", "R"]

print(lista_1.pop(4))
# → R

print(lista_1)
# → ['C', 'C++', 'Python', 'Java']
```

> 💡 Si no pasas un índice, `pop()` elimina y retorna el último elemento.

---

## 8. Ordenar — `sort()`

Ordena los elementos de la lista **en el lugar** (modifica la lista original).

```python
lista_3 = ["d", "a", "c", "b", "e"]

lista_3.sort()
print(lista_3)
# → ['a', 'b', 'c', 'd', 'e']
```

Para ordenar de mayor a menor:

```python
lista_3.sort(reverse=True)
print(lista_3)
# → ['e', 'd', 'c', 'b', 'a']
```

---

## 9. Invertir — `reverse()`

Invierte el orden de los elementos **en el lugar**. No los ordena; simplemente los voltea.

```python
lista_4 = [5, 4, 7, 1, 9]

lista_4.reverse()
print(lista_4)
# → [9, 1, 7, 4, 5]
```

> ⚠️ `sort()` y `reverse()` no son opuestos. `sort()` ordena según un criterio (alfabético, numérico). `reverse()` solo invierte el orden actual, sin importar cuál sea.

---

## 10. Resumen — Cheatsheet

| Operación | Código | Resultado |
|-----------|--------|-----------|
| Crear lista | `lista = ["a", "b", "c"]` | Lista con 3 elementos |
| Acceder por índice | `lista[0]` | `"a"` |
| Slicing | `lista[1:3]` | `["b", "c"]` |
| Longitud | `len(lista)` | `3` |
| Concatenar | `lista + ["d"]` | `["a", "b", "c", "d"]` |
| Agregar al final | `lista.append("d")` | Modifica la lista original |
| Eliminar por índice | `lista.pop(1)` | Retorna y elimina `"b"` |
| Ordenar | `lista.sort()` | Ordena en el lugar |
| Invertir | `lista.reverse()` | Invierte en el lugar |
| Verificar tipo | `type(lista)` | `<class 'list'>` |
