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
