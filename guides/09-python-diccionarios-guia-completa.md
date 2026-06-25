# Guía Completa de Diccionarios en Python

Un **diccionario** es una estructura de datos que almacena información en pares **clave:valor**. Son especialmente útiles para guardar y recuperar información a partir del nombre de sus claves, sin necesidad de índices numéricos.

> 💡 En Python, un diccionario se reconoce por las llaves `{ }` con pares `clave: valor` separados por dos puntos. Por ejemplo: `{"curso": "Python TOTAL", "clase": "Diccionarios"}`.

---

## Propiedades de los Diccionarios

| Propiedad | Descripción |
|-----------|-------------|
| **Mutables** | Se pueden agregar, modificar y eliminar pares clave:valor después de creado. |
| **Ordenados** * | Mantienen el orden de inserción desde Python 3.7+. |
| **Claves únicas** | No se permiten claves duplicadas. Si repetís una clave, el valor anterior se sobreescribe. |
| **Valores duplicados** | Los valores sí pueden repetirse entre distintas claves. |
| **Acceso por clave** | Los elementos se acceden por su nombre de clave, no por índice numérico. |

> \* A partir de Python 3.7+, los diccionarios mantienen el orden de inserción para aumentar la eficiencia en el uso de la memoria.

> Ver también: [Guía de Tipos de Datos](./04-python-tipos-de-datos-guia-completa.md) para comparar diccionarios con listas, tuplas y sets.

---

## Índice

