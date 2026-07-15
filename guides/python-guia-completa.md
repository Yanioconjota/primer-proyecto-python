# Python — Guía Completa de Referencia

Guía unificada de referencia rápida para aprender Python desde cero.

---

## Índice

- [01 · `print()`](#01-print)
- [02 · Strings](#02-strings)
- [03 · `input()`](#03-input)
- [04 · Tipos de Datos](#04-tipos-de-datos)
- [05 · Variables](#05-variables)
- [06 · Integers y Floats](#06-integers-y-floats)
- [07 · Métodos de String](#07-metodos-de-string)
- [08 · Listas](#08-listas)
- [09 · Diccionarios](#09-diccionarios)
- [10 · Tuples](#10-tuples)
- [11 · Sets](#11-sets)
- [12 · Booleanos](#12-booleanos)
- [13 · Operadores de Comparación](#13-operadores-de-comparacion)
- [14 · Operadores](#14-operadores)
- [15 · Control de Flujo — `if` / `elif` / `else`](#15-control-de-flujo-if-elif-else)
- [16 · `match` / `case`](#16-match-case)
- [Preguntas y Respuestas del Curso](#preguntas-y-respuestas-del-curso)

---

## 01 · `print()`

`print()` es la primera instrucción que aprendes en Python. Su trabajo es simple: mostrar texto o números en la pantalla.

> 💡 Todo lo que pongas dentro de los paréntesis de `print()` aparecerá en la consola de Python.

---

### 1. Lo Básico

#### Mostrar texto

Para mostrar texto, escríbelo entre comillas dentro de los paréntesis.

```python
print("Hola, mundo")
# → Hola, mundo

print("Bienvenido a Python")
# → Bienvenido a Python

print("¡Esto es muy fácil!")
# → ¡Esto es muy fácil!
```

#### Mostrar números

Los números van sin comillas. Python los reconoce automáticamente.

```python
print(42)
# → 42

print(3.14159)
# → 3.14159

print(10 + 5)
# → 15

print(100 / 4)
# → 25.0
```

#### Línea vacía

Si usas `print()` sin nada adentro, imprime una línea en blanco.

```python
print("Primera línea")
print()
print("Segunda línea")
# → Primera línea
# →
# → Segunda línea
```

---

### 2. Comillas Simples y Dobles

#### Ambas funcionan igual

Python acepta comillas simples `'texto'` o dobles `"texto"`.

```python
print("Hola")   # → Hola
print('Hola')   # → Hola
```

#### Cuando el texto tiene comillas

```python
print("Él dijo 'hola' y se fue")
# → Él dijo 'hola' y se fue

print('Ella respondió "adiós"')
# → Ella respondió "adiós"
```

> 💡 **Tip:** La mayoría de programadores usan comillas dobles `"texto"` por costumbre. Lo importante es ser consistente.

---

### 3. Imprimir Varias Cosas a la Vez

#### Separar con comas

Puedes poner varios elementos separados por comas. Python los imprime con un espacio entre cada uno.

```python
print("Hola", "mundo")
# → Hola mundo

print("El resultado es:", 42)
# → El resultado es: 42

print("Suma:", 10, "+", 5, "=", 15)
# → Suma: 10 + 5 = 15
```

#### Cambiar el separador con `sep`

```python
print("A", "B", "C")           # → A B C
print("A", "B", "C", sep="-")  # → A-B-C
print("A", "B", "C", sep="")   # → ABC
print(2024, 12, 25, sep="/")   # → 2024/12/25
print(14, 30, 00, sep=":")     # → 14:30:0
```

---

### 4. Controlar los Saltos de Línea

#### Comportamiento normal

Cada `print()` termina con un salto de línea automático.

```python
print("Línea 1")
print("Línea 2")
print("Línea 3")
```

#### Cambiar el final con `end`

```python
print("Hola", end=" ")
print("mundo")
# → Hola mundo

print("Cargando", end="...")
print("Listo")
# → Cargando...Listo

print("A", end="")
print("B", end="")
print("C")
# → ABC
```

---

### 5. Caracteres Especiales

#### Secuencias de escape

```python
# \n = Nueva línea
print("Primera línea\nSegunda línea")

# \t = Tabulación
print("Nombre:\tJuan")
print("Edad:\t25")

# \\ = Barra invertida
print("Carpeta: C:\\Usuarios\\Juan")
```

| Secuencia | Significado      | Ejemplo                          |
|-----------|-----------------|----------------------------------|
| `\n`      | Nueva línea     | `"Hola\nMundo"` → Hola / Mundo   |
| `\t`      | Tabulación      | `"A\tB"` → A &nbsp;&nbsp;&nbsp; B |
| `\\`      | Barra invertida | `"C:\\ruta"` → C:\ruta           |
| `\"`      | Comilla doble   | `"Dijo \"hola\""` → Dijo "hola"  |
| `\'`      | Comilla simple  | `'It\'s ok'` → It's ok          |

---

### 6. Texto en Varias Líneas

#### Comillas triples

```python
print("""
Bienvenido al sistema.
Por favor, siga las instrucciones.
Gracias por su visita.
""")
```

#### Crear menús o arte ASCII

```python
print("""
╔═══════════════════════╗
║    MI PROGRAMA        ║
║                       ║
║  1. Opción uno        ║
║  2. Opción dos        ║
║  3. Salir             ║
╚═══════════════════════╝
""")
```

> 💡 Las comillas triples pueden ser dobles `"""texto"""` o simples `'''texto'''`. Ambas funcionan igual.

---

*Fuente: [Claude Artifact](https://claude.ai/public/artifacts/fc8b5048-b427-47e5-9601-123d52233c5e)*

---

## 02 · Strings

Un **string** (o cadena de texto) es simplemente texto en Python. Puede ser una palabra, una frase, un párrafo, o incluso un solo carácter. Los strings son uno de los tipos de datos más usados en programación.

> 💡 En Python, cualquier texto entre comillas es un string: `"Hola"`, `'Python'`, `"123"` (sí, los números entre comillas también son texto).

---

### Propiedades de los Strings

Esto es lo que debes tener presente al trabajar con strings en Python:

| Propiedad | Descripción |
|-----------|-------------|
| **Inmutables** | Una vez creados, sus partes no pueden modificarse directamente. Los métodos de string no alteran el original: retornan uno nuevo. |
| **Concatenables** | Se pueden unir con el operador `+`. |
| **Multiplicables** | Se pueden repetir con el operador `*`. |
| **Multilineales** | Pueden escribirse en varias líneas encerrándolos entre triples comillas simples `''' '''` o dobles `""" """`. |
| **Tienen longitud** | Se puede medir con `len(mi_string)`. |
| **Verificables** | Se puede comprobar si contienen una subcadena con `in` y `not in` (retornan `True` o `False`). |

> Ver también: [Guía de Métodos de String](#07-metodos-de-string) para el listado completo de operaciones disponibles.

---

### 1. Crear Strings

#### Texto entre comillas

Para crear un string, solo escribe texto entre comillas simples o dobles.

```python
# Con comillas dobles
print("Hola, mundo")
# → Hola, mundo

# Con comillas simples
print('Bienvenido a Python')
# → Bienvenido a Python

# Un solo carácter también es un string
print("A")
# → A

# String vacío (sin caracteres)
print("")
# → (nada)
```

#### Números como texto

Si pones números entre comillas, Python los trata como texto, no como números.

```python
# Esto es un número
print(42 + 8)
# → 50

# Esto es texto (no se puede sumar matemáticamente)
print("42" + "8")
# → 428 (los une como texto)
```

> ⚠️ **Error común:** poner números entre comillas sin querer. `"42" + "8"` da `"428"` (concatenación), no `50` (suma).

---

### 2. Comillas Simples vs Dobles

Ambas funcionan igual. La elección es tuya.

```python
print("Hola")
# → Hola

print('Hola')
# → Hola
```

#### Cuando el texto tiene comillas

Si tu texto incluye un tipo de comillas, usa el otro tipo para encerrarlo.

```python
# El texto tiene comillas simples → usa dobles afuera
print("Él dijo 'hola' y se fue")
# → Él dijo 'hola' y se fue

# El texto tiene comillas dobles → usa simples afuera
print('Ella respondió "adiós"')
# → Ella respondió "adiós"

# O usa la barra invertida para "escapar" la comilla
print("Él dijo \"hola\" y se fue")
# → Él dijo "hola" y se fue
```

---

### 3. Strings Multilínea

#### Comillas triples

Para texto que ocupa varias líneas, usa tres comillas al inicio y al final.

```python
print("""Este es un texto
que ocupa varias
líneas.""")

# → Este es un texto
# → que ocupa varias
# → líneas.
```

#### Crear diseños con texto

Las comillas triples son perfectas para arte ASCII o menús.

```python
print("""
    *****
   *     *
  *  ^ ^  *
  *  (o)  *
   *     *
    *****
""")
```

---

### 4. Caracteres Especiales

#### Secuencias de escape

Algunos caracteres no se pueden escribir directamente. Se usan secuencias que empiezan con `\`.

```python
# \n = Nueva línea
print("Primera\nSegunda")
# → Primera
# → Segunda

# \t = Tabulación
print("Nombre:\tJuan")
# → Nombre:    Juan

# \\ = Barra invertida
print("C:\\Usuarios\\Juan")
# → C:\Usuarios\Juan
```

#### Tabla de secuencias de escape

| Secuencia | Resultado      | Uso común                          |
|-----------|----------------|------------------------------------|
| `\n`      | Nueva línea    | Saltar a la siguiente línea        |
| `\t`      | Tabulación     | Alinear texto en columnas          |
| `\\`      | Barra `\`      | Rutas de Windows                   |
| `\"`      | Comilla `"`    | Comillas dentro del texto          |
| `\'`      | Comilla `'`    | Apóstrofes dentro del texto        |

---

### 5. Unir Strings (Concatenación)

#### Usar el signo `+`

Puedes unir dos o más strings usando el operador `+`.

```python
print("Hola" + "Mundo")
# → HolaMundo

# Agrega espacios si los necesitas
print("Hola" + " " + "Mundo")
# → Hola Mundo

# Puedes unir muchos strings
print("A" + "B" + "C" + "D")
# → ABCD
```

> ⚠️ **Cuidado:** No puedes concatenar strings con números directamente. `"Tengo " + 5` dará error. Más adelante aprenderás cómo resolver esto.

---

### 6. Repetir Strings

#### Usar el signo `*`

Puedes repetir un string multiplicándolo por un número.

```python
print("Ja" * 3)
# → JaJaJa

print("=" * 20)
# → ====================

print("-*" * 10)
# → -*-*-*-*-*-*-*-*-*-*

# Útil para crear separadores
print("TÍTULO")
print("─" * 15)
# → TÍTULO
# → ───────────────
```

---

### 7. Acceder a Caracteres

#### Índices (posiciones)

Cada carácter en un string tiene una posición llamada **índice**. El primer carácter está en la posición `0`.

```
P  y  t  h  o  n
0  1  2  3  4  5
```

```python
# Acceder al primer carácter (índice 0)
print("Python"[0])
# → P

# Acceder al segundo carácter (índice 1)
print("Python"[1])
# → y

# Acceder al último carácter (índice 5)
print("Python"[5])
# → n
```

#### Índices negativos

También puedes contar desde el final usando números negativos. `-1` es el último carácter.

```
P   y   t   h   o   n
-6  -5  -4  -3  -2  -1
```

```python
# Último carácter
print("Python"[-1])
# → n

# Penúltimo carácter
print("Python"[-2])
# → o

# Primer carácter (desde el final)
print("Python"[-6])
# → P
```

> 💡 **¿Por qué empieza en 0?** En programación, los índices suelen empezar en 0, no en 1. Es una convención que viene de cómo las computadoras manejan la memoria.

---

### 8. Extraer Partes (Slicing)

#### Sintaxis completa

Las substrings se extraen con la técnica de **slicing** (*rebanar*). La sintaxis completa acepta tres parámetros:

```python
string[start:stop:step]
```

| Parámetro | Descripción |
|-----------|-------------|
| `start`   | Índice de inicio — **incluido** (por defecto: inicio del string) |
| `stop`    | Índice de fin — **no incluido** (por defecto: fin del string) |
| `step`    | Paso — cada cuántos caracteres avanzar (por defecto: `1`) |

#### Cortar un pedazo del string

```python
# Desde índice 0 hasta índice 3 (sin incluir el 3)
print("Python"[0:3])
# → Pyt

# Desde índice 2 hasta índice 5
print("Python"[2:5])
# → tho

# Desde el inicio hasta índice 4
print("Python"[:4])
# → Pyth

# Desde índice 2 hasta el final
print("Python"[2:])
# → thon
```

#### Usar el paso (`step`)

El tercer parámetro define cada cuántos caracteres avanzar.

```python
saludo = "Hola_Mundo"
#índices: 0123456789

# Desde índice 2 hasta 6 → "la_M"
print(saludo[2:6])
# → la_M

# Desde índice 3 hasta el final, de 3 en 3 → "auo"
print(saludo[3::3])
# → auo

# Paso negativo: recorre el string al revés
print(saludo[::-1])
# → odnuM_aloH
```

> 💡 `[::-1]` es el truco clásico para invertir un string en Python.

#### Ejemplos prácticos

```python
# Extraer extensión de archivo
print("documento.pdf"[-3:])
# → pdf

# Extraer código de país
print("+54 11 1234-5678"[:3])
# → +54

# Extraer las primeras 5 letras
print("Bienvenidos al curso"[:5])
# → Bienv

# Tomar un carácter de cada dos
print("P-y-t-h-o-n"[::2])
# → Python
```

#### Tabla de sintaxis de slicing

| Sintaxis   | Significado                          | Ejemplo con `"Python"` |
|------------|--------------------------------------|------------------------|
| `[n]`      | Carácter en posición n               | `[2]` → `"t"`          |
| `[a:b]`    | Desde a hasta b (sin incluir b)      | `[1:4]` → `"yth"`      |
| `[:b]`     | Desde el inicio hasta b              | `[:3]` → `"Pyt"`       |
| `[a:]`     | Desde a hasta el final               | `[3:]` → `"hon"`       |
| `[-n]`     | n-ésimo carácter desde el final      | `[-1]` → `"n"`         |
| `[a:b:s]`  | Desde a hasta b con paso s           | `[0:6:2]` → `"Pto"`    |
| `[::-1]`   | String invertido                     | `[::-1]` → `"nohtyP"`  |

---

### 9. Longitud de un String

#### Contar caracteres con `len()`

`len()` te dice cuántos caracteres tiene un string (incluyendo espacios).

```python
print(len("Hola"))
# → 4

print(len("Python"))
# → 6

# Los espacios también cuentan
print(len("Hola Mundo"))
# → 10

# String vacío tiene longitud 0
print(len(""))
# → 0
```

> 💡 **Relación entre `len()` e índices:** Si un string tiene longitud 6, sus índices van de `0` a `5` (no de 1 a 6). El último índice siempre es `len() - 1`.

---

### 10. Formatear Cadenas

Para facilitar la concatenación de variables y texto en Python, contamos con dos herramientas que nos evitan manipular las variables para incorporarlas directamente al texto.

#### Función `.format()`

Se encierran las posiciones de las variables entre llaves `{}`, y a continuación del string se llama a las variables con `.format()`.

```python
color_auto = "rojo"
matricula = "ABC 123"

print("Mi auto es {} y de matrícula {}".format(color_auto, matricula))
# → Mi auto es rojo y de matrícula ABC 123
```

También puedes usar índices o nombres dentro de las llaves para mayor claridad:

```python
# Con índices
print("El {0} cuesta ${1} y el {0} es bueno".format("producto", 99))
# → El producto cuesta $99 y el producto es bueno

# Con nombres
print("Hola, {nombre}. Tienes {edad} años.".format(nombre="Ana", edad=30))
# → Hola, Ana. Tienes 30 años.
```

#### Cadenas literales — f-strings

A partir de Python 3.8, puedes anticipar la concatenación de variables anteponiendo `f` al string y escribiendo las variables directamente dentro de `{}`.

```python
color_auto = "rojo"
matricula = "ABC 123"

print(f"Mi auto es {color_auto} y de matrícula {matricula}")
# → Mi auto es rojo y de matrícula ABC 123
```

Las f-strings también admiten expresiones dentro de las llaves:

```python
nombre = "Carlos"
edad = 25

print(f"Hola, {nombre}. El año que viene tendrás {edad + 1} años.")
# → Hola, Carlos. El año que viene tendrás 26 años.

precio = 19.99
print(f"Total con IVA: ${precio * 1.21:.2f}")
# → Total con IVA: $24.19
```

#### Comparativa

| Método         | Sintaxis                                      | Disponible desde |
|----------------|-----------------------------------------------|------------------|
| Concatenación  | `"Hola " + nombre`                            | Siempre          |
| `.format()`    | `"Hola {}".format(nombre)`                    | Python 2.6+      |
| f-string       | `f"Hola {nombre}"`                            | Python 3.6+      |

> 💡 **¿Cuál usar?** Las **f-strings** son la forma moderna y recomendada: más cortas, legibles y rápidas. Usa `.format()` solo si necesitas compatibilidad con versiones antiguas de Python.

---

### 11. Buscar la Posición de un Carácter — `index()` y `rindex()`

#### `index()` — buscar de izquierda a derecha

Devuelve el índice de la **primera aparición** de un carácter o cadena dentro de un string.

```python
string.index(value, start, end)
```

| Parámetro | Descripción |
|-----------|-------------|
| `value`   | Carácter(es) a buscar (obligatorio) |
| `start`   | Índice desde donde empezar (opcional). Las apariciones antes de `start` se ignoran |
| `end`     | Índice donde terminar (opcional). Las apariciones después de `end` se ignoran |

```python
texto = "programación"

print(texto.index("a"))
# → 4  (primera "a" que encuentra)

print(texto.index("a", 5))
# → 7  (ignora las "a" antes del índice 5)

print(texto.index("a", 5, 9))
# → 7  (busca solo entre índices 5 y 9)
```

> ⚠️ Si el valor no existe en el string, `index()` lanza un `ValueError`. Para evitar el error puedes usar `find()`, que devuelve `-1` si no lo encuentra.

#### `rindex()` — buscar de derecha a izquierda

Igual que `index()`, pero la búsqueda se hace en **sentido inverso** y devuelve la última aparición.

```python
texto = "programación"

print(texto.rindex("a"))
# → 7  (última "a" del string)

print(texto.rindex("a", 0, 6))
# → 4  (última "a" buscando solo entre índices 0 y 6)
```

#### Acceder al carácter en un índice conocido

Una vez que tienes el índice, puedes acceder al carácter con `string[i]`:

```python
texto = "Python"
i = texto.index("t")   # → 2
print(texto[i])        # → t
```

> 💡 **Recordá:** el índice en primera posición es siempre `0`.

#### Comparativa `index()` vs `rindex()` vs `find()`

| Método      | Dirección | Si no encuentra |
|-------------|-----------|-----------------|
| `index(v)`  | → derecha | Lanza `ValueError` |
| `rindex(v)` | ← izquierda | Lanza `ValueError` |
| `find(v)`   | → derecha | Devuelve `-1` |

---

### 12. Verificar Contenido — `in` y `not in`

Los operadores `in` y `not in` permiten comprobar si una subcadena existe dentro de un string. El resultado es siempre un booleano (`True` o `False`).

```python
print("mundo" in "Hola mundo")      # → True
print("Python" in "Hola mundo")     # → False

print("Python" not in "Hola mundo") # → True
print("Hola" not in "Hola mundo")   # → False
```

#### Uso con variables

```python
mensaje = "Bienvenido al curso de Python"

if "Python" in mensaje:
    print("El mensaje menciona Python")
# → El mensaje menciona Python
```

#### Distinción entre mayúsculas y minúsculas

`in` es sensible a mayúsculas:

```python
print("python" in "Hola Python")    # → False
print("Python" in "Hola Python")    # → True

# Para ignorar mayúsculas, normaliza primero con lower()
print("python" in "Hola Python".lower())  # → True
```

> 💡 `in` también funciona con listas, tuplas y otros iterables en Python, no solo con strings.

---

### Resumen General

| Operación           | Sintaxis                  | Ejemplo                          |
|---------------------|---------------------------|----------------------------------|
| Crear string        | `"texto"` o `'texto'`     | `"Hola"`                         |
| Multilínea          | `"""texto"""`             | `"""línea1\nlínea2"""`           |
| Concatenar          | `str1 + str2`             | `"Hola" + " Mundo"`              |
| Repetir             | `str * n`                 | `"=" * 10`                       |
| Acceder carácter    | `str[i]`                  | `"Python"[0]` → `"P"`           |
| Índice negativo     | `str[-i]`                 | `"Python"[-1]` → `"n"`          |
| Slicing             | `str[a:b]`                | `"Python"[1:4]` → `"yth"`       |
| Longitud            | `len(str)`                | `len("Hola")` → `4`             |
| format()            | `"Hola {}".format(var)`   | `"Mi auto es rojo"`              |
| f-string            | `f"Hola {var}"`           | `"Mi auto es rojo"`              |
| Buscar posición     | `str.index(v)`            | `"Python".index("t")` → `2`     |
| Buscar inverso      | `str.rindex(v)`           | `"Python".rindex("t")` → `2`    |

---

## 03 · `input()`

`input()` es lo que hace que tus programas sean **interactivos**. En lugar de que todo esté escrito de antemano, puedes pedirle información al usuario mientras el programa corre.

> 💡 Con `input()` tu programa puede preguntar "¿Cómo te llamas?" y luego usar la respuesta del usuario.

---

### 1. ¿Qué hace `input()`?

#### Pedir datos al usuario

`input()` pausa el programa, muestra un mensaje, y espera a que el usuario escriba algo y presione Enter.

```
Muestra el mensaje → Espera que el usuario escriba → Usuario presiona Enter → Devuelve lo que escribió
```

```python
# Pide el nombre y lo muestra inmediatamente
print(input("¿Cómo te llamas? "))
```

```
¿Cómo te llamas? María
María
```

> 💡 **Nota sobre el espacio:** Agrega un espacio al final del mensaje `"¿Tu nombre? "` para que el cursor no quede pegado al texto. Es más fácil de leer para el usuario.

---

### 2. La Sintaxis de `input()`

#### Estructura básica

Dentro de los paréntesis va el mensaje que verá el usuario. Este mensaje es opcional, pero casi siempre lo usamos.

```python
# Con mensaje (lo más común)
print(input("Escribe algo: "))

# Sin mensaje (solo espera que escribas)
print(input())
```

#### Diferentes tipos de preguntas

El mensaje puede ser cualquier texto que ayude al usuario a saber qué escribir.

```python
# Preguntas claras y directas
print(input("¿Cuál es tu nombre? "))
print(input("Ingresa tu edad: "))
print(input("¿En qué ciudad vives? "))

# Instrucciones
print(input("Escribe un número del 1 al 10: "))
print(input("Presiona Enter para continuar..."))
```

---

### 3. `input()` Siempre Devuelve Texto

#### Todo es un string

No importa lo que el usuario escriba, `input()` siempre lo devuelve como texto (string). Incluso si escribe números.

```python
# Aunque el usuario escriba "25", es texto, no número
print(type(input("Tu edad: ")))
```

```
Tu edad: 25
<class 'str'>
```

Dice `'str'` (string = texto), no `'int'` (integer = número entero).

> ⚠️ **Error común de principiantes:** Si pides un número y tratas de sumarle algo, no funcionará como esperas porque es texto. `"5" + "3"` da `"53"`, no `8`.

---

### 4. Combinar `input()` con Texto

#### Concatenar la respuesta

Puedes unir lo que el usuario escribe con otro texto usando `+`.

```python
# Saludo personalizado
print("¡Hola, " + input("¿Cómo te llamas? ") + "!")
```

```
¿Cómo te llamas? Carlos
¡Hola, Carlos!
```

#### Más ejemplos de concatenación

```python
# Bienvenida
print("Bienvenido a " + input("¿A qué ciudad viajas? "))

# Despedida
print("Hasta luego, " + input("Tu nombre: ") + ". ¡Vuelve pronto!")

# Confirmación
print("Tu correo es: " + input("Email: "))
```

---

### 5. Convertir a Números

#### `int()` para números enteros

Si necesitas hacer cálculos, convierte el texto a número con `int()`.

```python
# Sin convertir: concatena como texto
print(input("Número: ") + input("Otro número: "))
```

```
Número: 5
Otro número: 3
53  ← ¡Los unió como texto!
```

```python
# Convertido con int(): suma como números
print(int(input("Número: ")) + int(input("Otro número: ")))
```

```
Número: 5
Otro número: 3
8  ← ¡Ahora sí suma!
```

#### `float()` para decimales

Si el número puede tener decimales, usa `float()` en lugar de `int()`.

```python
# Para precios, medidas, temperaturas, etc.
print(float(input("Precio: $")) * 1.16)
```

```
Precio: $100.50
116.58  ← Precio + 16% de impuesto
```

> ⚠️ **Cuidado con `int()` y decimales:** Si el usuario escribe `"3.5"` y usas `int()`, dará error. Usa `float()` si el número podría tener decimales.

---

### 6. Ejemplos Prácticos

#### Calculadora simple

```python
print("=== CALCULADORA ===")
print("Resultado: ", float(input("Primer número: ")) + float(input("Segundo número: ")))
```

```
=== CALCULADORA ===
Primer número: 15.5
Segundo número: 4.5
Resultado:  20.0
```

#### Calculador de edad

```python
print("Tu edad es:", 2025 - int(input("¿En qué año naciste? ")))
```

```
¿En qué año naciste? 1990
Tu edad es: 35
```

#### Área de un rectángulo

```python
print("=== ÁREA DEL RECTÁNGULO ===")
print("El área es:", float(input("Base: ")) * float(input("Altura: ")))
```

```
=== ÁREA DEL RECTÁNGULO ===
Base: 5
Altura: 3
El área es: 15.0
```

#### Saludo completo

```python
print("¡Hola, " + input("Tu nombre: ") + " de " + input("Tu ciudad: ") + "!")
```

```
Tu nombre: Ana
Tu ciudad: Madrid
¡Hola, Ana de Madrid!
```

> 💡 Estos ejemplos usan `input()` directamente dentro de `print()`. Más adelante aprenderás a guardar las respuestas en variables para usarlas varias veces en tu programa.

---

### 7. Resumen Rápido

```python
# Pedir texto
print(input("Tu nombre: "))

# Combinar con otro texto
print("Hola, " + input("Nombre: "))

# Pedir número entero (para cálculos)
print(int(input("Edad: ")) + 10)

# Pedir número decimal (para cálculos)
print(float(input("Precio: ")) * 2)
```

---

### Tabla de Referencia

| Necesidad                     | Código                                     | Resultado               |
|-------------------------------|--------------------------------------------|-------------------------|
| Pedir texto simple            | `input("Mensaje: ")`                       | String del usuario      |
| Mostrar lo que escribe        | `print(input("Mensaje: "))`                | Imprime la respuesta    |
| Unir con otro texto           | `"Hola, " + input("Nombre: ")`             | Concatenación           |
| Convertir a entero            | `int(input("Número: "))`                   | Para cálculos enteros   |
| Convertir a decimal           | `float(input("Número: "))`                 | Para cálculos con punto |
| Verificar tipo de dato        | `type(input("Algo: "))`                    | Siempre `<class 'str'>` |

---

## 04 · Tipos de Datos

En Python, cada dato tiene un **tipo**. El tipo determina qué puedes hacer con ese dato: si puedes sumarlo, multiplicarlo, acceder a partes de él, etc. Reconocer los tipos es fundamental para entender cómo funciona tu código.

> 💡 Puedes verificar el tipo de cualquier dato usando `type()`. Por ejemplo: `print(type("hola"))` muestra `<class 'str'>`.

---

### 1. Tipos Simples

Estos tipos almacenan un solo valor. Son los más básicos y los que usarás con más frecuencia.

#### `str` — String (Texto)

Texto. Cualquier cosa entre comillas es un string: palabras, frases, símbolos, o incluso números escritos como texto.

```python
"hola"    "%$&"    " "    "123"    'Python'
```

> 🔑 **Se reconoce por:** las comillas (simples o dobles)

---

#### `int` — Integer (Entero)

Números enteros. Sin decimales. Pueden ser positivos, negativos o cero.

```python
150    1    555    -15    0
```

> 🔑 **Se reconoce por:** número sin punto decimal ni comillas

---

#### `float` — Float (Decimal)

Números decimales. También llamados "de punto flotante". Siempre tienen un punto.

```python
1.25    25.0    500.50    -95.1    3.14159
```

> 🔑 **Se reconoce por:** tiene punto decimal

---

#### `bool` — Boolean (Booleano)

Verdadero o Falso. Solo tiene dos valores posibles. Se usa para condiciones y decisiones.

```python
True    False
```

> 🔑 **Se reconoce por:** solo puede ser `True` o `False` (con mayúscula inicial)

---

> 💡 **¿`"123"` vs `123`?**
> `"123"` es un string (texto) porque tiene comillas. `123` es un int (número) porque no tiene comillas. Esto importa: `"5" + "3"` da `"53"`, pero `5 + 3` da `8`.

---

### 2. Colecciones

Estos tipos pueden almacenar **múltiples valores**. Son como "contenedores" que guardan otros datos.

#### `list` — Lista

Colección **ordenada y modificable**. Puede contener cualquier tipo de dato, incluso mezclados. Puedes agregar, quitar o cambiar elementos.

```python
["sal", 1, -3, 4.5, "marte", 0]
```

> 🔑 **Se reconoce por:** corchetes `[ ]`

---

#### `tuple` — Tupla

Colección **ordenada e inmutable**. Similar a la lista, pero una vez creada no se puede modificar. Ideal para datos que no deben cambiar.

```python
("lun", "mar", "mie", "jue", "vie")
```

> 🔑 **Se reconoce por:** paréntesis `( )`

---

#### `dict` — Diccionario

Colección de **pares clave:valor**. Como un diccionario real: buscas por la "palabra" (clave) y obtienes su "definición" (valor).

```python
{"color": "rojo", "arte": "cine"}
```

> 🔑 **Se reconoce por:** llaves `{ }` con pares clave:valor separados por dos puntos

---

#### `set` — Conjunto

Colección **sin duplicados y sin orden**. Automáticamente elimina valores repetidos. Útil para encontrar elementos únicos.

```python
{"a", "b", "c", "d", "e"}
```

> 🔑 **Se reconoce por:** llaves `{ }` pero SIN dos puntos (a diferencia del diccionario)

---

> ⚠️ **¿Set o Diccionario?** Ambos usan llaves `{ }`, pero el diccionario tiene dos puntos entre clave y valor: `{"clave": "valor"}`. El set solo tiene valores sueltos: `{"a", "b", "c"}`.

---

### 3. Tabla Comparativa

#### Cómo reconocer cada tipo

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

#### Características de las colecciones

| Tipo    | Ordenado | Modificable | Duplicados      |
|---------|----------|-------------|-----------------|
| `list`  | ✓ Sí     | ✓ Sí        | ✓ Permite       |
| `tuple` | ✓ Sí     | ✗ No        | ✓ Permite       |
| `dict`  | ✓ Sí *   | ✓ Sí        | ✗ Claves únicas |
| `set`   | ✗ No     | ✓ Sí        | ✗ No permite    |

> \* Los diccionarios mantienen el orden de inserción desde Python 3.7

---

### 4. Verificar el Tipo con `type()`

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

---

## 05 · Variables

Una **variable** es como una caja con etiqueta donde guardas un valor para usarlo después. En lugar de repetir el mismo dato una y otra vez, lo guardas en una variable y usas su nombre.

> 💡 Las variables te permiten guardar información, modificarla, y usarla en cualquier parte de tu programa.

---

### 1. ¿Qué es una Variable?

#### Una etiqueta para un valor

Imagina que tienes una caja donde guardas algo. Le pones una etiqueta para saber qué hay adentro. Eso es exactamente una variable: un nombre que apunta a un valor.

```
nombre  →  "María"
```

Aquí, `nombre` es la etiqueta (variable) y `"María"` es el valor que guardamos.

#### Crear una variable

Para crear una variable, escribes el nombre, luego `=`, y después el valor que quieres guardar.

```python
# Crear variables
nombre = "María"
edad = 25
precio = 99.99
activo = True

# Usar las variables
print(nombre)
print(edad)
print(precio)
print(activo)
```

```
María
25
99.99
True
```

> 💡 **El signo `=` en Python:** significa "asignar", no "igual a". Cuando escribes `edad = 25`, le estás diciendo a Python: "guarda el valor 25 en la variable llamada edad".

---

### 2. Reglas para Nombrar Variables

Existen convenciones y buenas prácticas asociadas al nombre de las variables creadas en Python. Tienen la intención de facilitar la **interpretabilidad** y el **mantenimiento** del código.

#### Las 6 reglas clave

| # | Regla            | Descripción                                                                 |
|---|------------------|-----------------------------------------------------------------------------|
| 1 | **Legible**      | El nombre de la variable debe ser relevante según su contenido              |
| 2 | **Unidad**       | No pueden existir espacios; usa guiones bajos para separar palabras         |
| 3 | **Hispanismos**  | Omitir signos específicos del español: tildes (`á`, `é`) y la letra `ñ`    |
| 4 | **Números**      | No deben empezar por número, aunque pueden contenerlos al final             |
| 5 | **Símbolos**     | No incluir: `" ' , < > / ? \ ( ) ! @ # $ % ^ & * ~ - +`                   |
| 6 | **Palabras clave** | No usar palabras reservadas por Python (`print`, `if`, `True`, `class`…) |

#### Nombres válidos

| Regla                            | Ejemplo                              |
|----------------------------------|--------------------------------------|
| ✓ Letras y guiones bajos         | `nombre`, `mi_variable`, `_privado`  |
| ✓ Números (no al inicio)         | `usuario1`, `total2024`, `item_3`    |
| ✓ snake_case (recomendado)       | `nombre_completo`, `precio_total`    |
| ✓ Nombres descriptivos           | `cantidad_productos` mejor que `x`   |

#### Nombres inválidos

| Regla                            | Ejemplo                              |
|----------------------------------|--------------------------------------|
| ✗ Empezar con número             | `1nombre`, `2024_total` — Error      |
| ✗ Espacios                       | `mi variable` — Usa: `mi_variable`   |
| ✗ Caracteres especiales          | `precio$`, `nombre@` — Error         |
| ✗ Hispanismos                    | `año`, `dirección`, `tamaño` — Evitar |
| ✗ Palabras reservadas            | `print`, `True`, `if`, `class`       |

#### Tabla rápida de referencia

| Nombre           | ¿Válido?    | Razón                           |
|------------------|-------------|---------------------------------|
| `edad`           | ✓ Válido    | Simple y descriptivo            |
| `nombre_usuario` | ✓ Válido    | snake_case correcto             |
| `_temporal`      | ✓ Válido    | Puede empezar con `_`           |
| `usuario2`       | ✓ Válido    | Número al final OK              |
| `anio`           | ✓ Válido    | Sin tilde (en lugar de `año`)   |
| `2usuario`       | ✗ Inválido  | No puede empezar con número     |
| `mi nombre`      | ✗ Inválido  | No puede tener espacios         |
| `dirección`      | ✗ Evitar    | Contiene tilde                  |
| `print`          | ✗ Inválido  | Es palabra reservada            |

> ⚠️ **Python distingue mayúsculas:** `nombre`, `Nombre` y `NOMBRE` son tres variables diferentes. Por convención, usa minúsculas con guiones bajos: `mi_variable`.

---

### 3. Reasignar Variables

#### Cambiar el valor

Puedes cambiar el valor de una variable en cualquier momento. El nuevo valor reemplaza al anterior.

```python
puntos = 100
print(puntos)

puntos = 150
print(puntos)

puntos = 200
print(puntos)
```

```
100
150
200
```

#### Actualizar con operaciones

Puedes usar el valor actual de una variable para calcular su nuevo valor.

```python
contador = 0
print(contador)

contador = contador + 1
print(contador)

contador = contador + 1
print(contador)

# Forma abreviada (hace lo mismo)
contador += 1
print(contador)
```

```
0
1
2
3
```

> 💡 **Operadores de asignación abreviados:** `x += 5` es lo mismo que `x = x + 5`. También existen: `-=`, `*=`, `/=`. Son atajos muy útiles.

---

### 4. Tipos de Datos en Variables

#### Una variable puede guardar cualquier tipo

```python
# String (texto)
mensaje = "Hola mundo"

# Integer (número entero)
cantidad = 42

# Float (número decimal)
temperatura = 36.5

# Boolean (verdadero/falso)
encendido = True

# Lista
colores = ["rojo", "verde", "azul"]

# Verificar el tipo
print(type(mensaje))
print(type(cantidad))
print(type(temperatura))
```

```
<class 'str'>
<class 'int'>
<class 'float'>
```

#### Python es de tipado dinámico

Una variable puede cambiar de tipo. No estás obligado a mantener el mismo tipo de dato.

```python
dato = 100
print(dato, type(dato))

dato = "cien"
print(dato, type(dato))

dato = True
print(dato, type(dato))
```

```
100 <class 'int'>
cien <class 'str'>
True <class 'bool'>
```

#### Conversiones de tipos

Python realiza **conversiones implícitas** de tipos de datos automáticamente para operar con valores numéricos. En otros casos, necesitaremos generar una conversión de manera **explícita**.

| Función      | Resultado         | Descripción                  |
|--------------|-------------------|------------------------------|
| `int(var)`   | `<class 'int'>`   | Convierte el dato en integer |
| `float(var)` | `<class 'float'>` | Convierte el dato en float   |

```python
# Conversión explícita a int
precio_texto = "250"
precio = int(precio_texto)
print(precio, type(precio))
# → 250 <class 'int'>

# Conversión explícita a float
temperatura_texto = "36.5"
temperatura = float(temperatura_texto)
print(temperatura, type(temperatura))
# → 36.5 <class 'float'>

# Conversión implícita (Python lo hace solo)
resultado = 10 + 5.0        # int + float → float automáticamente
print(resultado, type(resultado))
# → 15.0 <class 'float'>
```

> ⚠️ No todos los valores se pueden convertir. `int("hola")` lanza un `ValueError`. Solo funciona si el string contiene un número válido.

---

### 5. Usar Variables con `print()`

#### Mostrar el valor

Cuando usas `print()` con una variable, muestra su valor, no su nombre.

```python
ciudad = "Buenos Aires"
pais = "Argentina"

print(ciudad)
print(pais)
```

```
Buenos Aires
Argentina
```

#### Combinar variables con texto

Puedes mostrar variables junto con texto usando comas o concatenación.

```python
nombre = "Carlos"
edad = 30

# Con comas (agrega espacios automáticamente)
print("Hola,", nombre)
print("Tienes", edad, "años")

# Con concatenación (solo strings)
print("Hola, " + nombre + "!")
```

```
Hola, Carlos
Tienes 30 años
Hola, Carlos!
```

> ⚠️ **Concatenación: solo strings.** Si usas `+` para unir, todos los valores deben ser strings. `"Edad: " + 30` da error. Usa comas: `print("Edad:", 30)` o convierte: `"Edad: " + str(30)`.

---

### 6. Operaciones con Variables

#### Matemáticas

```python
precio = 100
cantidad = 5
descuento = 0.10

subtotal = precio * cantidad
print("Subtotal:", subtotal)

ahorro = subtotal * descuento
print("Ahorro:", ahorro)

total = subtotal - ahorro
print("Total:", total)
```

```
Subtotal: 500
Ahorro: 50.0
Total: 450.0
```

#### Variables con `input()`

Puedes guardar lo que el usuario escribe en una variable para usarlo después.

```python
nombre = input("¿Cómo te llamas? ")
print("¡Hola,", nombre + "!")

edad = int(input("¿Cuántos años tienes? "))
proximo = edad + 1
print("El próximo año tendrás", proximo, "años")
```

```
¿Cómo te llamas? Ana
¡Hola, Ana!
¿Cuántos años tienes? 25
El próximo año tendrás 26 años
```

---

### 7. Múltiples Variables

#### Asignación múltiple

Puedes crear varias variables en una sola línea.

```python
# Asignar varios valores a varias variables
x, y, z = 1, 2, 3
print(x, y, z)

# Asignar el mismo valor a varias variables
a = b = c = 0
print(a, b, c)

# Intercambiar valores (truco de Python)
x, y = y, x
print(x, y)
```

```
1 2 3
0 0 0
2 1
```

---

### 8. Resumen

```python
# Crear una variable
nombre = "valor"

# Usar una variable
print(nombre)

# Cambiar su valor
nombre = "nuevo valor"

# Operaciones
total = precio * cantidad

# Actualizar
contador += 1

# Guardar input del usuario
respuesta = input("Pregunta: ")

# Ver el tipo
print(type(nombre))
```

---

### Tabla de Referencia

| Operación                  | Código                          | Descripción                        |
|----------------------------|---------------------------------|------------------------------------|
| Crear variable             | `x = 10`                        | Asigna el valor `10` a `x`         |
| Reasignar                  | `x = 20`                        | Cambia el valor de `x`             |
| Actualizar (suma)          | `x += 5`                        | Equivale a `x = x + 5`             |
| Actualizar (resta)         | `x -= 3`                        | Equivale a `x = x - 3`             |
| Actualizar (multiplicar)   | `x *= 2`                        | Equivale a `x = x * 2`             |
| Verificar tipo             | `type(x)`                       | Devuelve el tipo de la variable     |
| Asignación múltiple        | `a, b = 1, 2`                   | Crea `a` y `b` en una línea        |
| Mismo valor a varias       | `a = b = 0`                     | Ambas valen `0`                    |
| Intercambiar valores       | `a, b = b, a`                   | Swap sin variable temporal         |
| Guardar input              | `x = input("Mensaje: ")`        | Guarda lo que escribe el usuario   |

---

## 06 · Integers y Floats

Python tiene dos tipos de números: **integers** (enteros, sin decimales) y **floats** (con decimales). Entender la diferencia es fundamental para hacer cálculos correctos en tus programas.

> 💡 **La regla de oro:** si tiene punto decimal, es `float`. Si no tiene punto, es `int`.

---

### 1. Los Dos Tipos de Números

#### `int` — Integer (Entero)

Números enteros. Sin punto decimal. Positivos, negativos o cero.

```python
42    -15    0    1000    -999
```

> 🔑 Sin punto decimal

#### `float` — Float (Decimal)

Números decimales. También llamados "de punto flotante". Siempre tienen punto.

```python
3.14    -0.5    100.0    2.718
```

> 🔑 Con punto decimal

#### Verificar el tipo

Usa `type()` para saber si un número es `int` o `float`.

```python
print(type(42))
# → <class 'int'>

print(type(3.14))
# → <class 'float'>

print(type(100.0))
# → <class 'float'>  (tiene punto, aunque sea .0)
```

> 💡 **`100` vs `100.0`:** `100` es un `int`, pero `100.0` es un `float`. El punto hace toda la diferencia, aunque matemáticamente sean iguales.

---

### 2. Operaciones Básicas

#### Las cuatro operaciones

| Operador | Operación       | Ejemplo   | Resultado  |
|----------|-----------------|-----------|------------|
| `+`      | Suma            | `10 + 3`  | `13`       |
| `-`      | Resta           | `10 - 3`  | `7`        |
| `*`      | Multiplicación  | `10 * 3`  | `30`       |
| `/`      | División        | `10 / 3`  | `3.333...` |

```python
print(10 + 5)    # 15
print(20 - 8)    # 12
print(7 * 6)     # 42
print(15 / 4)    # 3.75

# Con variables
precio = 100
cantidad = 3
total = precio * cantidad
print(total)     # 300
```

> ⚠️ **La división `/` siempre da `float`:** En Python 3, incluso si el resultado es "exacto". `10 / 2` da `5.0`, no `5`.

---

### 3. Operaciones Especiales

#### División entera, módulo y potencia

| Operador | Operación       | Ejemplo    | Resultado |
|----------|-----------------|------------|-----------|
| `//`     | División entera | `17 // 5`  | `3`       |
| `%`      | Módulo (resto)  | `17 % 5`   | `2`       |
| `**`     | Potencia        | `2 ** 3`   | `8`       |

#### División entera `//`

Devuelve solo la parte entera del resultado, descartando los decimales.

```python
print(17 / 5)     # 3.4   (división normal)
print(17 // 5)    # 3     (división entera)

print(10 // 3)    # 3
print(25 // 4)    # 6
print(100 // 7)   # 14
```

#### Módulo `%` (el resto)

Devuelve lo que sobra después de dividir. Muy útil para saber si un número es par o impar.

```python
print(17 % 5)     # 2  (17 = 5×3 + 2)
print(10 % 3)     # 1  (10 = 3×3 + 1)
print(20 % 4)     # 0  (división exacta)

# ¿Es par o impar?
print(8 % 2)      # 0 → es par
print(7 % 2)      # 1 → es impar
```

#### Potencia `**`

Eleva un número a una potencia. También funciona para raíces usando decimales.

```python
print(2 ** 3)      # 8      (2³ = 2×2×2)
print(5 ** 2)      # 25     (5² = 5×5)
print(10 ** 4)     # 10000  (10⁴)

# Raíz cuadrada (potencia 0.5)
print(16 ** 0.5)   # 4.0    (√16 = 4)
print(27 ** (1/3)) # 3.0    (∛27 = 3)
```

---

### 4. Mezclar `int` y `float`

Cuando operas un `int` con un `float`, el resultado siempre es `float`. Python "promueve" el `int` automáticamente.

```python
print(5 + 2.0)     # 7.0   (int + float = float)
print(10 * 0.5)    # 5.0   (int * float = float)
print(8 - 3.5)     # 4.5   (int - float = float)

# Verificar el tipo
resultado = 10 + 5.0
print(resultado)           # 15.0
print(type(resultado))     # <class 'float'>
```

> 💡 **La regla de la "promoción":**
> - `int` + `int` = `int` (excepto división `/`)
> - `float` + `float` = `float`
> - `int` + `float` = `float`
>
> Python siempre elige el tipo más "amplio".

---

### 5. Convertir entre Tipos

#### De `float` a `int`

Usa `int()` para convertir un float a entero. **Trunca** los decimales (no redondea).

```python
print(int(3.7))    # 3  (no redondea, trunca)
print(int(3.2))    # 3
print(int(9.99))   # 9  (¡no es 10!)
print(int(-2.8))   # -2 (hacia el cero)
```

#### De `int` a `float`

Usa `float()` para convertir un entero a decimal. Agrega `.0` al final.

```python
print(float(5))     # 5.0
print(float(100))   # 100.0
print(float(-7))    # -7.0
```

#### Convertir desde texto

Puedes convertir strings que contengan números válidos.

```python
# String a int
print(int("42"))      # 42
print(int("-15"))     # -15

# String a float
print(float("3.14"))  # 3.14
print(float("100"))   # 100.0

# Útil con input()
edad = int(input("Tu edad: "))
precio = float(input("Precio: "))
```

> ⚠️ **Cuidado con las conversiones:** `int("3.14")` da error porque tiene punto. Primero convierte a float: `int(float("3.14"))` da `3`.

---

### 6. Redondear Números

El redondeo facilita la interpretación de los valores calculados al limitar la cantidad de decimales que se muestran en pantalla. También permite aproximar valores decimales al entero más próximo.

#### Sintaxis de `round()`

```
round(number, ndigits)
         │         └── cantidad de decimales (si se omite, el resultado es entero)
         └── valor a redondear
```

| Parámetro  | Descripción                                              |
|------------|----------------------------------------------------------|
| `number`   | El valor a redondear                                     |
| `ndigits`  | Cantidad de decimales. Si se omite, devuelve un entero   |

#### Ejemplos de uso

```python
# Sin ndigits → resultado entero
print(round(100/3))       # → 33
print(round(3.7))         # → 4
print(round(3.2))         # → 3

# Con ndigits → resultado con N decimales
print(round(12/7, 2))     # → 1.71
print(round(3.14159, 2))  # → 3.14
print(round(3.14159, 3))  # → 3.142
print(round(3.14159, 4))  # → 3.1416

# Ejemplo práctico: precios
precio = 19.99
impuesto = precio * 0.16
print(round(impuesto, 2)) # → 3.2
```

> 💡 **`round()` vs `int()`:** `round(3.7)` da `4` (redondea al más cercano). `int(3.7)` da `3` (trunca, simplemente corta los decimales).

---

### 7. Números Grandes y Pequeños

#### Notación científica

Python puede manejar números muy grandes o muy pequeños usando notación científica con `e`.

```python
# Números grandes
print(1e6)       # 1000000.0  (1 × 10⁶)
print(2.5e8)     # 250000000.0

# Números pequeños
print(1e-3)      # 0.001  (1 × 10⁻³)
print(5e-6)      # 0.000005

# Enteros grandes (Python los maneja bien)
grande = 10 ** 100
print(type(grande))  # <class 'int'>
```

#### Separador visual (guión bajo)

Para números largos, puedes usar `_` como separador visual. Python lo ignora completamente.

```python
poblacion = 8_000_000_000
precio = 1_500_000.50

print(poblacion)  # 8000000000
print(precio)     # 1500000.5
```

---

### 8. Errores Comunes

#### División por cero

Dividir por cero causa un error. Python no puede calcular algo dividido entre nada.

```python
print(10 / 0)
# ZeroDivisionError: division by zero

print(10 // 0)
# ZeroDivisionError: integer division by zero

print(10 % 0)
# ZeroDivisionError: integer modulo by zero
```

#### Precisión de floats

Los floats a veces dan resultados "raros" por cómo las computadoras representan decimales en binario.

```python
print(0.1 + 0.2)
# 0.30000000000000004  (¡no es exactamente 0.3!)

# Solución: redondear
print(round(0.1 + 0.2, 1))
# 0.3
```

> ⚠️ **¿Por qué pasa esto?** Las computadoras usan sistema binario y algunos decimales no se pueden representar exactamente. Es normal y ocurre en todos los lenguajes. Para cálculos de dinero, usa siempre `round()`.

---

### 9. Resumen — Cheatsheet de Números

```python
# Tipos
42        # int (entero)
3.14      # float (decimal)

# Operaciones básicas
10 + 5    # Suma: 15
10 - 5    # Resta: 5
10 * 5    # Multiplicación: 50
10 / 5    # División: 2.0 (siempre float)

# Operaciones especiales
17 // 5   # División entera: 3
17 % 5    # Módulo (resto): 2
2 ** 3    # Potencia: 8

# Conversiones
int(3.7)           # 3     (trunca)
float(5)           # 5.0
round(3.7)         # 4     (redondea)
round(3.14159, 2)  # 3.14
```

---

### Tabla de Referencia

| Operación          | Código             | Resultado  | Tipo devuelto |
|--------------------|--------------------|------------|---------------|
| Suma               | `10 + 5`           | `15`       | `int`         |
| Resta              | `10 - 5`           | `5`        | `int`         |
| Multiplicación     | `10 * 5`           | `50`       | `int`         |
| División           | `10 / 5`           | `2.0`      | `float`       |
| División entera    | `17 // 5`          | `3`        | `int`         |
| Módulo (resto)     | `17 % 5`           | `2`        | `int`         |
| Potencia           | `2 ** 3`           | `8`        | `int`         |
| Raíz cuadrada      | `16 ** 0.5`        | `4.0`      | `float`       |
| Truncar a entero   | `int(3.9)`         | `3`        | `int`         |
| Convertir a float  | `float(5)`         | `5.0`      | `float`       |
| Redondear          | `round(3.7)`       | `4`        | `int`         |
| Redondear decimales| `round(3.14, 1)`   | `3.1`      | `float`       |

---

## 07 · Métodos de String

Los strings en Python tienen una gran cantidad de **métodos incorporados** que permiten analizarlos, transformarlos, dividirlos y unirlos sin necesidad de librerías externas.

> 💡 Los strings son **inmutables**: los métodos de transformación no modifican el string original, sino que retornan uno nuevo.

---

### Índice

1. [Métodos de Análisis](#1-métodos-de-análisis)
2. [Métodos de Transformación](#2-métodos-de-transformación)
3. [Métodos de Separación y Unión](#3-métodos-de-separación-y-unión)

---

### 1. Métodos de Análisis

Permiten examinar el contenido de un string sin modificarlo.

#### `count()` — contar ocurrencias

Retorna cuántas veces aparece un conjunto de caracteres dentro del string.

```python
s = "Hola mundo"
print(s.count("Hola"))
# → 1

print("abracadabra".count("a"))
# → 5
```

---

#### `find()` e `index()` — buscar posición

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

#### `rfind()` y `rindex()` — buscar desde el final

Igual que `find()` e `index()`, pero la búsqueda se realiza de **derecha a izquierda**, retornando la última ocurrencia.

```python
s = "C:/python36/python.exe"

print(s.find("/"))    # → 2   (primera ocurrencia)
print(s.rfind("/"))   # → 11  (última ocurrencia)
```

---

#### `startswith()` y `endswith()` — verificar inicio y fin

Retornan `True` o `False` según si la cadena comienza o termina con el argumento dado.

```python
s = "Hola mundo"

print(s.startswith("Hola"))    # → True
print(s.endswith("mundo"))     # → True
print(s.endswith("world"))     # → False
```

> 💡 Muy útiles para validar extensiones de archivos, prefijos de rutas, etc.

---

#### `isdigit()`, `isnumeric()` e `isdecimal()` — verificar si es número

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

#### Otros métodos de verificación

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

#### `isidentifier()` — verificar si es un identificador válido

Retorna `True` si la cadena puede ser un nombre de variable válido en Python (letras, dígitos y guiones bajos, sin comenzar con dígito).

```python
print("mi_variable".isidentifier())   # → True
print("2nombre".isidentifier())       # → False
print("class".isidentifier())         # → True  (palabras reservadas también pasan)
```

#### `istitle()` — verificar formato título

Retorna `True` si cada palabra comienza con mayúscula y el resto son minúsculas.

```python
print("Hola Mundo".istitle())   # → True
print("Hola mundo".istitle())   # → False
print("HOLA MUNDO".istitle())   # → False
```

---

### 2. Métodos de Transformación

Retornan un **nuevo string** con la transformación aplicada. El original no se modifica.

#### `capitalize()` — primera letra en mayúscula

```python
print("hola mundo".capitalize())
# → Hola mundo
```

---

#### `lower()` y `upper()` — minúsculas y mayúsculas

```python
print("Hola Mundo!".lower())   # → hola mundo!
print("Hola Mundo!".upper())   # → HOLA MUNDO!
```

---

#### `swapcase()` — invertir mayúsculas y minúsculas

```python
print("Hola Mundo!".swapcase())
# → hOLA mUNDO!
```

---

#### `title()` — formato título

Primera letra de cada palabra en mayúscula, el resto en minúsculas.

```python
print("hola mundo desde python".title())  # → Hola Mundo Desde Python
print("hola_mundo".title())               # → Hola_Mundo
```

---

#### `casefold()` — minúsculas para comparaciones multiidioma

Versión más agresiva que `lower()`, diseñada para comparaciones sin distinción de mayúsculas en múltiples idiomas.

```python
print("Straße".casefold())   # → strasse
print("Straße".lower())      # → straße

# Útil para comparar cadenas independientemente del idioma:
print("Straße".casefold() == "strasse".casefold())   # → True
```

---

#### `strip()`, `lstrip()` y `rstrip()` — eliminar espacios

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

#### `removeprefix()` y `removesuffix()` *(Python 3.9+)*

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

#### `replace()` — reemplazar texto

Reemplaza todas las ocurrencias de una subcadena por otra.

```python
s = "Hola mundo"
print(s.replace("mundo", "world"))
# → Hola world
```

---

#### `center()`, `ljust()` y `rjust()` — alineación

Alinean el string dentro de un ancho dado. El segundo argumento opcional define el carácter de relleno (por defecto un espacio).

```python
print("Hola".center(10))        # →    Hola   
print("Hola".ljust(10))         # → Hola      
print("Hola".rjust(10))         # →       Hola
print("Hola".center(10, "*"))   # → ***Hola***
```

---

#### `zfill()` — rellenar con ceros

Rellena con ceros a la izquierda hasta el ancho indicado. Respeta los signos `+` y `-`.

```python
print("42".zfill(6))     # → 000042
print("-42".zfill(6))    # → -00042
print("Hola".zfill(8))   # → 0000Hola
```

---

#### `expandtabs()` — reemplazar tabulaciones

Reemplaza los caracteres `\t` por espacios. El argumento indica el tamaño de cada tabulación (por defecto `8`).

```python
print("col1\tcol2\tcol3".expandtabs())     # → col1    col2    col3
print("col1\tcol2".expandtabs(4))          # → col1col2
print("a\tb\tc".expandtabs(4))             # → a   b   c
```

---

#### `encode()` — codificar la cadena

Codifica el string con el mapa de caracteres especificado y retorna un objeto `bytes`.

```python
print("Hola mundo".encode("utf-8"))
# → b'Hola mundo'
```

---

#### `format()` y `format_map()` — interpolación

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

#### `maketrans()` y `translate()` — reemplazos carácter a carácter

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

### 3. Métodos de Separación y Unión

#### `split()` — dividir en lista

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

#### `rsplit()` — dividir desde el final

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

#### `splitlines()` — dividir por saltos de línea

Divide el string en cada salto de línea y retorna una lista.

```python
print("Hola mundo!\nHello world!".splitlines())
# → ['Hola mundo!', 'Hello world!']
```

---

#### `partition()` y `rpartition()` — dividir en tres partes

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

#### `join()` — unir una lista en un string

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

### Resumen General

#### Métodos de análisis

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

#### Métodos de transformación

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

#### Métodos de separación y unión

| Método | Descripción |
|--------|-------------|
| `split(sep, n)` | Divide por `sep` (máx. `n` veces) desde la izquierda |
| `rsplit(sep, n)` | Divide por `sep` (máx. `n` veces) desde la derecha |
| `splitlines()` | Divide por saltos de línea |
| `partition(sep)` | Divide en 3: antes, `sep`, después (desde izquierda) |
| `rpartition(sep)` | Divide en 3: antes, `sep`, después (desde derecha) |
| `join(lista)` | Une elementos de `lista` con el string como separador |

---

## 08 · Listas

Una **lista** es una secuencia ordenada de objetos. Esos objetos pueden ser de cualquier tipo: strings, integers, floats, booleanos, e incluso otras listas. Son uno de los tipos de datos más usados en Python.

> 💡 En Python, una lista se reconoce por los corchetes `[ ]`. Por ejemplo: `["C", "C++", "Python", "Java"]`.

---

### Propiedades de las Listas

| Propiedad | Descripción |
|-----------|-------------|
| **Mutables** | Sus elementos pueden modificarse después de creada la lista. |
| **Ordenadas** | Los elementos mantienen el orden en que fueron agregados. |
| **Admiten duplicados** | Pueden contener el mismo valor más de una vez. |
| **Indexadas** | Se puede acceder a cada elemento por su posición (`[índice]`). |
| **Tienen longitud** | Se puede medir con `len()`. |
| **Concatenables** | Se pueden unir con el operador `+`. |

> Ver también: [Guía de Tipos de Datos](#04-tipos-de-datos) para comparar listas con tuplas, diccionarios y sets.

---

### Índice

1. [Crear Listas](#1-crear-listas)
2. [Acceder a Elementos — Indexado](#2-acceder-a-elementos--indexado)
3. [Extraer Partes — Slicing](#3-extraer-partes--slicing)
4. [Longitud con `len()`](#4-longitud-con-len)
5. [Concatenar Listas](#5-concatenar-listas)
6. [Agregar Elementos — `append()`](#6-agregar-elementos--append)
7. [Eliminar Elementos — `pop()`](#7-eliminar-elementos--pop)
8. [Ordenar — `sort()`](#8-ordenar--sort)
9. [Invertir — `reverse()`](#9-invertir--reverse)
10. [Resumen — Cheatsheet](#10-resumen--cheatsheet)

---

### 1. Crear Listas

Una lista se crea con corchetes `[ ]`, separando cada elemento con una coma.

```python
lista_1 = ["C", "C++", "Python", "Java"]
lista_2 = ["PHP", "SQL", "Visual Basic"]

# Una lista puede mezclar tipos de datos
mixta = ["hola", 42, 3.14, True]

# Lista vacía
vacia = []
```

Para verificar el tipo de dato:

```python
mi_lista = ["a", "b", "c"]
print(type(mi_lista))
# → <class 'list'>
```

---

### 2. Acceder a Elementos — Indexado

Cada elemento tiene un índice que empieza en `0`. También se puede usar índices negativos para contar desde el final.

```python
lista_1 = ["C", "C++", "Python", "Java"]

print(lista_1[0])    # → C
print(lista_1[2])    # → Python
print(lista_1[-1])   # → Java  (último elemento)
```

---

### 3. Extraer Partes — Slicing

La sintaxis es `lista[inicio:fin:paso]`. El índice `fin` no está incluido.

```python
lista_1 = ["C", "C++", "Python", "Java"]

print(lista_1[1:3])
# → ['C++', 'Python']

print(lista_1[0:2])
# → ['C', 'C++']

print(lista_1[::2])
# → ['C', 'Python']  (cada dos elementos)
```

> 💡 El slicing funciona igual que en los strings: `[inicio:fin:paso]`.

---

### 4. Longitud con `len()`

Retorna la cantidad de elementos de la lista.

```python
lista_1 = ["C", "C++", "Python", "Java"]

print(len(lista_1))
# → 4
```

---

### 5. Concatenar Listas

El operador `+` une dos listas en una nueva.

```python
lista_1 = ["C", "C++", "Python", "Java"]
lista_2 = ["PHP", "SQL", "Visual Basic"]

print(lista_1 + lista_2)
# → ['C', 'C++', 'Python', 'Java', 'PHP', 'SQL', 'Visual Basic']
```

> ⚠️ La concatenación no modifica las listas originales; genera una nueva.

---

### 6. Agregar Elementos — `append()`

Agrega un elemento **al final** de la lista, modificándola en el lugar.

```python
lista_1 = ["C", "C++", "Python", "Java"]

lista_1.append("R")
print(lista_1)
# → ['C', 'C++', 'Python', 'Java', 'R']
```

---

### 7. Eliminar Elementos — `pop()`

Elimina el elemento en el índice indicado y **retorna el valor eliminado**.

```python
lista_1 = ["C", "C++", "Python", "Java", "R"]

print(lista_1.pop(4))
# → R

print(lista_1)
# → ['C', 'C++', 'Python', 'Java']
```

> 💡 Si no pasas un índice, `pop()` elimina y retorna el último elemento.

---

### 8. Ordenar — `sort()`

Ordena los elementos de la lista **en el lugar** (modifica la lista original).

```python
lista_3 = ["d", "a", "c", "b", "e"]

lista_3.sort()
print(lista_3)
# → ['a', 'b', 'c', 'd', 'e']
```

Para ordenar de mayor a menor:

```python
lista_3.sort(reverse=True)
print(lista_3)
# → ['e', 'd', 'c', 'b', 'a']
```

---

### 9. Invertir — `reverse()`

Invierte el orden de los elementos **en el lugar**. No los ordena; simplemente los voltea.

```python
lista_4 = [5, 4, 7, 1, 9]

lista_4.reverse()
print(lista_4)
# → [9, 1, 7, 4, 5]
```

> ⚠️ `sort()` y `reverse()` no son opuestos. `sort()` ordena según un criterio (alfabético, numérico). `reverse()` solo invierte el orden actual, sin importar cuál sea.

---

### 10. Resumen — Cheatsheet

| Operación | Código | Resultado |
|-----------|--------|-----------|
| Crear lista | `lista = ["a", "b", "c"]` | Lista con 3 elementos |
| Acceder por índice | `lista[0]` | `"a"` |
| Slicing | `lista[1:3]` | `["b", "c"]` |
| Longitud | `len(lista)` | `3` |
| Concatenar | `lista + ["d"]` | `["a", "b", "c", "d"]` |
| Agregar al final | `lista.append("d")` | Modifica la lista original |
| Eliminar por índice | `lista.pop(1)` | Retorna y elimina `"b"` |
| Ordenar | `lista.sort()` | Ordena en el lugar |
| Invertir | `lista.reverse()` | Invierte en el lugar |
| Verificar tipo | `type(lista)` | `<class 'list'>` |

---

## 09 · Diccionarios

Un **diccionario** es una estructura de datos que almacena información en pares **clave:valor**. Son especialmente útiles para guardar y recuperar información a partir del nombre de sus claves, sin necesidad de índices numéricos.

> 💡 En Python, un diccionario se reconoce por las llaves `{ }` con pares `clave: valor` separados por dos puntos. Por ejemplo: `{"curso": "Python TOTAL", "clase": "Diccionarios"}`.

---

### Propiedades de los Diccionarios

| Propiedad | Descripción |
|-----------|-------------|
| **Mutables** | Se pueden agregar, modificar y eliminar pares clave:valor después de creado. |
| **Ordenados** * | Mantienen el orden de inserción desde Python 3.7+. |
| **Claves únicas** | No se permiten claves duplicadas. Si repetís una clave, el valor anterior se sobreescribe. |
| **Valores duplicados** | Los valores sí pueden repetirse entre distintas claves. |
| **Acceso por clave** | Los elementos se acceden por su nombre de clave, no por índice numérico. |

> \* A partir de Python 3.7+, los diccionarios mantienen el orden de inserción para aumentar la eficiencia en el uso de la memoria.

> Ver también: [Guía de Tipos de Datos](#04-tipos-de-datos) para comparar diccionarios con listas, tuplas y sets.

---

### Índice

1. [Crear Diccionarios](#1-crear-diccionarios)
2. [Acceder a Valores](#2-acceder-a-valores)
3. [Estructuras Anidadas](#3-estructuras-anidadas)
4. [Agregar, Modificar y Mutar Valores](#4-agregar-modificar-y-mutar-valores)
5. [Listar Claves, Valores y Pares — `keys()`, `values()`, `items()`](#5-listar-claves-valores-y-pares--keys-values-items)
6. [Unpacking — `*` y `**`](#6-unpacking----y-)
7. [Resumen — Cheatsheet](#7-resumen--cheatsheet)

---

### 1. Crear Diccionarios

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

### 2. Acceder a Valores

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

### 3. Estructuras Anidadas

Los valores de un diccionario pueden ser de **cualquier tipo**: números, strings, listas, o incluso otros diccionarios.

```python
dic = {
    "c1": 55,
    "c2": [10, 20, 30],
    "c3": {"a1": 100, "a2": 200, "a3": 300}
}
```

#### Acceder a un elemento dentro de una lista anidada

Encadenás los corchetes: primero la clave del diccionario, luego el índice de la lista.

```python
print(dic["c2"][1])
# → 20
```

#### Acceder a un elemento dentro de un diccionario anidado

```python
print(dic["c3"]["a2"])
# → 200
```

#### Encadenar métodos de string sobre valores

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

### 4. Agregar, Modificar y Mutar Valores

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

#### Mutar un valor de tipo lista — `append()`

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

### 5. Listar Claves, Valores y Pares — `keys()`, `values()`, `items()`

Tres métodos para inspeccionar el contenido de un diccionario:

#### `keys()` — lista las claves

```python
mi_diccionario = {"curso": "Python TOTAL", "clase": "Diccionarios"}

print(mi_diccionario.keys())
# → dict_keys(['curso', 'clase'])
```

#### `values()` — lista los valores

```python
print(mi_diccionario.values())
# → dict_values(['Python TOTAL', 'Diccionarios'])
```

#### `items()` — lista los pares clave:valor

```python
print(mi_diccionario.items())
# → dict_items([('curso', 'Python TOTAL'), ('clase', 'Diccionarios')])
```

> 💡 Estos métodos retornan vistas especiales (`dict_keys`, `dict_values`, `dict_items`). Para obtener una lista común, envolvelos con `list()`: `list(mi_diccionario.keys())`.

---

### 6. Unpacking — `*` y `**`

Python tiene el equivalente del operador spread `...` de JavaScript: `*` para listas y `**` para diccionarios.

#### Listas — `*`

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

#### Diccionarios — `**`

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

#### Comparación JS → Python

| JS | Python |
|----|--------|
| `[...a, ...b]` | `[*a, *b]` |
| `{ ...a, ...b }` | `{**a, **b}` |
| `{ ...obj, key: val }` | `{**obj, "key": val}` |

#### Pasar diccionario como argumentos a una función

`**` también desempaqueta un diccionario como argumentos nombrados al llamar una función:

```python
def saludar(nombre, edad):
    print(f"Hola {nombre}, tenés {edad} años")

datos = {"nombre": "Juan", "edad": 20}
saludar(**datos)  # → Hola Juan, tenés 20 años
```

---

### 7. Resumen — Cheatsheet

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

---

## 10 · Tuples

Un **tuple** (o tupla) es una estructura de datos que almacena múltiples elementos en una única variable. Se distingue de las listas por ser **inmutable**: una vez creado, sus elementos no pueden modificarse.

> 💡 Un tuple se reconoce por los paréntesis `( )` con elementos separados por comas. Por ejemplo: `(1, "dos", 3.0)`.

---

### Propiedades de los Tuples

| Propiedad | Descripción |
|-----------|-------------|
| **Inmutables** | No se pueden agregar, modificar ni eliminar elementos después de creado. |
| **Ordenados** | Mantienen el orden de inserción; el índice es estable. |
| **Admiten duplicados** | El mismo valor puede aparecer más de una vez. |
| **Heterogéneos** | Pueden contener elementos de distintos tipos: `int`, `str`, `list`, otro `tuple`, etc. |
| **Eficientes** | Al ser inmutables, ocupan menos memoria y son más rápidos que las listas. |

> Ver también: [Guía de Tipos de Datos](#04-tipos-de-datos) para comparar tuples con listas, diccionarios y sets.

---

### Índice

1. [Crear Tuples](#1-crear-tuples)
2. [Indexado y Longitud](#2-indexado-y-longitud)
3. [Inmutabilidad](#3-inmutabilidad)
4. [Casting — Convertir a Lista](#4-casting--convertir-a-lista)
5. [Unpacking — Extraer Elementos](#5-unpacking--extraer-elementos)
6. [Métodos — `count()` e `index()`](#6-métodos--count-e-index)
7. [Resumen — Cheatsheet](#7-resumen--cheatsheet)

---

### 1. Crear Tuples

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

### 2. Indexado y Longitud

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

### 3. Inmutabilidad

Los tuples **no soportan asignación de ítems**. Intentarlo lanza `TypeError`:

```python
mi_tuple = (1, 2, 3, 4, (10, 20))

# Esto genera error:
# mi_tuple[4] = 44
# → TypeError: 'tuple' object does not support item assignment
```

Si necesitás modificar elementos, primero convertí el tuple a lista (ver sección 4).

---

### 4. Casting — Convertir a Lista

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

### 5. Unpacking — Extraer Elementos

El unpacking asigna cada elemento del tuple a una variable en una sola línea. La cantidad de variables debe coincidir con la cantidad de elementos.

```python
mi_otro_tuple = (1, 2, 3)
x, y, z = mi_otro_tuple
print(x, y, z)  # → 1 2 3
```

#### Unpacking parcial con `*`

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

### 6. Métodos — `count()` e `index()`

Los tuples tienen solo dos métodos propios (al ser inmutables no pueden tener métodos que modifiquen la estructura).

#### `count(valor)` — cuenta ocurrencias

```python
t = (1, 2, 3, 4, 2)
print(t.count(2))
# → 2
print(f"Hay {t.count(2)} elementos con el valor 2 en tu tuple")
```

#### `index(valor)` — índice de la primera ocurrencia

```python
t = (1, 2, 3, 4, 2)
print(t.index(2))
# → 1  (primera posición donde aparece el 2)
```

> ⚠️ Si el valor no existe, `index()` lanza `ValueError`. Verificá con `valor in t` antes si no estás seguro.

---

### 7. Resumen — Cheatsheet

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

---

## 11 · Sets

Un **set** es una colección mutable de elementos **inmutables**, **no ordenados** y **sin datos repetidos**. Son útiles para eliminar duplicados y para operaciones matemáticas de conjuntos (unión, intersección, diferencia).

> 💡 Los sets se reconocen por las llaves `{ }` con elementos separados por comas — igual que un diccionario, pero **sin pares clave:valor**. Por ejemplo: `{1, 2, "tres"}`.

---

### Propiedades de los Sets

| Propiedad | Valor | Descripción |
|-----------|:-----:|-------------|
| **Mutable** | ✅ | Se pueden agregar y eliminar elementos. |
| **Ordenado** | ❌ | No mantiene el orden de inserción; no se accede por índice. |
| **Admite duplicados** | ❌ | Si agregás un elemento que ya existe, el set lo ignora. |
| **Elementos hasheables** | ✅ | Solo acepta `int`, `float`, `str`, `bool`, `tuple`. No puede contener listas ni diccionarios (son mutables). |

> Ver también: [Guía de Tipos de Datos](#04-tipos-de-datos) para comparar sets con listas, tuples y diccionarios.

---

### Índice

1. [Crear Sets](#1-crear-sets)
2. [Restricciones — Qué puede y no puede contener](#2-restricciones--qué-puede-y-no-puede-contener)
3. [Operador `in` — Verificar membresía](#3-operador-in--verificar-membresía)
4. [Métodos de Elemento — `add()`, `remove()`, `discard()`, `pop()`](#4-métodos-de-elemento--add-remove-discard-pop)
5. [Vaciar — `clear()`](#5-vaciar--clear)
6. [Operaciones de Conjuntos — `union()`, `intersection()`, `difference()`](#6-operaciones-de-conjuntos--union-intersection-difference)
7. [Resumen — Cheatsheet](#7-resumen--cheatsheet)

---

### 1. Crear Sets

#### Con llaves `{ }` — sintaxis literal

```python
otro_set = {1, 2, 3, 4, 5}
print(otro_set, type(otro_set))
# → {1, 2, 3, 4, 5} <class 'set'>
```

#### Con `set([lista])` — constructor

```python
mi_set = set([1, 2, 3, 4, 5])
print(mi_set, type(mi_set))
# → {1, 2, 3, 4, 5} <class 'set'>
```

> ⚠️ `set(1, 2, 3)` **no funciona** — Python interpreta que recibe múltiples argumentos. El constructor `set()` recibe **un único iterable**: `set([1, 2, 3])`.

#### Set vacío — siempre con `set()`

```python
vacio = set()
print(type(vacio))  # → <class 'set'>

# {} crea un diccionario vacío, no un set
print(type({}))     # → <class 'dict'>
```

#### Duplicados — se eliminan automáticamente

```python
set_con_repetidos = {1, 1, 2, 3, 4, 5, 5, 5}
print(set_con_repetidos)
# → {1, 2, 3, 4, 5}  — sin error, solo valores únicos
```

---

### 2. Restricciones — Qué puede y no puede contener

Los elementos de un set deben ser **hasheables** (inmutables). Un set puede contener:

```python
another_set = set([1, 2, "Tres", False, (5, 10)])
print(another_set)
# → {False, 1, 2, 'Tres', (5, 10)}
```

Lo que **no** puede contener:

```python
# Listas y diccionarios son mutables → TypeError: unhashable type
# set_con_mutables = {1, 2, "Tres", False, [1], {"nombre": "Janio"}}
```

| Tipo | ¿Permitido en set? |
|------|--------------------|
| `int`, `float`, `str`, `bool` | ✅ |
| `tuple` | ✅ (si sus elementos también son hasheables) |
| `list` | ❌ — mutable |
| `dict` | ❌ — mutable |
| `set` | ❌ — mutable |

---

### 3. Operador `in` — Verificar membresía

Al igual que en listas y diccionarios, podés preguntar si un elemento está en el set:

```python
another_set = {1, 2, "Tres", False, (5, 10)}

print("Tres" in another_set)   # → True
print(99 in another_set)       # → False
print(99 not in another_set)   # → True
```

> 💡 La verificación con `in` en sets es **O(1)** (tiempo constante), más eficiente que en listas donde es O(n).

---

### 4. Métodos de Elemento — `add()`, `remove()`, `discard()`, `pop()`

#### `add(item)` — agrega un elemento; si ya existe, lo omite sin error

```python
s3 = {1, 2, 3, 4, 5}
s3.add(6)
print(s3)  # → {1, 2, 3, 4, 5, 6}

s3.add(4)  # ya existe, no hace nada
print(s3)  # → {1, 2, 3, 4, 5, 6}
```

#### `remove(item)` — elimina un elemento; lanza `KeyError` si no existe

```python
s1 = {1, 2, 3}
s1.remove(1)
print(s1)  # → {2, 3}

# s1.remove(6)  → KeyError: 6
```

#### `discard(item)` — elimina un elemento; **no lanza error** si no existe

```python
s1 = {2, 3}
s1.discard(1)  # no existe, pero no hay error
print(s1)      # → {2, 3}  (sin cambios)
```

> 💡 Preferí `discard()` cuando no estás seguro de si el elemento existe.

#### `pop()` — elimina y retorna un elemento **al azar**

Como los sets no tienen orden, `pop()` elige un elemento aleatorio. Puede usarse para sorteos o selección aleatoria:

```python
s2 = {3, 4, 5}
sorteo = s2.pop()
print(sorteo)  # → algún elemento (no predecible)
print(s2)      # → el set sin ese elemento
```

---

### 5. Vaciar — `clear()`

```python
s2 = {3, 4, 5}
s2.clear()
print(s2)  # → set()
```

---

### 6. Operaciones de Conjuntos — `union()`, `intersection()`, `difference()`

Sets de referencia:

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
```

#### `union(set)` — une dos sets eliminando duplicados (retorna set nuevo)

```python
s3 = s1.union(s2)
print(f"union une los 2 sets sin repetidos: {s3}")
# → {1, 2, 3, 4, 5}
```

#### `intersection(set)` — elementos comunes a ambos sets

```python
print(s1.intersection(s2))  # → {3}
```

#### `difference(set)` — elementos solo en A (no en B)

```python
print(s1.difference(s2))  # → {1, 2}
print(s2.difference(s1))  # → {4, 5}
```

> Para las variantes que modifican el set original (`update()`, `intersection_update()`, `difference_update()`, `symmetric_difference()`) ver el [PDF de métodos de sets](../Sets+-+Métodos.pdf).

---

### 7. Resumen — Cheatsheet

| Operación | Código | Modifica in-place |
|-----------|--------|:-----------------:|
| Crear desde lista | `set([1, 2, 3])` | — |
| Crear literal | `{1, 2, 3}` | — |
| Set vacío | `set()` | — |
| Verificar membresía | `x in s` | No |
| Agregar elemento | `s.add(x)` | Sí |
| Eliminar (con error) | `s.remove(x)` | Sí |
| Eliminar (sin error) | `s.discard(x)` | Sí |
| Eliminar al azar | `s.pop()` | Sí |
| Vaciar | `s.clear()` | Sí |
| Unión | `s1.union(s2)` | No |
| Intersección | `s1.intersection(s2)` | No |
| Diferencia | `s1.difference(s2)` | No |
| Verificar tipo | `type(s)` | — |

---

## 12 · Booleanos

Los **booleanos** son tipos de datos binarios (`True` / `False`) que surgen de operaciones lógicas, o pueden declararse explícitamente.

> 💡 En Python, `True` y `False` se escriben con mayúscula inicial. Son instancias del tipo `bool`, que es una subclase de `int` (`True == 1`, `False == 0`).

---

### Índice

1. [Declarar Booleanos](#1-declarar-booleanos)
2. [Operadores de Comparación](#2-operadores-de-comparación)
3. [Operadores Lógicos — `and`, `or`, `not`](#3-operadores-lógicos--and-or-not)
4. [Valores Truthy y Falsy](#4-valores-truthy-y-falsy)
5. [Resumen — Cheatsheet](#5-resumen--cheatsheet)

---

### 1. Declarar Booleanos

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

### 2. Operadores de Comparación

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

### 3. Operadores Lógicos — `and`, `or`, `not`

Combinan o invierten expresiones booleanas.

#### `and` — `True` si **ambas** declaraciones son `True`

```python
tiene_dni = True
es_mayor = True

puede_votar = tiene_dni and es_mayor
print(puede_votar)  # → True

print(True and False)  # → False
print(False and False) # → False
```

#### `or` — `True` si **al menos una** declaración es `True`

```python
tiene_efectivo = False
tiene_tarjeta = True

puede_pagar = tiene_efectivo or tiene_tarjeta
print(puede_pagar)  # → True

print(False or False)  # → False
```

#### `not` — invierte el valor del booleano

```python
esta_cerrado = False
print(not esta_cerrado)  # → True

print(not True)   # → False
print(not False)  # → True
```

#### Tabla de verdad

| A | B | `A and B` | `A or B` | `not A` |
|---|---|:---------:|:--------:|:-------:|
| `True` | `True` | `True` | `True` | `False` |
| `True` | `False` | `False` | `True` | `False` |
| `False` | `True` | `False` | `True` | `True` |
| `False` | `False` | `False` | `False` | `True` |

---

### 4. Valores Truthy y Falsy

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

### 5. Resumen — Cheatsheet

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

---

## 13 · Operadores de Comparación

Como su nombre lo indica, sirven para comparar dos o más valores.
El resultado de esta comparación es un **booleano** (`True` / `False`).

---

### 1. Tabla de Operadores

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

### 2. `==` — Igual a

Compara si dos valores son iguales. Es sensible al tipo de dato.

```python
print(10 == 10)      # True
print(10 == 10.0)    # True  — int y float con el mismo valor son iguales
print(10 == "10")    # False — int vs str nunca son iguales
print("hola" == "Hola")  # False — mayúsculas importan
```

---

### 3. `!=` — Diferente a

Devuelve `True` cuando los valores **no** son iguales.

```python
print(5 != 6)   # True
print(5 != 5)   # False
print("a" != "A")  # True
```

---

### 4. `>` y `<` — Mayor / Menor que

```python
print(10 > 6)   # True
print(6 > 10)   # False

print(5 < 6)    # True
print(6 < 5)    # False
```

---

### 5. `>=` y `<=` — Mayor o igual / Menor o igual que

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

### 6. Comparar Expresiones

Los operadores actúan sobre el **resultado** de cualquier expresión, no solo variables.

```python
print(10 == 2 * 5)   # True
print(10 > 3 + 6)    # True
print(4 ** 2 == 16)  # True
```

---

### 7. Comparar Strings

Python compara strings **carácter a carácter** usando el orden Unicode.

```python
print("manzana" == "manzana")   # True
print("manzana" == "Manzana")   # False — 'M' (77) < 'm' (109)
print("b" > "a")                # True
print("abc" < "abd")            # True — difieren en el tercer carácter
```

---

### 8. Guardar el Resultado en una Variable

El resultado es un `bool` y puede almacenarse y reutilizarse.

```python
mi_bool = 5 >= 6
print(mi_bool)          # False
print(type(mi_bool))    # <class 'bool'>

es_mayor = 10 > 3
print(es_mayor)         # True
```

---

### 9. Resumen — Cheatsheet

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

---

## 14 · Operadores

Los **operadores** son símbolos o palabras clave que le indican a Python que realice una operación sobre uno o más valores. Se dividen en tres grupos principales: aritméticos, de comparación y lógicos.

---

### 1. Operadores Aritméticos

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

### 2. Operadores de Comparación

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

### 3. Operadores Lógicos

Permiten tomar decisiones basadas en **múltiples condiciones**. Trabajan con booleanos y también retornan un booleano.

```python
a = 6 > 5    # → True
b = 30 == 15 * 3  # → False (15*3 = 45, no 30)
```

---

#### `and` — todas las condiciones deben ser verdaderas

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

#### `or` — al menos una condición debe ser verdadera

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

#### `not` — invierte el booleano

Retorna `True` si el valor es `False`, y `False` si el valor es `True`.

```python
mi_bool = not a
print(mi_bool)
# → False   (a es True → not True → False)

print(not False)   # → True
print(not True)    # → False
```

---

#### Combinar operadores lógicos

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

### Resumen General

#### Aritméticos

| Operador | Operación | Ejemplo | Resultado |
|----------|-----------|---------|-----------|
| `+` | Suma | `3 + 2` | `5` |
| `-` | Resta | `3 - 2` | `1` |
| `*` | Multiplicación | `3 * 2` | `6` |
| `/` | División | `7 / 2` | `3.5` |
| `//` | División entera | `7 // 2` | `3` |
| `%` | Módulo | `7 % 2` | `1` |
| `**` | Potencia | `2 ** 3` | `8` |

#### Comparación

| Operador | Significado | Retorna |
|----------|-------------|---------|
| `==` | Igual | `bool` |
| `!=` | Distinto | `bool` |
| `>` | Mayor | `bool` |
| `<` | Menor | `bool` |
| `>=` | Mayor o igual | `bool` |
| `<=` | Menor o igual | `bool` |

#### Lógicos

| Operador | Comportamiento | Retorna `True` cuando... |
|----------|---------------|--------------------------|
| `and` | Todas verdaderas | Todas las condiciones son `True` |
| `or` | Al menos una verdadera | Al menos una condición es `True` |
| `not` | Invierte el booleano | El valor original es `False` |

---

## 15 · Control de Flujo — `if` / `elif` / `else`

El **control de flujo** determina el orden en que el código de un programa se va ejecutando. En Python, el flujo está controlado por tres mecanismos:

| Mecanismo | Descripción |
|-----------|-------------|
| **Estructuras condicionales** | Ejecutan código solo si se cumple una condición (`if`) |
| **Loops** | Repiten código un número de veces o mientras se cumpla una condición |
| **Funciones** | Agrupan código reutilizable que se ejecuta cuando se la llama |

> Esta guía cubre las **estructuras condicionales**. Los loops se cubren en la siguiente guía.

---

### 1. Estructura `if` básica

Ejecuta un bloque de código **solo si la expresión es `True`**.

```
if expresión:        ← expresión de resultado booleano (True/False)
    código           ← los dos puntos (:) dan paso al bloque
                     ← la indentación es OBLIGATORIA en Python
```

```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
# → Eres mayor de edad
```

> ⚠️ **La indentación es obligatoria.** Python usa los espacios (o tabulaciones) para saber qué código pertenece al bloque `if`. El estándar es **4 espacios**.

---

### 2. `if` / `else`

`else` define el código que se ejecuta cuando la condición del `if` es `False`.

```python
edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
# → Eres menor de edad
```

---

### 3. `if` / `elif` / `else`

`elif` ("else if") permite evaluar **múltiples condiciones** en secuencia. Se pueden incluir tantos `elif` como se necesiten. `else` y `elif` son **opcionales**.

```
if expresión:
    código a ejecutarse
elif expresión:
    código a ejecutarse
elif expresión:
    código a ejecutarse
...
else:
    código a ejecutarse
```

```python
nota = 75

if nota >= 90:
    print("Sobresaliente")
elif nota >= 75:
    print("Notable")
elif nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")
# → Notable
```

> 💡 Python evalúa las condiciones **de arriba hacia abajo** y ejecuta el primer bloque cuya condición sea `True`. El resto se ignora.

---

### 4. Condiciones compuestas

Se pueden combinar múltiples condiciones usando los operadores lógicos `and`, `or` y `not`.

```python
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puede conducir")
# → Puede conducir

temperatura = 35

if temperatura < 0 or temperatura > 40:
    print("Temperatura extrema")
# → Temperatura extrema

es_fin_de_semana = False

if not es_fin_de_semana:
    print("Día laboral")
# → Día laboral
```

---

### 5. `if` anidado

Un `if` dentro de otro `if`. Útil para verificar condiciones secundarias.

```python
usuario = "admin"
contrasena = "1234"

if usuario == "admin":
    if contrasena == "1234":
        print("Acceso concedido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no reconocido")
# → Acceso concedido
```

> 💡 Cada nivel de anidamiento agrega 4 espacios de indentación. Evitá anidar demasiados niveles — dificulta la lectura.

---

### 6. Condicional en una línea (ternario)

Python permite escribir un `if`/`else` simple en una sola línea.

```python
# Sintaxis: valor_si_true if condición else valor_si_false
edad = 20
estado = "mayor" if edad >= 18 else "menor"
print(estado)
# → mayor

# También dentro de un print
print("Par") if 10 % 2 == 0 else print("Impar")
# → Par
```

---

### 7. `match` / `case` *(Python 3.10+)*

Alternativa más legible al encadenamiento largo de `elif` cuando se compara una variable contra valores fijos.

```python
comando = "salir"

match comando:
    case "iniciar":
        print("Iniciando...")
    case "pausar":
        print("Pausado")
    case "salir":
        print("Saliendo...")
    case _:             # _ es el caso por defecto (equivale a else)
        print("Comando desconocido")
# → Saliendo...
```

---

### Resumen General

| Estructura | Cuándo usarla |
|-----------|---------------|
| `if` solo | Una sola condición, sin alternativa |
| `if` / `else` | Dos caminos posibles |
| `if` / `elif` / `else` | Tres o más caminos posibles |
| `if` anidado | Condición dentro de otra condición |
| Ternario | `if`/`else` simple en una línea |
| `match`/`case` | Comparar una variable contra valores fijos (Python 3.10+) |

#### Reglas clave

| Regla | Detalle |
|-------|---------|
| Indentación obligatoria | 4 espacios por nivel |
| Los dos puntos `:` | Siempre al final de `if`, `elif` y `else` |
| `elif` y `else` son opcionales | Pueden no aparecer |
| Se pueden usar varios `elif` | Sin límite de cantidad |
| Solo se ejecuta el primer bloque `True` | El resto se saltea |

---

## 16 · `match` / `case`

En Python 3.10 se incorpora la **coincidencia de patrones estructurales** mediante las declaraciones `match` y `case`. Esto permite asociar acciones específicas basadas en las formas o patrones de tipos de datos complejos, más allá de simples comparaciones de igualdad.

---

### 1. Estructura general

```
match objeto:
    case <patron_1>:
        <accion_1>
    case <patron_2>:
        <accion_2>
    case <patron_3>:
        <accion_3>
    case _:               ← comodín: coincide si ningún caso anterior lo hace
        <accion_comodin>
```

> ⚠️ `match` / `case` requiere **Python 3.10 o superior**.

---

### 2. Comparar contra valores literales

El uso más directo: comparar una variable contra strings, números u otros valores fijos. Es una alternativa más legible a una cadena larga de `elif`.

```python
# Con elif (forma clásica)
serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No conozco el fabricante")

# Con match (equivalente más limpio)
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No conozco el fabricante")
# → Nokia
```

---

### 3. El comodín `case _:`

`_` actúa como el `else` del `match`: se ejecuta si ningún caso anterior coincidió. Es opcional, pero recomendado para manejar valores inesperados.

```python
comando = "reiniciar"

match comando:
    case "iniciar":
        print("Iniciando...")
    case "pausar":
        print("Pausado")
    case "salir":
        print("Saliendo...")
    case _:
        print("Comando desconocido")
# → Comando desconocido
```

---

### 4. Coincidencia de patrones estructurales (diccionarios)

Los patrones no son únicamente valores literales. `match` puede **detectar y deconstruir** estructuras de datos: verifica que el diccionario tenga determinadas claves y, si coincide, extrae sus valores en variables locales automáticamente.

```python
case {"clave": variable, ...}:
```

Esto hace tres cosas a la vez:
1. **Verifica** que el dict tenga esas claves.
2. **Extrae** los valores correspondientes.
3. **Los vincula** a variables locales usables dentro del bloque.

#### Ejemplo con múltiples tipos de diccionario

```python
cliente = {"nombre": "Juan", "edad": 25, "ocupacion": "Programador", "ciudad": "Madrid"}
pelicula = {"titulo": "The Dark Knight", "ficha_tecnica": {"protagonista": "Christian Bale", "director": "Christopher Nolan", "anio": 2008}}
libro = {"titulo": "1984", "autor": "George Orwell", "publicacion": 1949}

elemento = [cliente, pelicula, libro]

for e in elemento:
    match e:
        case {"nombre": nombre, "edad": edad, "ocupacion": ocupacion, "ciudad": ciudad}:
            print("Es un cliente")
            print(nombre, edad, ocupacion, ciudad)
        case {"titulo": titulo, "ficha_tecnica": {"protagonista": protagonista, "director": director, "anio": anio}}:
            print("Es una pelicula")
            print(titulo, protagonista, director, anio)
        case {"titulo": titulo, "autor": autor, "publicacion": publicacion}:
            print("Es un libro")
            print(titulo, autor, publicacion)
        case _:
            print("No se que es este elemento")
            print(e)
```

**Salida:**
```
Es un cliente
Juan 25 Programador Madrid
Es una pelicula
The Dark Knight Christian Bale Christopher Nolan 2008
Es un libro
1984 George Orwell 1949
```

---

### 5. Estructuras anidadas

El patrón de diccionarios puede ser anidado. En el ejemplo anterior, `"ficha_tecnica": {"protagonista": protagonista, ...}` verifica la existencia del dict interno y extrae sus campos en una sola línea.

```python
pelicula = {
    "titulo": "Inception",
    "ficha_tecnica": {
        "protagonista": "Leonardo DiCaprio",
        "director": "Christopher Nolan",
        "anio": 2010
    }
}

match pelicula:
    case {"titulo": titulo, "ficha_tecnica": {"director": director}}:
        print(f"'{titulo}' fue dirigida por {director}")
# → 'Inception' fue dirigida por Christopher Nolan
```

---

### 6. `match` vs. `if/elif` — cuándo usar cada uno

| Situación | Usar |
|-----------|------|
| Comparar una variable contra valores fijos | `match` |
| Detectar la "forma" de un diccionario o estructura | `match` |
| Condiciones con rangos (`>`, `<`, `>=`) | `if/elif` |
| Condiciones compuestas con `and`/`or` | `if/elif` |
| Python < 3.10 | `if/elif` (match no disponible) |

---

### 7. Resumen — Cheatsheet

| Concepto | Ejemplo |
|----------|---------|
| Literal | `case "texto":` |
| Número | `case 42:` |
| Comodín | `case _:` |
| Extraer valor de dict | `case {"clave": variable}:` |
| Dict anidado | `case {"a": {"b": variable}}:` |
| Múltiples claves | `case {"k1": v1, "k2": v2}:` |

#### Reglas clave

| Regla | Detalle |
|-------|---------|
| Versión mínima | Python 3.10+ |
| Indentación | Obligatoria, igual que `if` |
| `case _:` | Opcional, siempre debe ir al final |
| Deconstrucción | Los valores extraídos son variables locales al bloque `case` |
| Orden de evaluación | De arriba hacia abajo; se ejecuta el primer `case` que coincida |

---

## Preguntas y Respuestas del Curso

Recopilación de dudas y respuestas que van surgiendo a lo largo del curso.

---

### Strings inmutables — `TypeError: 'str' object does not support item assignment`

**Código de referencia (`propiedades_string.py`):**

```python
nombres = "Carina"
nombres[0] = "K"
print(nombres)
```

#### ¿Qué error produce este código?

Al ejecutar el script, Python detiene el programa en la segunda línea con:

```text
TypeError: 'str' object does not support item assignment
```

En español: **un objeto `str` no admite asignación por índice**.

---

#### ¿Por qué ocurre ese error?

Porque en Python los **strings son inmutables**: una vez creados, no puedes cambiar un carácter individual dentro del mismo objeto.

La línea `nombres[0] = "K"` intenta modificar el string existente. Python no lo permite y lanza `TypeError`.

---

#### ¿Puedo leer un carácter con `[índice]`?

Sí. Leer funciona sin problema:

```python
nombres = "Carina"
print(nombres[0])   # "C"
print(nombres[-1])  # "a" (último carácter)
```

---

#### ¿Cómo cambio un carácter si no puedo usar `nombres[0] = "K"`?

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

#### ¿Es lo mismo reasignar la variable que modificar el string?

No.

| Acción | ¿Permitido? |
|--------|-------------|
| `nombres[0]` (leer) | Sí |
| `nombres[0] = "K"` (modificar) | No — `TypeError` |
| `nombres = "Karina"` (reasignar) | Sí — apunta a un string nuevo |

---

### Listas — `sort()` devuelve `None`

**Código de referencia (`listas.py`):**

```python
otra_lista = ["C", "D", "M", "A"]
lista_ordenada = otra_lista.sort()
print(lista_ordenada, type(lista_ordenada))
```

#### ¿Por qué `lista_ordenada` vale `None`?

Porque `sort()` es un método **in-place**: modifica la lista original directamente y no retorna nada (retorna `None`). Al asignar su resultado a una variable, esa variable recibe `None`.

```python
otra_lista = ["C", "D", "M", "A"]
lista_ordenada = otra_lista.sort()

print(lista_ordenada)          # → None
print(type(lista_ordenada))    # → <class 'NoneType'>
print(otra_lista)              # → ['A', 'C', 'D', 'M']  ← acá sí quedó ordenada
```

---

#### ¿Cómo obtengo una lista ordenada sin modificar la original?

Usando `sorted()` — es una función (no un método) que retorna una **lista nueva** y deja la original intacta.

```python
otra_lista = ["C", "D", "M", "A"]
lista_ordenada = sorted(otra_lista)

print(lista_ordenada)   # → ['A', 'C', 'D', 'M']
print(otra_lista)       # → ['C', 'D', 'M', 'A']  (sin cambios)
```

---

#### ¿Cuándo uso cada uno?

| | `lista.sort()` | `sorted(lista)` |
|---|---|---|
| Modifica el original | Sí | No |
| Retorna | `None` | Lista nueva ordenada |
| Cuándo usarlo | Cuando no necesitás el original | Cuando necesitás ambas versiones |

---

#### ¿`reverse()` tiene el mismo comportamiento?

Sí. `reverse()` también es in-place y retorna `None`. Su equivalente que retorna un nuevo objeto sin modificar el original es `reversed()`.

```python
lista = [1, 2, 3]
print(lista.reverse())        # → None  (modifica lista en el lugar)
print(lista)                  # → [3, 2, 1]

lista = [1, 2, 3]
print(list(reversed(lista)))  # → [3, 2, 1]
print(lista)                  # → [1, 2, 3]  (sin cambios)
```

---

### Diccionarios — ¿Por qué no se puede repetir una clave?

**Código de referencia (`diccionarios.py`):**

```python
mi_otro_diccionario = {
    "clave1": "valor1",
    "clave1": "valor2",
}
print(f"{mi_otro_diccionario} notese que el valor de clave 1 se reescribe")
```

#### ¿Por qué no pueden existir claves duplicadas en un diccionario?

Un diccionario es una estructura de **mapeo clave-valor**, y cada clave debe ser única porque es el **identificador** que Python usa para encontrar su valor. Si hubiera dos entradas con la misma clave, Python no sabría cuál devolver al hacer `mi_otro_diccionario["clave1"]`.

Internamente, Python usa una **tabla hash**: al insertar una clave calcula su `hash()` para determinar dónde guardar el valor. Si esa clave ya existe, simplemente **sobreescribe** el valor anterior.

---

#### ¿Python lanza un error si repito una clave?

No. Python **no lanza excepción**; gana silenciosamente el último valor asignado:

```python
mi_otro_diccionario = {
    "clave1": "valor1",  # se guarda "valor1"
    "clave1": "valor2",  # sobreescribe → "valor2"
}
print(mi_otro_diccionario)  # → {'clave1': 'valor2'}
```

---

#### ¿Cómo guardo múltiples valores para la misma clave?

Usando una **lista como valor**:

```python
mi_diccionario = {
    "clave1": ["valor1", "valor2"],
}
```

---

### Diccionarios y Listas — ¿Existe el operador spread `...` como en JavaScript?

Sí. Python usa `*` para listas y `**` para diccionarios.

#### Listas — `*`

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

combinada = [*lista1, *lista2]   # equivale a [...lista1, ...lista2]
print(combinada)  # → [1, 2, 3, 4, 5, 6]
```

#### Diccionarios — `**`

```python
base = {"nombre": "Juan", "edad": 20}
extras = {"peso": 80.5, "altura": 1.85}

cliente = {**base, **extras}     # equivale a { ...base, ...extras }
print(cliente)
# → {'nombre': 'Juan', 'edad': 20, 'peso': 80.5, 'altura': 1.85}

# Sobreescribir una clave (gana el último)
actualizado = {**base, "edad": 25}
print(actualizado)  # → {'nombre': 'Juan', 'edad': 25}
```

#### Comparación JS → Python

| JS | Python |
|----|--------|
| `[...a, ...b]` | `[*a, *b]` |
| `{ ...a, ...b }` | `{**a, **b}` |
| `{ ...obj, key: val }` | `{**obj, "key": val}` |
| `fn(...args)` (named) | `fn(**dict)` |

---

---

## 17 · Loops `for`

A diferencia de otros lenguajes de programación, los **loops `for`** en Python tienen la capacidad de iterar a lo largo de los elementos de cualquier secuencia (listas, strings, entre otros), en el orden en que dichos elementos aparecen.

### Conceptos clave

| Concepto | Descripción |
|----------|-------------|
| **Loop / bucle** | Secuencia de instrucciones de código que se ejecutan repetidas veces |
| **Iterable** | Objeto en Python que se puede recorrer (iterar) a lo largo de sus elementos: listas, strings, tuplas, diccionarios, sets, rangos… |

---

### 1. Estructura general

```
for item in iterable:   ← dos puntos (:) obligatorios
    expresión           ← indentación obligatoria en Python
```

| Parte | Descripción |
|-------|-------------|
| `item` | Cada uno de los elementos que compone el iterable. Se puede nombrar como quieras |
| `iterable` | La secuencia que se recorre: lista, string, tupla, dict, set, rango… |
| `expresión` | Código que se ejecuta en cada iteración. Puedes usar `item` dentro de ella |

> 💡 **`item` es una variable local** al bloque del `for`. Puedes acceder al elemento que se está iterando —o a sus atributos— a través del nombre que definas.

---

### 2. Iterar sobre una lista

```python
hijos = ["Sabina", "Higinio", "Jacinta", "Cándido", "Teodosia"]

for hijo in hijos:
    print(hijo)
# → Sabina
# → Higinio
# → Jacinta
# → Cándido
# → Teodosia
```

#### Saludar a cada elemento

```python
alumnos = ["María", "José", "Carlos", "Martina", "Isabel"]

for alumno in alumnos:
    print(f"Hola {alumno}")
# → Hola María
# → Hola José
# ...
```

---

### 3. Iterar sobre un string

Los strings son iterables: cada iteración entrega un carácter.

```python
palabra = "Python"
for letra in palabra:
    print(letra)
# → P
# → y
# → t
# → h
# → o
# → n
```

---

### 4. Filtrar con `if` dentro del `for`

```python
hijos = ["Gomoso Sue", "Gervasia", "Sabina", "Gaudelia", "Higinio"]

for nombre in hijos:
    if nombre.startswith("G"):
        print(nombre)
    else:
        print(f"{nombre} no comienza con G")
# → Gomoso Sue
# → Gervasia
# → Sabina no comienza con G
# → Gaudelia
# → Higinio no comienza con G
```

> 💡 `startswith("G")` retorna `True` si el string comienza con esa letra.

---

### 5. Acumular valores

Patrón clásico para sumar, contar o construir un resultado a partir de cada elemento:

```python
numeros = [1, 2, 3, 4, 5]
total = 0

for elemento in numeros:
    total += elemento
    print(f"Suma acumulada: {total}")
# → Suma acumulada: 1
# → Suma acumulada: 3
# → Suma acumulada: 6
# → Suma acumulada: 10
# → Suma acumulada: 15
```

#### Sumar pares e impares por separado

```python
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num

print(f"Suma de pares:   {suma_pares}")
print(f"Suma de impares: {suma_impares}")
# → Suma de pares:   54
# → Suma de impares: 48
```

---

### 6. Iterar sobre listas anidadas

```python
lista = [[1, 2], [3, 4], [5, 6]]

# Sin unpacking: cada elemento es una lista
for elemento in lista:
    print(elemento)
# → [1, 2]
# → [3, 4]
# → [5, 6]

# Con unpacking: desempaqueta cada sublista en variables
for a, b in lista:
    print(a, b)
# → 1 2
# → 3 4
# → 5 6
```

---

### 7. Iterar sobre diccionarios — `.items()`

```python
diccionario = {"nombre": "Juan", "edad": 20, "ciudad": "Madrid"}

for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
# → nombre: Juan
# → edad: 20
# → ciudad: Madrid
```

> 💡 `.items()` retorna pares `(clave, valor)`. También existen `.keys()` (solo claves) y `.values()` (solo valores).

---

### 8. `enumerate()` — índice + valor

Cuando necesitas el índice de cada elemento junto con su valor:

```python
hijos = ["Sabina", "Higinio", "Jacinta"]

for i, hijo in enumerate(hijos):
    print(f"{i}: {hijo}")
# → 0: Sabina
# → 1: Higinio
# → 2: Jacinta
```

#### Usar `enumerate()` para controlar el separador

```python
hijos = ["Sabina", "Higinio", "Jacinta", "Cándido"]

for i, hijo in enumerate(hijos):
    separador = ", " if i < len(hijos) - 1 else ""
    print(hijo + separador, end="")
# → Sabina, Higinio, Jacinta, Cándido
```

---

### 9. `join()` como alternativa a separadores manuales

Para mostrar los elementos de una lista separados por un carácter, `join()` es la forma más simple y directa:

```python
hijos = ["Sabina", "Higinio", "Jacinta", "Cándido"]

print(", ".join(hijos))
# → Sabina, Higinio, Jacinta, Cándido
```

`join()` pone el separador **entre** elementos, nunca al final. Es la forma idiomática en Python para este patrón.

---

### 10. Resumen — Cheatsheet

| Patrón | Código |
|--------|--------|
| Iterar lista | `for x in lista:` |
| Iterar string | `for letra in "Python":` |
| Filtrar en el loop | `for x in lista: if condición:` |
| Acumular | `total += x` dentro del `for` |
| Lista anidada sin unpacking | `for sub in lista:` → `sub` es la sublista |
| Lista anidada con unpacking | `for a, b in lista:` |
| Diccionario | `for k, v in d.items():` |
| Índice + valor | `for i, x in enumerate(lista):` |
| Unir con separador | `", ".join(lista)` |

### Reglas clave

| Regla | Detalle |
|-------|---------|
| Indentación | Obligatoria; define el cuerpo del `for` |
| Dos puntos `:` | Siempre al final de la línea `for` |
| `item` | Nombre arbitrario; se redefine en cada iteración |
| Iterables válidos | `list`, `str`, `tuple`, `dict`, `set`, `range`, y cualquier objeto iterable |

---
