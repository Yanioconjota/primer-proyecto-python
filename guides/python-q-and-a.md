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
