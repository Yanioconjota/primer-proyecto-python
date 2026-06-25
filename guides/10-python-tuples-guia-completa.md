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
2. [Indexado — Acceder a Elementos](#2-indexado--acceder-a-elementos)
3. [Casting — Convertir a Lista](#3-casting--convertir-a-lista)
4. [Unpacking — Extraer Elementos](#4-unpacking--extraer-elementos)
5. [Resumen — Cheatsheet](#5-resumen--cheatsheet)

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

## 2. Indexado — Acceder a Elementos

Se accede igual que en listas, con corchetes `[ ]`. Los índices arrancan en `0`.

```python
mi_tuple = (1, "dos", [3.33, "cuatro"], (5.0, 6))

print(mi_tuple[1])     # → dos
print(mi_tuple[3])     # → (5.0, 6)

# Acceso encadenado (el elemento es un tuple o lista)
print(mi_tuple[3][0])  # → 5.0
print(mi_tuple[2][1])  # → cuatro
```

> ⚠️ Intentar modificar un elemento lanza `TypeError: 'tuple' object does not support item assignment`.

---

## 3. Casting — Convertir a Lista

Cuando necesitás modificar los datos de un tuple, convertilo a lista con `list()`. El resultado es una nueva lista mutable; el tuple original no cambia.

```python
mi_tuple = (1, "dos", [3.33, "cuatro"], (5.0, 6))

lista_1 = list(mi_tuple)
print(lista_1)
# → [1, 'dos', [3.33, 'cuatro'], (5.0, 6)]

lista_1.append("nuevo")
print(lista_1)
# → [1, 'dos', [3.33, 'cuatro'], (5.0, 6), 'nuevo']
```

Para el camino inverso, usá `tuple()`:

```python
de_vuelta = tuple(lista_1)
print(type(de_vuelta))  # → <class 'tuple'>
```

---

## 4. Unpacking — Extraer Elementos

El unpacking asigna cada elemento del tuple a una variable en una sola línea. La cantidad de variables debe coincidir con la cantidad de elementos.

```python
mi_tuple = (1, "dos", [3.33, "cuatro"], (5.0, 6))

a, b, c, d = mi_tuple

print(a)  # → 1
print(b)  # → dos
print(c)  # → [3.33, 'cuatro']
print(d)  # → (5.0, 6)
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

## 5. Resumen — Cheatsheet

| Operación | Código | Resultado |
|-----------|--------|-----------|
| Crear tuple | `t = (1, "a", 3.0)` | Tuple con 3 elementos |
| Tuple de un elemento | `t = (42,)` | `(42,)` — la coma es obligatoria |
| Acceder por índice | `t[0]` | Primer elemento |
| Acceso encadenado | `t[2][1]` | Elemento dentro de lista/tuple anidado |
| Longitud | `len(t)` | Número de elementos |
| Convertir a lista | `list(t)` | Lista mutable con los mismos elementos |
| Convertir a tuple | `tuple(lista)` | Tuple inmutable |
| Unpacking completo | `a, b, c = t` | Variables individuales |
| Unpacking parcial | `primero, *resto = t` | Primero + lista con el resto |
| Verificar tipo | `type(t)` | `<class 'tuple'>` |
