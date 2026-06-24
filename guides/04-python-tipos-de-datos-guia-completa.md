# Guía Completa de Tipos de Datos en Python

En Python, cada dato tiene un **tipo**. El tipo determina qué puedes hacer con ese dato: si puedes sumarlo, multiplicarlo, acceder a partes de él, etc. Reconocer los tipos es fundamental para entender cómo funciona tu código.

> 💡 Puedes verificar el tipo de cualquier dato usando `type()`. Por ejemplo: `print(type("hola"))` muestra `<class 'str'>`.

---

## 1. Tipos Simples

Estos tipos almacenan un solo valor. Son los más básicos y los que usarás con más frecuencia.

### `str` — String (Texto)

Texto. Cualquier cosa entre comillas es un string: palabras, frases, símbolos, o incluso números escritos como texto.

```python
"hola"    "%$&"    " "    "123"    'Python'
```

> 🔑 **Se reconoce por:** las comillas (simples o dobles)

---

### `int` — Integer (Entero)

Números enteros. Sin decimales. Pueden ser positivos, negativos o cero.

```python
150    1    555    -15    0
```

> 🔑 **Se reconoce por:** número sin punto decimal ni comillas

---

### `float` — Float (Decimal)

Números decimales. También llamados "de punto flotante". Siempre tienen un punto.

```python
1.25    25.0    500.50    -95.1    3.14159
```

> 🔑 **Se reconoce por:** tiene punto decimal

---

### `bool` — Boolean (Booleano)

Verdadero o Falso. Solo tiene dos valores posibles. Se usa para condiciones y decisiones.

```python
True    False
```

> 🔑 **Se reconoce por:** solo puede ser `True` o `False` (con mayúscula inicial)

---

> 💡 **¿`"123"` vs `123`?**
> `"123"` es un string (texto) porque tiene comillas. `123` es un int (número) porque no tiene comillas. Esto importa: `"5" + "3"` da `"53"`, pero `5 + 3` da `8`.

---

## 2. Colecciones

Estos tipos pueden almacenar **múltiples valores**. Son como "contenedores" que guardan otros datos.

### `list` — Lista

Colección **ordenada y modificable**. Puede contener cualquier tipo de dato, incluso mezclados. Puedes agregar, quitar o cambiar elementos.

```python
["sal", 1, -3, 4.5, "marte", 0]
```

> 🔑 **Se reconoce por:** corchetes `[ ]`

---

### `tuple` — Tupla

Colección **ordenada e inmutable**. Similar a la lista, pero una vez creada no se puede modificar. Ideal para datos que no deben cambiar.

```python
("lun", "mar", "mie", "jue", "vie")
```

> 🔑 **Se reconoce por:** paréntesis `( )`

---

### `dict` — Diccionario

Colección de **pares clave:valor**. Como un diccionario real: buscas por la "palabra" (clave) y obtienes su "definición" (valor).

```python
{"color": "rojo", "arte": "cine"}
```

> 🔑 **Se reconoce por:** llaves `{ }` con pares clave:valor separados por dos puntos

---

### `set` — Conjunto

Colección **sin duplicados y sin orden**. Automáticamente elimina valores repetidos. Útil para encontrar elementos únicos.

```python
{"a", "b", "c", "d", "e"}
```

> 🔑 **Se reconoce por:** llaves `{ }` pero SIN dos puntos (a diferencia del diccionario)

---

> ⚠️ **¿Set o Diccionario?** Ambos usan llaves `{ }`, pero el diccionario tiene dos puntos entre clave y valor: `{"clave": "valor"}`. El set solo tiene valores sueltos: `{"a", "b", "c"}`.

---

## 3. Tabla Comparativa

### Cómo reconocer cada tipo

| Tipo    | Símbolo clave         | Ejemplo       |
|---------|-----------------------|---------------|
| `str`   | Comillas `" "` o `' '` | `"hola"`     |
| `int`   | Número sin punto      | `42`          |
| `float` | Número con punto      | `3.14`        |
| `bool`  | `True` / `False`      | `True`        |
| `list`  | Corchetes `[ ]`       | `[1, 2, 3]`  |
| `tuple` | Paréntesis `( )`      | `(1, 2, 3)`  |
| `dict`  | Llaves con `:`        | `{"a": 1}`   |
| `set`   | Llaves sin `:`        | `{1, 2, 3}`  |

### Características de las colecciones

| Tipo    | Ordenado | Modificable | Duplicados      |
|---------|----------|-------------|-----------------|
| `list`  | ✓ Sí     | ✓ Sí        | ✓ Permite       |
| `tuple` | ✓ Sí     | ✗ No        | ✓ Permite       |
| `dict`  | ✓ Sí *   | ✓ Sí        | ✗ Claves únicas |
| `set`   | ✗ No     | ✓ Sí        | ✗ No permite    |

> \* Los diccionarios mantienen el orden de inserción desde Python 3.7

---

## 4. Verificar el Tipo con `type()`

Si tienes dudas sobre qué tipo de dato es algo, usa `type()` para averiguarlo.

```python
print(type("hola"))
# → <class 'str'>

print(type(42))
# → <class 'int'>

print(type(3.14))
# → <class 'float'>

print(type(True))
# → <class 'bool'>

print(type([1, 2, 3]))
# → <class 'list'>

print(type((1, 2, 3)))
# → <class 'tuple'>

print(type({"a": 1}))
# → <class 'dict'>

print(type({1, 2, 3}))
# → <class 'set'>
```
