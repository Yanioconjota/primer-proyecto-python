# Guía Completa de Operadores de Comparación

Como su nombre lo indica, sirven para comparar dos o más valores.
El resultado de esta comparación es un **booleano** (`True` / `False`).

---

## 1. Tabla de Operadores

| Operador | Significado          |
|----------|----------------------|
| `==`     | igual a              |
| `!=`     | diferente a          |
| `>`      | mayor que            |
| `<`      | menor que            |
| `>=`     | mayor o igual que    |
| `<=`     | menor o igual que    |

> Si la comparación resulta verdadera devuelve `True`; si es falsa devuelve `False`.

---

## 2. `==` — Igual a

Compara si dos valores son iguales. Es sensible al tipo de dato.

```python
print(10 == 10)      # True
print(10 == 10.0)    # True  — int y float con el mismo valor son iguales
print(10 == "10")    # False — int vs str nunca son iguales
print("hola" == "Hola")  # False — mayúsculas importan
```

---

## 3. `!=` — Diferente a

Devuelve `True` cuando los valores **no** son iguales.

```python
print(5 != 6)   # True
print(5 != 5)   # False
print("a" != "A")  # True
```

---

## 4. `>` y `<` — Mayor / Menor que

```python
print(10 > 6)   # True
print(6 > 10)   # False

print(5 < 6)    # True
print(6 < 5)    # False
```

---

## 5. `>=` y `<=` — Mayor o igual / Menor o igual que

La diferencia con `>` y `<` es que también devuelven `True` cuando los valores son iguales.

```python
print(5 >= 6)   # False
print(6 >= 6)   # True  ← también True cuando son iguales
print(7 >= 6)   # True

print(5 <= 6)   # True
print(6 <= 6)   # True  ← también True cuando son iguales
print(6 <= 5)   # False
```

---

## 6. Comparar Expresiones

Los operadores actúan sobre el **resultado** de cualquier expresión, no solo variables.

```python
print(10 == 2 * 5)   # True
print(10 > 3 + 6)    # True
print(4 ** 2 == 16)  # True
```

---

## 7. Comparar Strings

Python compara strings **carácter a carácter** usando el orden Unicode.

```python
print("manzana" == "manzana")   # True
print("manzana" == "Manzana")   # False — 'M' (77) < 'm' (109)
print("b" > "a")                # True
print("abc" < "abd")            # True — difieren en el tercer carácter
```

---

## 8. Guardar el Resultado en una Variable

El resultado es un `bool` y puede almacenarse y reutilizarse.

```python
mi_bool = 5 >= 6
print(mi_bool)          # False
print(type(mi_bool))    # <class 'bool'>

es_mayor = 10 > 3
print(es_mayor)         # True
```

---

## 9. Resumen — Cheatsheet

| Ejemplo         | Resultado |
|-----------------|-----------|
| `5 == 5`        | `True`    |
| `5 == 6`        | `False`   |
| `5 != 6`        | `True`    |
| `5 != 5`        | `False`   |
| `10 > 6`        | `True`    |
| `6 > 10`        | `False`   |
| `5 < 6`         | `True`    |
| `6 < 5`         | `False`   |
| `5 >= 6`        | `False`   |
| `6 >= 6`        | `True`    |
| `5 <= 6`        | `True`    |
| `6 <= 5`        | `False`   |
| `10 == 2 * 5`   | `True`    |
| `10 == "10"`    | `False`   |