1. [Crear Diccionarios](#1-crear-diccionarios)
2. [Acceder a Valores](#2-acceder-a-valores)
3. [Estructuras Anidadas](#3-estructuras-anidadas)
4. [Agregar, Modificar y Mutar Valores](#4-agregar-modificar-y-mutar-valores)
5. [Listar Claves, Valores y Pares — `keys()`, `values()`, `items()`](#5-listar-claves-valores-y-pares--keys-values-items)
6. [Unpacking — `*` y `**`](#6-unpacking----y-)
7. [Resumen — Cheatsheet](#7-resumen--cheatsheet)

---

## 1. Crear Diccionarios

Un diccionario se crea con llaves `{ }`, separando cada par `clave: valor` con una coma.

```python
mi_diccionario = {"curso": "Python TOTAL", "clase": "Diccionarios"}

# Las claves suelen ser strings, pero los valores pueden ser de cualquier tipo
persona = {
    "nombre": "Ana",
    "edad": 30,
    "activa": True,
    "cursos": ["Python", "SQL"]
}

# Diccionario vacío
vacio = {}
```

Para verificar el tipo de dato:

```python
print(type(mi_diccionario))
# → <class 'dict'>
```

---

## 2. Acceder a Valores

Se accede a un valor usando su clave entre corchetes `[ ]`.

```python
mi_diccionario = {"curso": "Python TOTAL", "clase": "Diccionarios"}

print(mi_diccionario["curso"])
# → Python TOTAL

print(mi_diccionario["clase"])
# → Diccionarios
```

Si el valor es una lista, podés encadenar el índice de la lista:

```python
mi_diccionario = {"recursos": ["notas", "ejercicios"]}

print(mi_diccionario["recursos"][1])
# → ejercicios
```

> ⚠️ Intentar acceder a una clave que no existe lanza `KeyError`. Para evitarlo, usá `get()`: `mi_diccionario.get("clave")` retorna `None` si la clave no existe, en lugar de lanzar un error.

---

## 3. Estructuras Anidadas

Los valores de un diccionario pueden ser de **cualquier tipo**: números, strings, listas, o incluso otros diccionarios.

```python
dic = {
    "c1": 55,
    "c2": [10, 20, 30],
    "c3": {"a1": 100, "a2": 200, "a3": 300}
}
```

### Acceder a un elemento dentro de una lista anidada

Encadenás los corchetes: primero la clave del diccionario, luego el índice de la lista.

```python
print(dic["c2"][1])
# → 20
```

### Acceder a un elemento dentro de un diccionario anidado

```python
print(dic["c3"]["a2"])
# → 200
```

### Encadenar métodos de string sobre valores

Si el valor es un string (o un elemento de una lista de strings), podés aplicar métodos directamente sobre el resultado:

```python
dic1 = {
    "clave1": ["a", "b", "c"],
    "clave2": ["d", "e", "f"],
}

print(dic1["clave2"][1].upper())
# → E
```

> 💡 El encadenamiento funciona porque `dic1["clave2"]` devuelve la lista, `[1]` devuelve el string `"e"`, y `.upper()` opera sobre ese string.

---

## 4. Agregar, Modificar y Mutar Valores

Para agregar un nuevo par o modificar uno existente, asignás directamente usando la clave como índice.

```python
mi_diccionario = {"curso": "Python TOTAL", "clase": "Diccionarios"}

# Agregar una nueva clave
mi_diccionario["recursos"] = ["notas", "ejercicios"]
print(mi_diccionario)
# → {'curso': 'Python TOTAL', 'clase': 'Diccionarios', 'recursos': ['notas', 'ejercicios']}

# Modificar un valor existente
mi_diccionario["clase"] = "Diccionarios avanzados"
print(mi_diccionario["clase"])
# → Diccionarios avanzados
```

> 💡 La misma sintaxis sirve para agregar y para modificar. Si la clave ya existe, sobreescribe el valor; si no existe, la crea.

### Mutar un valor de tipo lista — `append()`

Cuando el valor de una clave es una lista, podés llamar sus métodos directamente. La lista se modifica **in-place** dentro del diccionario.

```python
dic1 = {
    "clave1": ["a", "b", "c"],
    "clave2": ["d", "e", "f"],
}

# Agregar una nueva clave con lista
dic1["clave3"] = ["g", "h", "i"]
print(dic1)
# → {'clave1': ['a', 'b', 'c'], 'clave2': ['d', 'e', 'f'], 'clave3': ['g', 'h', 'i']}

# Mutar la lista de clave3 con append()
dic1["clave3"].append("j")
print(dic1)
# → {'clave1': ['a', 'b', 'c'], 'clave2': ['d', 'e', 'f'], 'clave3': ['g', 'h', 'i', 'j']}
```

> 💡 `dic1["clave3"].append("j")` no reemplaza el valor; modifica la lista existente. Es la misma lista, solo con un elemento más.

---

## 5. Listar Claves, Valores y Pares — `keys()`, `values()`, `items()`

Tres métodos para inspeccionar el contenido de un diccionario:

### `keys()` — lista las claves

```python
mi_diccionario = {"curso": "Python TOTAL", "clase": "Diccionarios"}

print(mi_diccionario.keys())
# → dict_keys(['curso', 'clase'])
```

### `values()` — lista los valores

```python
print(mi_diccionario.values())
# → dict_values(['Python TOTAL', 'Diccionarios'])
```

### `items()` — lista los pares clave:valor

```python
print(mi_diccionario.items())
# → dict_items([('curso', 'Python TOTAL'), ('clase', 'Diccionarios')])
```

> 💡 Estos métodos retornan vistas especiales (`dict_keys`, `dict_values`, `dict_items`). Para obtener una lista común, envolvelos con `list()`: `list(mi_diccionario.keys())`.

---

## 6. Unpacking — `*` y `**`

Python tiene el equivalente del operador spread `...` de JavaScript: `*` para listas y `**` para diccionarios.

### Listas — `*`

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Equivalente a [...lista1, ...lista2] en JS
combinada = [*lista1, *lista2]
print(combinada)  # → [1, 2, 3, 4, 5, 6]

# Agregar elementos en cualquier posición
con_extras = [0, *lista1, 99]
print(con_extras)  # → [0, 1, 2, 3, 99]
```

### Diccionarios — `**`

```python
base = {"nombre": "Juan", "edad": 20}
extras = {"peso": 80.5, "altura": 1.85}

# Equivalente a { ...base, ...extras } en JS
cliente = {**base, **extras}
print(cliente)
# → {'nombre': 'Juan', 'edad': 20, 'peso': 80.5, 'altura': 1.85}

# Sobreescribir un valor al hacer merge (gana el último)
actualizado = {**base, "edad": 25}
print(actualizado)
# → {'nombre': 'Juan', 'edad': 25}
```

### Comparación JS → Python

| JS | Python |
|----|--------|
| `[...a, ...b]` | `[*a, *b]` |
| `{ ...a, ...b }` | `{**a, **b}` |
| `{ ...obj, key: val }` | `{**obj, "key": val}` |

### Pasar diccionario como argumentos a una función

`**` también desempaqueta un diccionario como argumentos nombrados al llamar una función:

```python
def saludar(nombre, edad):
    print(f"Hola {nombre}, tenés {edad} años")

datos = {"nombre": "Juan", "edad": 20}
saludar(**datos)  # → Hola Juan, tenés 20 años
```

---

## 7. Resumen — Cheatsheet

| Operación | Código | Resultado |
|-----------|--------|-----------|
| Crear diccionario | `d = {"a": 1, "b": 2}` | Dict con 2 pares |
| Acceder a un valor | `d["a"]` | `1` |
| Acceder con seguridad | `d.get("c")` | `None` (sin error) |
| Agregar o modificar | `d["c"] = 3` | Agrega o sobreescribe |
| Acceder a lista anidada | `d["lista"][1]` | Elemento en índice 1 |
| Acceder a dict anidado | `d["sub"]["clave"]` | Valor en dict interno |
| Encadenar método string | `d["lista"][0].upper()` | String en mayúsculas |
| Mutar lista anidada | `d["lista"].append("x")` | Agrega al final in-place |
| Listar claves | `d.keys()` | `dict_keys([...])` |
| Listar valores | `d.values()` | `dict_values([...])` |
| Listar pares | `d.items()` | `dict_items([...])` |
| Convertir a lista | `list(d.keys())` | Lista común |
| Merge de dicts | `{**d1, **d2}` | Dict combinado |
| Merge con override | `{**d, "k": v}` | Dict con clave sobreescrita |
| Merge de listas | `[*l1, *l2]` | Lista combinada |
| Verificar tipo | `type(d)` | `<class 'dict'>` |
