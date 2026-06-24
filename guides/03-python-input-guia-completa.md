# Guía Completa de `input()` en Python

`input()` es lo que hace que tus programas sean **interactivos**. En lugar de que todo esté escrito de antemano, puedes pedirle información al usuario mientras el programa corre.

> 💡 Con `input()` tu programa puede preguntar "¿Cómo te llamas?" y luego usar la respuesta del usuario.

---

## 1. ¿Qué hace `input()`?

### Pedir datos al usuario

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

## 2. La Sintaxis de `input()`

### Estructura básica

Dentro de los paréntesis va el mensaje que verá el usuario. Este mensaje es opcional, pero casi siempre lo usamos.

```python
# Con mensaje (lo más común)
print(input("Escribe algo: "))

# Sin mensaje (solo espera que escribas)
print(input())
```

### Diferentes tipos de preguntas

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

## 3. `input()` Siempre Devuelve Texto

### Todo es un string

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

## 4. Combinar `input()` con Texto

### Concatenar la respuesta

Puedes unir lo que el usuario escribe con otro texto usando `+`.

```python
# Saludo personalizado
print("¡Hola, " + input("¿Cómo te llamas? ") + "!")
```

```
¿Cómo te llamas? Carlos
¡Hola, Carlos!
```

### Más ejemplos de concatenación

```python
# Bienvenida
print("Bienvenido a " + input("¿A qué ciudad viajas? "))

# Despedida
print("Hasta luego, " + input("Tu nombre: ") + ". ¡Vuelve pronto!")

# Confirmación
print("Tu correo es: " + input("Email: "))
```

---

## 5. Convertir a Números

### `int()` para números enteros

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

### `float()` para decimales

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

## 6. Ejemplos Prácticos

### Calculadora simple

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

### Calculador de edad

```python
print("Tu edad es:", 2025 - int(input("¿En qué año naciste? ")))
```

```
¿En qué año naciste? 1990
Tu edad es: 35
```

### Área de un rectángulo

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

### Saludo completo

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

## 7. Resumen Rápido

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

## Tabla de Referencia

| Necesidad                     | Código                                     | Resultado               |
|-------------------------------|--------------------------------------------|-------------------------|
| Pedir texto simple            | `input("Mensaje: ")`                       | String del usuario      |
| Mostrar lo que escribe        | `print(input("Mensaje: "))`                | Imprime la respuesta    |
| Unir con otro texto           | `"Hola, " + input("Nombre: ")`             | Concatenación           |
| Convertir a entero            | `int(input("Número: "))`                   | Para cálculos enteros   |
| Convertir a decimal           | `float(input("Número: "))`                 | Para cálculos con punto |
| Verificar tipo de dato        | `type(input("Algo: "))`                    | Siempre `<class 'str'>` |
