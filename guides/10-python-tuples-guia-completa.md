# Guía Completa de Tuples en Python

Un **tuple** (o tupla) es una estructura de datos que almacena múltiples elementos en una única variable. Se distingue de las listas por ser **inmutable**: una vez creado, sus elementos no pueden modificarse.

> 💡 Un tuple se reconoce por los paréntesis `( )` con elementos separados por comas. Por ejemplo: `(1, "dos", 3.0)`.

---

## Propiedades de los Tuples

| Propiedad | Descripción |
|-----------|-------------|
| **Inmutables** | No se pueden agregar, modificar ni eliminar elementos después de creado. |
| **Ordenados** | Mantienen el orden de inserción; el índice es estable. |
| **Admiten duplicados** | El mismo valor puede aparecer más de una vez. |
| **Heterogéneos** | Pueden contener elementos de distintos tipos: `int`, `str`, `list`, otro `tuple`, etc. |
| **Eficientes** | Al ser inmutables, ocupan menos memoria y son más rápidos que las listas. |

> Ver también: [Guía de Tipos de Datos](./04-python-tipos-de-datos-guia-completa.md) para comparar tuples con listas, diccionarios y sets.

---

## Índice

1. [Crear Tuples](#1-crear-tuples)
2. [Indexado y Longitud](#2-indexado-y-longitud)
3. [Inmutabilidad](#3-inmutabilidad)
4. [Casting — Convertir a Lista](#4-casting--convertir-a-lista)
5. [Unpacking — Extraer Elementos](#5-unpacking--extraer-elementos)
6. [Métodos — `count()` e `index()`](#6-métodos--count-e-index)
7. [Resumen — Cheatsheet](#7-resumen--cheatsheet)

---

## 1. Crear Tuples

```python
# Tuple de un solo tipo
mi_tuple = (1, 2, 3, 4)
print(mi_tuple, type(mi_tuple))
# → (1, 2, 3, 4) <class 'tuple'>

# Tuple con tipos mixtos: int, str, list, tuple anidado
mi_tuple = (1, "dos", [3.33, "cuatro"], (5.0, 6))
print(mi_tuple)
# → (1, 'dos', [3.33, 'cuatro'], (5.0, 6))

# Tuple vacío
vacio = ()

# Tuple de un solo elemento (la coma es obligatoria)
uno = (42,)
print(type(uno))   # → <class 'tuple'>
print(type((42)))  # → <class 'int'>  ← sin coma, es solo un int entre paréntesis
```

---

## 2. Indexado y Longitud

Se accede igual que en listas, con corchetes `[ ]`. Los índices arrancan en `0`.

```python
mi_tuple = (1, 2, 3, 4, (10, 20))

print(mi_tuple[0])      # → 1
print(mi_tuple[4])      # → (10, 20)

# Acceso encadenado (el elemento es un tuple anidado)
print(mi_tuple[4][0])   # → 10

# Longitud con len()
print(len(mi_tuple))    # → 5
```

---

## 3. Inmutabilidad

Los tuples **no soportan asignación de ítems**. Intentarlo lanza `TypeError`:

```python
mi_tuple = (1, 2, 3, 4, (10, 20))

# Esto genera error:
# mi_tuple[4] = 44
# → TypeError: 'tuple' object does not support item assignment
```

Si necesitás modificar elementos, primero convertí el tuple a lista (ver sección 4).

---

## 4. Casting — Convertir a Lista

Cuando necesitás modificar los datos de un tuple, convertilo a lista con `list()`. El resultado es una nueva lista mutable; el tuple original no cambia.

```python
mi_tuple = (1, 2, 3, 4, (10, 20))

mi_tuple = list(mi_tuple)
print(mi_tuple, type(mi_tuple))
# → [1, 2, 3, 4, (10, 20)] <class 'list'>
```

Para el camino inverso, usá `tuple()`:

```python
de_vuelta = tuple(mi_tuple)
print(type(de_vuelta))  # → <class 'tuple'>
```

---

## 5. Unpacking — Extraer Elementos

El unpacking asigna cada elemento del tuple a una variable en una sola línea. La cantidad de variables debe coincidir con la cantidad de elementos.

```python
mi_otro_tuple = (1, 2, 3)
x, y, z = mi_otro_tuple
print(x, y, z)  # → 1 2 3
```

### Unpacking parcial con `*`

Si no necesitás todas las variables, usá `*` para capturar el resto en una lista:

```python
primero, *resto = (1, 2, 3, 4)
print(primero)  # → 1
print(resto)    # → [2, 3, 4]

*inicio, ultimo = (1, 2, 3, 4)
print(inicio)   # → [1, 2, 3]
print(ultimo)   # → 4
```

---

## 6. Métodos — `count()` e `index()`

Los tuples tienen solo dos métodos propios (al ser inmutables no pueden tener métodos que modifiquen la estructura).

### `count(valor)` — cuenta ocurrencias

```python
t = (1, 2, 3, 4, 2)
print(t.count(2))
# → 2
print(f"Hay {t.count(2)} elementos con el valor 2 en tu tuple")
```

### `index(valor)` — índice de la primera ocurrencia

```python
t = (1, 2, 3, 4, 2)
print(t.index(2))
# → 1  (primera posición donde aparece el 2)
```

> ⚠️ Si el valor no existe, `index()` lanza `ValueError`. Verificá con `valor in t` antes si no estás seguro.

---

## 7. Resumen — Cheatsheet

| Operación | Código | Resultado |
|-----------|--------|-----------|
| Crear tuple | `t = (1, "a", 3.0)` | Tuple con 3 elementos |
| Tuple de un elemento | `t = (42,)` | `(42,)` — la coma es obligatoria |
| Acceder por índice | `t[0]` | Primer elemento |
| Acceso encadenado | `t[2][1]` | Elemento dentro de tuple/lista anidado |
| Longitud | `len(t)` | Número de elementos |
| Contar ocurrencias | `t.count(val)` | Número de veces que aparece `val` |
| Encontrar índice | `t.index(val)` | Índice de la primera ocurrencia |
| Convertir a lista | `list(t)` | Lista mutable con los mismos elementos |
| Convertir a tuple | `tuple(lista)` | Tuple inmutable |
| Unpacking completo | `a, b, c = t` | Variables individuales |
| Unpacking parcial | `primero, *resto = t` | Primero + lista con el resto |
| Verificar tipo | `type(t)` | `<class 'tuple'>` |
