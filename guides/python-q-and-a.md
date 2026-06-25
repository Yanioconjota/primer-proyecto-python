# Python — Preguntas y respuestas del curso

Recopilación de dudas y respuestas que van surgiendo a lo largo del curso.

---

## Strings inmutables — `TypeError: 'str' object does not support item assignment`

**Código de referencia (`propiedades_string.py`):**

```python
nombres = "Carina"
nombres[0] = "K"
print(nombres)
```

### ¿Qué error produce este código?

Al ejecutar el script, Python detiene el programa en la segunda línea con:

```text
TypeError: 'str' object does not support item assignment
```

En español: **un objeto `str` no admite asignación por índice**.

---

### ¿Por qué ocurre ese error?

Porque en Python los **strings son inmutables**: una vez creados, no puedes cambiar un carácter individual dentro del mismo objeto.

La línea `nombres[0] = "K"` intenta modificar el string existente. Python no lo permite y lanza `TypeError`.

---

### ¿Puedo leer un carácter con `[índice]`?

Sí. Leer funciona sin problema:

```python
nombres = "Carina"
print(nombres[0])   # "C"
print(nombres[-1])  # "a" (último carácter)
```

---

### ¿Cómo cambio un carácter si no puedo usar `nombres[0] = "K"`?

Debes crear un **nuevo** string. No modificas el original; reasignas la variable.

**Opción 1 — concatenar con slicing:**

```python
nombres = "Carina"
nombres = "K" + nombres[1:]
print(nombres)   # Karina
```

**Opción 2 — `replace()`:**

```python
nombres = "Carina"
nombres = nombres.replace("C", "K", 1)
print(nombres)   # Karina
```

---

### ¿Es lo mismo reasignar la variable que modificar el string?

No.

| Acción | ¿Permitido? |
|--------|-------------|
| `nombres[0]` (leer) | Sí |
| `nombres[0] = "K"` (modificar) | No — `TypeError` |
| `nombres = "Karina"` (reasignar) | Sí — apunta a un string nuevo |

---

## Listas — `sort()` devuelve `None`

**Código de referencia (`listas.py`):**

```python
otra_lista = ["C", "D", "M", "A"]
lista_ordenada = otra_lista.sort()
print(lista_ordenada, type(lista_ordenada))
```

### ¿Por qué `lista_ordenada` vale `None`?

Porque `sort()` es un método **in-place**: modifica la lista original directamente y no retorna nada (retorna `None`). Al asignar su resultado a una variable, esa variable recibe `None`.

```python
otra_lista = ["C", "D", "M", "A"]
lista_ordenada = otra_lista.sort()

print(lista_ordenada)          # → None
print(type(lista_ordenada))    # → <class 'NoneType'>
print(otra_lista)              # → ['A', 'C', 'D', 'M']  ← acá sí quedó ordenada
```

---

### ¿Cómo obtengo una lista ordenada sin modificar la original?

Usando `sorted()` — es una función (no un método) que retorna una **lista nueva** y deja la original intacta.

```python
otra_lista = ["C", "D", "M", "A"]
lista_ordenada = sorted(otra_lista)

print(lista_ordenada)   # → ['A', 'C', 'D', 'M']
print(otra_lista)       # → ['C', 'D', 'M', 'A']  (sin cambios)
```

---

### ¿Cuándo uso cada uno?

| | `lista.sort()` | `sorted(lista)` |
|---|---|---|
| Modifica el original | Sí | No |
| Retorna | `None` | Lista nueva ordenada |
| Cuándo usarlo | Cuando no necesitás el original | Cuando necesitás ambas versiones |

---

### ¿`reverse()` tiene el mismo comportamiento?

Sí. `reverse()` también es in-place y retorna `None`. Su equivalente que retorna un nuevo objeto sin modificar el original es `reversed()`.

```python
lista = [1, 2, 3]
print(lista.reverse())        # → None  (modifica lista en el lugar)
print(lista)                  # → [3, 2, 1]

lista = [1, 2, 3]
print(list(reversed(lista)))  # → [3, 2, 1]
print(lista)                  # → [1, 2, 3]  (sin cambios)
```

---

## Diccionarios — ¿Por qué no se puede repetir una clave?

**Código de referencia (`diccionarios.py`):**

```python
mi_otro_diccionario = {
    "clave1": "valor1",
    "clave1": "valor2",
}
print(f"{mi_otro_diccionario} notese que el valor de clave 1 se reescribe")
```

### ¿Por qué no pueden existir claves duplicadas en un diccionario?

Un diccionario es una estructura de **mapeo clave-valor**, y cada clave debe ser única porque es el **identificador** que Python usa para encontrar su valor. Si hubiera dos entradas con la misma clave, Python no sabría cuál devolver al hacer `mi_otro_diccionario["clave1"]`.

Internamente, Python usa una **tabla hash**: al insertar una clave calcula su `hash()` para determinar dónde guardar el valor. Si esa clave ya existe, simplemente **sobreescribe** el valor anterior.

---

### ¿Python lanza un error si repito una clave?

No. Python **no lanza excepción**; gana silenciosamente el último valor asignado:

```python
mi_otro_diccionario = {
    "clave1": "valor1",  # se guarda "valor1"
    "clave1": "valor2",  # sobreescribe → "valor2"
}
print(mi_otro_diccionario)  # → {'clave1': 'valor2'}
```

---

### ¿Cómo guardo múltiples valores para la misma clave?

Usando una **lista como valor**:

```python
mi_diccionario = {
    "clave1": ["valor1", "valor2"],
}
```

---

## Diccionarios y Listas — ¿Existe el operador spread `...` como en JavaScript?

Sí. Python usa `*` para listas y `**` para diccionarios.

### Listas — `*`

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

combinada = [*lista1, *lista2]   # equivale a [...lista1, ...lista2]
print(combinada)  # → [1, 2, 3, 4, 5, 6]
```

### Diccionarios — `**`

```python
base = {"nombre": "Juan", "edad": 20}
extras = {"peso": 80.5, "altura": 1.85}

cliente = {**base, **extras}     # equivale a { ...base, ...extras }
print(cliente)
# → {'nombre': 'Juan', 'edad': 20, 'peso': 80.5, 'altura': 1.85}

# Sobreescribir una clave (gana el último)
actualizado = {**base, "edad": 25}
print(actualizado)  # → {'nombre': 'Juan', 'edad': 25}
```

### Comparación JS → Python

| JS | Python |
|----|--------|
| `[...a, ...b]` | `[*a, *b]` |
| `{ ...a, ...b }` | `{**a, **b}` |
| `{ ...obj, key: val }` | `{**obj, "key": val}` |
| `fn(...args)` (named) | `fn(**dict)` |

---
