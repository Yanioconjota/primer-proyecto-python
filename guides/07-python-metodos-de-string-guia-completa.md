# Guía Completa de Métodos de String en Python

Los strings en Python tienen una gran cantidad de **métodos incorporados** que permiten analizarlos, transformarlos, dividirlos y unirlos sin necesidad de librerías externas.

> 💡 Los strings son **inmutables**: los métodos de transformación no modifican el string original, sino que retornan uno nuevo.

---

## Índice

1. [Métodos de Análisis](#1-métodos-de-análisis)
2. [Métodos de Transformación](#2-métodos-de-transformación)
3. [Métodos de Separación y Unión](#3-métodos-de-separación-y-unión)

---

## 1. Métodos de Análisis

Permiten examinar el contenido de un string sin modificarlo.

### `count()` — contar ocurrencias

Retorna cuántas veces aparece un conjunto de caracteres dentro del string.

```python
s = "Hola mundo"
print(s.count("Hola"))
# → 1

print("abracadabra".count("a"))
# → 5
```

---

### `find()` e `index()` — buscar posición

Retornan el índice de la **primera aparición** del argumento. La diferencia es su comportamiento cuando el valor no existe:

| Método    | Si no encuentra | 
|-----------|-----------------|
| `find()`  | Retorna `-1`    |
| `index()` | Lanza `ValueError` |

```python
s = "Hola mundo"

print(s.find("mundo"))    # → 5
print(s.index("mundo"))   # → 5

print(s.find("world"))    # → -1
# s.index("world")        # → ValueError: substring not found
```

---

### `rfind()` y `rindex()` — buscar desde el final

Igual que `find()` e `index()`, pero la búsqueda se realiza de **derecha a izquierda**, retornando la última ocurrencia.

```python
s = "C:/python36/python.exe"

print(s.find("/"))    # → 2   (primera ocurrencia)
print(s.rfind("/"))   # → 11  (última ocurrencia)
```

---

### `startswith()` y `endswith()` — verificar inicio y fin

Retornan `True` o `False` según si la cadena comienza o termina con el argumento dado.

```python
s = "Hola mundo"

print(s.startswith("Hola"))    # → True
print(s.endswith("mundo"))     # → True
print(s.endswith("world"))     # → False
```

> 💡 Muy útiles para validar extensiones de archivos, prefijos de rutas, etc.

---

### `isdigit()`, `isnumeric()` e `isdecimal()` — verificar si es número

Las tres verifican si todos los caracteres de la cadena son numéricos, pero con distintos niveles de restricción:

| Método        | Acepta                                         |
|---------------|------------------------------------------------|
| `isdecimal()` | Solo dígitos del `0` al `9` (más restrictivo)  |
| `isdigit()`   | Dígitos y caracteres numéricos de otros idiomas |
| `isnumeric()` | Todo lo anterior + fracciones y símbolos numéricos (más amplio) |

```python
print("1234".isnumeric())      # → True
print("1234".isdecimal())      # → True
print("abc123".isdigit())      # → False
```

---

### Otros métodos de verificación

```python
# Todos los caracteres son alfanuméricos (letras + números)
print("abc123".isalnum())      # → True

# Todos los caracteres son alfabéticos
print("abcdef".isalpha())      # → True
print("abc123".isalpha())      # → False

# Todas las letras son minúsculas
print("abcdef".islower())      # → True

# Todas las letras son mayúsculas
print("ABCDEF".isupper())      # → True

# La cadena contiene solo caracteres imprimibles
print("Hola \t mundo!".isprintable())  # → False

# La cadena contiene solo espacios
print("Hola mundo".isspace())  # → False
print(" ".isspace())           # → True
```

### `isidentifier()` — verificar si es un identificador válido

Retorna `True` si la cadena puede ser un nombre de variable válido en Python (letras, dígitos y guiones bajos, sin comenzar con dígito).

```python
print("mi_variable".isidentifier())   # → True
print("2nombre".isidentifier())       # → False
print("class".isidentifier())         # → True  (palabras reservadas también pasan)
```

### `istitle()` — verificar formato título

Retorna `True` si cada palabra comienza con mayúscula y el resto son minúsculas.

```python
print("Hola Mundo".istitle())   # → True
print("Hola mundo".istitle())   # → False
print("HOLA MUNDO".istitle())   # → False
```

---

## 2. Métodos de Transformación

Retornan un **nuevo string** con la transformación aplicada. El original no se modifica.

### `capitalize()` — primera letra en mayúscula

```python
print("hola mundo".capitalize())
# → Hola mundo
```

---

### `lower()` y `upper()` — minúsculas y mayúsculas

```python
print("Hola Mundo!".lower())   # → hola mundo!
print("Hola Mundo!".upper())   # → HOLA MUNDO!
```

---

### `swapcase()` — invertir mayúsculas y minúsculas

```python
print("Hola Mundo!".swapcase())
# → hOLA mUNDO!
```

---

### `title()` — formato título

Primera letra de cada palabra en mayúscula, el resto en minúsculas.

```python
print("hola mundo desde python".title())  # → Hola Mundo Desde Python
print("hola_mundo".title())               # → Hola_Mundo
```

---

### `casefold()` — minúsculas para comparaciones multiidioma

Versión más agresiva que `lower()`, diseñada para comparaciones sin distinción de mayúsculas en múltiples idiomas.

```python
print("Straße".casefold())   # → strasse
print("Straße".lower())      # → straße

# Útil para comparar cadenas independientemente del idioma:
print("Straße".casefold() == "strasse".casefold())   # → True
```

---

### `strip()`, `lstrip()` y `rstrip()` — eliminar espacios

Remueven los espacios en blanco (u otros caracteres indicados) al inicio, al final, o en ambos extremos.

```python
s = " Hola mundo! "

print(s.strip())    # → Hola mundo!   (ambos lados)
print(s.rstrip())   # →  Hola mundo!  (solo derecha)
print(s.lstrip())   # → Hola mundo!   (solo izquierda)

# Con argumento: elimina esos caracteres de los extremos
print("***Hola***".strip("*"))   # → Hola
```

---

### `removeprefix()` y `removesuffix()` *(Python 3.9+)*

Eliminan un prefijo o sufijo exacto. A diferencia de `lstrip()`/`rstrip()`, el argumento se trata como subcadena exacta, no como conjunto de caracteres.

```python
print("archivo.csv".removeprefix("archivo"))   # → .csv
print("archivo.csv".removesuffix(".csv"))       # → archivo

# Si no coincide, retorna el string original
print("Hola mundo".removeprefix("Chau"))        # → Hola mundo

# Diferencia clave con lstrip():
print("__basura__ texto útil".lstrip("__basura__ "))      # → exto útil  (elimina caracteres sueltos)
print("__basura__ texto útil".removeprefix("__basura__ ")) # → texto útil (elimina exactamente ese prefijo)
```

---

### `replace()` — reemplazar texto

Reemplaza todas las ocurrencias de una subcadena por otra.

```python
s = "Hola mundo"
print(s.replace("mundo", "world"))
# → Hola world
```

---

### `center()`, `ljust()` y `rjust()` — alineación

Alinean el string dentro de un ancho dado. El segundo argumento opcional define el carácter de relleno (por defecto un espacio).

```python
print("Hola".center(10))        # →    Hola   
print("Hola".ljust(10))         # → Hola      
print("Hola".rjust(10))         # →       Hola
print("Hola".center(10, "*"))   # → ***Hola***
```

---

### `zfill()` — rellenar con ceros

Rellena con ceros a la izquierda hasta el ancho indicado. Respeta los signos `+` y `-`.

```python
print("42".zfill(6))     # → 000042
print("-42".zfill(6))    # → -00042
print("Hola".zfill(8))   # → 0000Hola
```

---

### `expandtabs()` — reemplazar tabulaciones

Reemplaza los caracteres `\t` por espacios. El argumento indica el tamaño de cada tabulación (por defecto `8`).

```python
print("col1\tcol2\tcol3".expandtabs())     # → col1    col2    col3
print("col1\tcol2".expandtabs(4))          # → col1col2
print("a\tb\tc".expandtabs(4))             # → a   b   c
```

---

### `encode()` — codificar la cadena

Codifica el string con el mapa de caracteres especificado y retorna un objeto `bytes`.

```python
print("Hola mundo".encode("utf-8"))
# → b'Hola mundo'
```

---

### `format()` y `format_map()` — interpolación

`format()` inserta valores dentro de una cadena usando `{}` como marcadores:

```python
print("Hola, {}!".format("mundo"))
# → Hola, mundo!

print("{0} + {1} = {2}".format(1, 2, 3))
# → 1 + 2 = 3

print("{nombre} tiene {edad} años".format(nombre="Ana", edad=30))
# → Ana tiene 30 años

print("{:.2f}".format(3.14159))
# → 3.14
```

`format_map()` recibe un diccionario directamente (más eficiente con objetos personalizados):

```python
datos = {"nombre": "Carlos", "edad": 25}
print("{nombre} tiene {edad} años".format_map(datos))
# → Carlos tiene 25 años
```

---

### `maketrans()` y `translate()` — reemplazos carácter a carácter

Trabajan juntos para reemplazos eficientes carácter a carácter. `maketrans()` crea la tabla de traducción y `translate()` la aplica.

```python
# Reemplazar vocales minúsculas por mayúsculas
tabla = str.maketrans("aeiou", "AEIOU")
print("hola mundo".translate(tabla))
# → hOlA mUndO

# Con diccionario (admite eliminación con None)
tabla = str.maketrans({"a": "A", "e": None, "o": "0"})
print("hola mundo".translate(tabla))
# → h0lA mund0

# Tercer argumento: caracteres a eliminar
tabla = str.maketrans("", "", "aeiou")
print("hola mundo".translate(tabla))
# → hl mnd
```

---

## 3. Métodos de Separación y Unión

### `split()` — dividir en lista

Divide el string según un separador (por defecto espacios en blanco) y retorna una lista.

```python
print("Hola mundo!\nHello world!".split())
# → ['Hola', 'mundo!', 'Hello', 'world!']

print("Hola mundo!\nHello world!".split(" "))
# → ['Hola', 'mundo!\nHello', 'world!']

# Segundo argumento: máximo de divisiones
print("Hola mundo hello world".split(" ", 2))
# → ['Hola', 'mundo', 'hello world']
```

---

### `rsplit()` — dividir desde el final

Igual que `split()`, pero las divisiones se realizan comenzando desde el final. La diferencia es visible cuando se usa `maxsplit`.

```python
print("uno dos tres cuatro".rsplit())
# → ['uno', 'dos', 'tres', 'cuatro']

print("uno dos tres cuatro".split(" ", 2))
# → ['uno', 'dos', 'tres cuatro']   (divide desde la izquierda)

print("uno dos tres cuatro".rsplit(" ", 2))
# → ['uno dos', 'tres', 'cuatro']   (divide desde la derecha)
```

---

### `splitlines()` — dividir por saltos de línea

Divide el string en cada salto de línea y retorna una lista.

```python
print("Hola mundo!\nHello world!".splitlines())
# → ['Hola mundo!', 'Hello world!']
```

---

### `partition()` y `rpartition()` — dividir en tres partes

Retornan una tupla de tres elementos: el bloque anterior al separador, el separador mismo, y el bloque posterior.

`partition()` busca de izquierda a derecha; `rpartition()`, de derecha a izquierda.

```python
s = "Hola mundo. Hello world!"

print(s.partition(" "))
# → ('Hola', ' ', 'mundo. Hello world!')

print(s.rpartition(" "))
# → ('Hola mundo. Hello', ' ', 'world!')
```

---

### `join()` — unir una lista en un string

Se llama desde el string que actúa como separador y une los elementos de una lista.

```python
print(" ".join(["Hola", "mundo"]))
# → Hola mundo

print(", ".join(["C", "C++", "Python", "Java"]))
# → C, C++, Python, Java

# Unir sin separador
print("".join(["P", "y", "t", "h", "o", "n"]))
# → Python
```

---

## Resumen General

### Métodos de análisis

| Método | Descripción | Retorna |
|--------|-------------|---------|
| `count(v)` | Número de ocurrencias de `v` | `int` |
| `find(v)` | Índice de primera ocurrencia | `int` (`-1` si no existe) |
| `index(v)` | Índice de primera ocurrencia | `int` (`ValueError` si no existe) |
| `rfind(v)` | Índice de última ocurrencia | `int` (`-1` si no existe) |
| `rindex(v)` | Índice de última ocurrencia | `int` (`ValueError` si no existe) |
| `startswith(v)` | ¿Empieza con `v`? | `bool` |
| `endswith(v)` | ¿Termina con `v`? | `bool` |
| `isdigit()` | ¿Solo dígitos? | `bool` |
| `isdecimal()` | ¿Solo dígitos decimales? | `bool` |
| `isnumeric()` | ¿Solo caracteres numéricos? | `bool` |
| `isalnum()` | ¿Solo alfanuméricos? | `bool` |
| `isalpha()` | ¿Solo letras? | `bool` |
| `islower()` | ¿Todas minúsculas? | `bool` |
| `isupper()` | ¿Todas mayúsculas? | `bool` |
| `isspace()` | ¿Solo espacios? | `bool` |
| `isprintable()` | ¿Solo imprimibles? | `bool` |
| `isidentifier()` | ¿Identificador Python válido? | `bool` |
| `istitle()` | ¿Formato título? | `bool` |

### Métodos de transformación

| Método | Descripción |
|--------|-------------|
| `capitalize()` | Primera letra en mayúscula |
| `lower()` | Todo en minúsculas |
| `upper()` | Todo en mayúsculas |
| `swapcase()` | Invierte mayúsculas/minúsculas |
| `title()` | Formato título |
| `casefold()` | Minúsculas para comparaciones multiidioma |
| `strip(c)` | Elimina `c` de ambos extremos (por defecto espacios) |
| `lstrip(c)` | Elimina `c` del extremo izquierdo |
| `rstrip(c)` | Elimina `c` del extremo derecho |
| `removeprefix(p)` | Elimina el prefijo exacto `p` *(3.9+)* |
| `removesuffix(s)` | Elimina el sufijo exacto `s` *(3.9+)* |
| `replace(a, b)` | Reemplaza `a` por `b` |
| `center(n, c)` | Centra en ancho `n` con relleno `c` |
| `ljust(n, c)` | Alinea a la izquierda en ancho `n` |
| `rjust(n, c)` | Alinea a la derecha en ancho `n` |
| `zfill(n)` | Rellena con ceros hasta ancho `n` |
| `expandtabs(n)` | Reemplaza `\t` por `n` espacios |
| `encode(enc)` | Codifica a `bytes` |
| `format(...)` | Interpolación con `{}` |
| `format_map(d)` | Interpolación desde diccionario |
| `maketrans(a, b)` | Crea tabla de traducción |
| `translate(t)` | Aplica tabla de traducción |

### Métodos de separación y unión

| Método | Descripción |
|--------|-------------|
| `split(sep, n)` | Divide por `sep` (máx. `n` veces) desde la izquierda |
| `rsplit(sep, n)` | Divide por `sep` (máx. `n` veces) desde la derecha |
| `splitlines()` | Divide por saltos de línea |
| `partition(sep)` | Divide en 3: antes, `sep`, después (desde izquierda) |
| `rpartition(sep)` | Divide en 3: antes, `sep`, después (desde derecha) |
| `join(lista)` | Une elementos de `lista` con el string como separador |
