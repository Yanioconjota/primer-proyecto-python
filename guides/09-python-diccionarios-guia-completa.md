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
3. [Agregar y Modificar Datos](#3-agregar-y-modificar-datos)
4. [Listar Claves, Valores y Pares — `keys()`, `values()`, `items()`](#4-listar-claves-valores-y-pares--keys-values-items)
5. [Resumen — Cheatsheet](#5-resumen--cheatsheet)

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

## 3. Agregar y Modificar Datos

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

---

## 4. Listar Claves, Valores y Pares — `keys()`, `values()`, `items()`

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

## 5. Resumen — Cheatsheet

| Operación | Código | Resultado |
|-----------|--------|-----------|
| Crear diccionario | `d = {"a": 1, "b": 2}` | Dict con 2 pares |
| Acceder a un valor | `d["a"]` | `1` |
| Acceder con seguridad | `d.get("c")` | `None` (sin error) |
| Agregar o modificar | `d["c"] = 3` | Agrega o sobreescribe |
| Listar claves | `d.keys()` | `dict_keys(['a', 'b'])` |
| Listar valores | `d.values()` | `dict_values([1, 2])` |
| Listar pares | `d.items()` | `dict_items([('a',1), ('b',2)])` |
| Verificar tipo | `type(d)` | `<class 'dict'>` |
