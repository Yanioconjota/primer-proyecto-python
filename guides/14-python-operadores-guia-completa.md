# Guía Completa de Operadores en Python

Los **operadores** son símbolos o palabras clave que le indican a Python que realice una operación sobre uno o más valores. Se dividen en tres grupos principales: aritméticos, de comparación y lógicos.

---

## 1. Operadores Aritméticos

Realizan operaciones matemáticas sobre números (`int` o `float`).

| Operador | Nombre | Ejemplo | Resultado |
|----------|--------|---------|-----------|
| `+` | Suma | `5 + 3` | `8` |
| `-` | Resta | `5 - 3` | `2` |
| `*` | Multiplicación | `5 * 3` | `15` |
| `/` | División | `7 / 2` | `3.5` (siempre `float`) |
| `//` | División entera | `7 // 2` | `3` (descarta decimales) |
| `%` | Módulo (resto) | `7 % 2` | `1` |
| `**` | Potencia | `2 ** 8` | `256` |

```python
x = 6
y = 2
z = 7

print(f"{x} más {y} es: {x + y}")           # → 8
print(f"{x} menos {y} es: {x - y}")         # → 4
print(f"{x} por {y} es: {x * y}")           # → 12
print(f"{x} dividido {y} es: {x / y}")      # → 3.0

print(f"{z} división entera {y}: {z // y}") # → 3
print(f"{z} módulo {y}: {z % y}")           # → 1
print(f"{x} elevado a {y}: {x ** y}")       # → 36
print(f"Raíz cuadrada de {x}: {x ** .5}")   # → 2.449...
```

> 💡 `/` siempre devuelve `float`. `//` devuelve `int` si ambos operandos son `int`.

---

## 2. Operadores de Comparación

Comparan dos valores y siempre retornan un **booleano** (`True` o `False`).

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Distinto de | `5 != 3` | `True` |
| `>` | Mayor que | `5 > 3` | `True` |
| `<` | Menor que | `5 < 3` | `False` |
| `>=` | Mayor o igual | `5 >= 5` | `True` |
| `<=` | Menor o igual | `3 <= 5` | `True` |

```python
print(10 == 10)     # → True
print(10 == 9)      # → False
print(10 != 9)      # → True
print(10 > 5)       # → True
print(10 < 5)       # → False
print(10 >= 10)     # → True
print(10 <= 9)      # → False
```

> ⚠️ **Error común:** confundir `=` (asignación) con `==` (comparación). `x = 5` asigna el valor; `x == 5` pregunta si son iguales.

---

## 3. Operadores Lógicos

Permiten tomar decisiones basadas en **múltiples condiciones**. Trabajan con booleanos y también retornan un booleano.

```python
a = 6 > 5    # → True
b = 30 == 15 * 3  # → False (15*3 = 45, no 30)
```

---

### `and` — todas las condiciones deben ser verdaderas

Retorna `True` solo si **todas** las condiciones son `True`.

```python
mi_bool = a and b
print(mi_bool)
# → False   (a es True, b es False → una es False → resultado False)
```

**Tabla de verdad de `and`:**

| `a` | `b` | `a and b` |
|-----|-----|-----------|
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

---

### `or` — al menos una condición debe ser verdadera

Retorna `True` si **al menos una** condición es `True`.

```python
mi_bool = a or b
print(mi_bool)
# → True   (a es True → con una basta)
```

**Tabla de verdad de `or`:**

| `a` | `b` | `a or b` |
|-----|-----|----------|
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

---

### `not` — invierte el booleano

Retorna `True` si el valor es `False`, y `False` si el valor es `True`.

```python
mi_bool = not a
print(mi_bool)
# → False   (a es True → not True → False)

print(not False)   # → True
print(not True)    # → False
```

---

### Combinar operadores lógicos

Puedes encadenar múltiples condiciones en una sola expresión:

```python
edad = 25
tiene_dni = True
es_mayor = edad >= 18

# Debe cumplir las dos condiciones
print(es_mayor and tiene_dni)
# → True

# Basta con una
print(edad < 18 or tiene_dni)
# → True

# Verificar que NO se cumpla una condición
print(not (edad < 18))
# → True
```

> 💡 **Orden de evaluación:** `not` → `and` → `or`. Usa paréntesis para forzar el orden que necesites.

---

## Resumen General

### Aritméticos

| Operador | Operación | Ejemplo | Resultado |
|----------|-----------|---------|-----------|
| `+` | Suma | `3 + 2` | `5` |
| `-` | Resta | `3 - 2` | `1` |
| `*` | Multiplicación | `3 * 2` | `6` |
| `/` | División | `7 / 2` | `3.5` |
| `//` | División entera | `7 // 2` | `3` |
| `%` | Módulo | `7 % 2` | `1` |
| `**` | Potencia | `2 ** 3` | `8` |

### Comparación

| Operador | Significado | Retorna |
|----------|-------------|---------|
| `==` | Igual | `bool` |
| `!=` | Distinto | `bool` |
| `>` | Mayor | `bool` |
| `<` | Menor | `bool` |
| `>=` | Mayor o igual | `bool` |
| `<=` | Menor o igual | `bool` |

### Lógicos

| Operador | Comportamiento | Retorna `True` cuando... |
|----------|---------------|--------------------------|
| `and` | Todas verdaderas | Todas las condiciones son `True` |
| `or` | Al menos una verdadera | Al menos una condición es `True` |
| `not` | Invierte el booleano | El valor original es `False` |
