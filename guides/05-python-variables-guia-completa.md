# Guía Completa de Variables en Python

Una **variable** es como una caja con etiqueta donde guardas un valor para usarlo después. En lugar de repetir el mismo dato una y otra vez, lo guardas en una variable y usas su nombre.

> 💡 Las variables te permiten guardar información, modificarla, y usarla en cualquier parte de tu programa.

---

## 1. ¿Qué es una Variable?

### Una etiqueta para un valor

Imagina que tienes una caja donde guardas algo. Le pones una etiqueta para saber qué hay adentro. Eso es exactamente una variable: un nombre que apunta a un valor.

```
nombre  →  "María"
```

Aquí, `nombre` es la etiqueta (variable) y `"María"` es el valor que guardamos.

### Crear una variable

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

## 2. Reglas para Nombrar Variables

Existen convenciones y buenas prácticas asociadas al nombre de las variables creadas en Python. Tienen la intención de facilitar la **interpretabilidad** y el **mantenimiento** del código.

### Las 6 reglas clave

| # | Regla            | Descripción                                                                 |
|---|------------------|-----------------------------------------------------------------------------|
| 1 | **Legible**      | El nombre de la variable debe ser relevante según su contenido              |
| 2 | **Unidad**       | No pueden existir espacios; usa guiones bajos para separar palabras         |
| 3 | **Hispanismos**  | Omitir signos específicos del español: tildes (`á`, `é`) y la letra `ñ`    |
| 4 | **Números**      | No deben empezar por número, aunque pueden contenerlos al final             |
| 5 | **Símbolos**     | No incluir: `" ' , < > / ? \ ( ) ! @ # $ % ^ & * ~ - +`                   |
| 6 | **Palabras clave** | No usar palabras reservadas por Python (`print`, `if`, `True`, `class`…) |

### Nombres válidos

| Regla                            | Ejemplo                              |
|----------------------------------|--------------------------------------|
| ✓ Letras y guiones bajos         | `nombre`, `mi_variable`, `_privado`  |
| ✓ Números (no al inicio)         | `usuario1`, `total2024`, `item_3`    |
| ✓ snake_case (recomendado)       | `nombre_completo`, `precio_total`    |
| ✓ Nombres descriptivos           | `cantidad_productos` mejor que `x`   |

### Nombres inválidos

| Regla                            | Ejemplo                              |
|----------------------------------|--------------------------------------|
| ✗ Empezar con número             | `1nombre`, `2024_total` — Error      |
| ✗ Espacios                       | `mi variable` — Usa: `mi_variable`   |
| ✗ Caracteres especiales          | `precio$`, `nombre@` — Error         |
| ✗ Hispanismos                    | `año`, `dirección`, `tamaño` — Evitar |
| ✗ Palabras reservadas            | `print`, `True`, `if`, `class`       |

### Tabla rápida de referencia

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

## 3. Reasignar Variables

### Cambiar el valor

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

### Actualizar con operaciones

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

## 4. Tipos de Datos en Variables

### Una variable puede guardar cualquier tipo

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

### Python es de tipado dinámico

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

### Conversiones de tipos

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

## 5. Usar Variables con `print()`

### Mostrar el valor

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

### Combinar variables con texto

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

## 6. Operaciones con Variables

### Matemáticas

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

### Variables con `input()`

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

## 7. Múltiples Variables

### Asignación múltiple

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

## 8. Resumen

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

## Tabla de Referencia

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
