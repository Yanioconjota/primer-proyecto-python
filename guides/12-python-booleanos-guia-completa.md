# Guía Completa de Booleanos en Python

Los **booleanos** son tipos de datos binarios (`True` / `False`) que surgen de operaciones lógicas, o pueden declararse explícitamente.

> 💡 En Python, `True` y `False` se escriben con mayúscula inicial. Son instancias del tipo `bool`, que es una subclase de `int` (`True == 1`, `False == 0`).

---

## Índice

1. [Declarar Booleanos](#1-declarar-booleanos)
2. [Operadores de Comparación](#2-operadores-de-comparación)
3. [Operadores Lógicos — `and`, `or`, `not`](#3-operadores-lógicos--and-or-not)
4. [Valores Truthy y Falsy](#4-valores-truthy-y-falsy)
5. [Resumen — Cheatsheet](#5-resumen--cheatsheet)

---

## 1. Declarar Booleanos

```python
activo = True
inactivo = False

print(activo, type(activo))    # → True <class 'bool'>
print(inactivo, type(inactivo)) # → False <class 'bool'>

# Bool es subclase de int
print(int(True))   # → 1
print(int(False))  # → 0
```

Los booleanos también **surgen de operaciones lógicas**:

```python
resultado = 5 > 3
print(resultado, type(resultado))  # → True <class 'bool'>
```

---

## 2. Operadores de Comparación

Comparan dos valores y retornan `True` o `False`.

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | igual a | `5 == 5` | `True` |
| `!=` | diferente a | `5 != 3` | `True` |
| `>` | mayor que | `5 > 3` | `True` |
| `<` | menor que | `5 < 3` | `False` |
| `>=` | mayor o igual que | `5 >= 5` | `True` |
| `<=` | menor o igual que | `3 <= 5` | `True` |

```python
edad = 20

print(edad == 20)   # → True
print(edad != 18)   # → True
print(edad > 18)    # → True
print(edad < 18)    # → False
print(edad >= 20)   # → True
print(edad <= 30)   # → True
```

---

## 3. Operadores Lógicos — `and`, `or`, `not`

Combinan o invierten expresiones booleanas.

### `and` — `True` si **ambas** declaraciones son `True`

```python
tiene_dni = True
es_mayor = True

puede_votar = tiene_dni and es_mayor
print(puede_votar)  # → True

print(True and False)  # → False
print(False and False) # → False
```

### `or` — `True` si **al menos una** declaración es `True`

```python
tiene_efectivo = False
tiene_tarjeta = True

puede_pagar = tiene_efectivo or tiene_tarjeta
print(puede_pagar)  # → True

print(False or False)  # → False
```

### `not` — invierte el valor del booleano

```python
esta_cerrado = False
print(not esta_cerrado)  # → True

print(not True)   # → False
print(not False)  # → True
```

### Tabla de verdad

| A | B | `A and B` | `A or B` | `not A` |
|---|---|:---------:|:--------:|:-------:|
| `True` | `True` | `True` | `True` | `False` |
| `True` | `False` | `False` | `True` | `False` |
| `False` | `True` | `False` | `True` | `True` |
| `False` | `False` | `False` | `False` | `True` |

---

## 4. Valores Truthy y Falsy

Python evalúa cualquier valor como `True` o `False` en un contexto booleano. Esto permite usar variables directamente en condiciones.

**Falsy** — se evalúan como `False`:

```python
print(bool(0))       # → False
print(bool(0.0))     # → False
print(bool(""))      # → False  (string vacío)
print(bool([]))      # → False  (lista vacía)
print(bool({}))      # → False  (dict/set vacío)
print(bool(None))    # → False
```

**Truthy** — todo lo demás se evalúa como `True`:

```python
print(bool(1))        # → True
print(bool(-1))       # → True  (cualquier número distinto de 0)
print(bool("hola"))   # → True
print(bool([0]))      # → True  (lista con al menos un elemento)
```

---

## 5. Resumen — Cheatsheet

| Concepto | Código | Resultado |
|----------|--------|-----------|
| Declarar | `x = True` | `bool` |
| Igual a | `a == b` | `True` / `False` |
| Diferente a | `a != b` | `True` / `False` |
| Mayor / Menor | `a > b` / `a < b` | `True` / `False` |
| Mayor o igual | `a >= b` | `True` / `False` |
| Menor o igual | `a <= b` | `True` / `False` |
| Ambas verdaderas | `a and b` | `True` si ambas son `True` |
| Al menos una | `a or b` | `True` si alguna es `True` |
| Invertir | `not a` | Invierte el booleano |
| Convertir a bool | `bool(valor)` | `True` o `False` |
| Convertir a int | `int(True)` | `1` |
