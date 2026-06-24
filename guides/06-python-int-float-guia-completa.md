# Guía Completa de Integers y Floats en Python

Python tiene dos tipos de números: **integers** (enteros, sin decimales) y **floats** (con decimales). Entender la diferencia es fundamental para hacer cálculos correctos en tus programas.

> 💡 **La regla de oro:** si tiene punto decimal, es `float`. Si no tiene punto, es `int`.

---

## 1. Los Dos Tipos de Números

### `int` — Integer (Entero)

Números enteros. Sin punto decimal. Positivos, negativos o cero.

```python
42    -15    0    1000    -999
```

> 🔑 Sin punto decimal

### `float` — Float (Decimal)

Números decimales. También llamados "de punto flotante". Siempre tienen punto.

```python
3.14    -0.5    100.0    2.718
```

> 🔑 Con punto decimal

### Verificar el tipo

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

## 2. Operaciones Básicas

### Las cuatro operaciones

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

## 3. Operaciones Especiales

### División entera, módulo y potencia

| Operador | Operación       | Ejemplo    | Resultado |
|----------|-----------------|------------|-----------|
| `//`     | División entera | `17 // 5`  | `3`       |
| `%`      | Módulo (resto)  | `17 % 5`   | `2`       |
| `**`     | Potencia        | `2 ** 3`   | `8`       |

### División entera `//`

Devuelve solo la parte entera del resultado, descartando los decimales.

```python
print(17 / 5)     # 3.4   (división normal)
print(17 // 5)    # 3     (división entera)

print(10 // 3)    # 3
print(25 // 4)    # 6
print(100 // 7)   # 14
```

### Módulo `%` (el resto)

Devuelve lo que sobra después de dividir. Muy útil para saber si un número es par o impar.

```python
print(17 % 5)     # 2  (17 = 5×3 + 2)
print(10 % 3)     # 1  (10 = 3×3 + 1)
print(20 % 4)     # 0  (división exacta)

# ¿Es par o impar?
print(8 % 2)      # 0 → es par
print(7 % 2)      # 1 → es impar
```

### Potencia `**`

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

## 4. Mezclar `int` y `float`

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

## 5. Convertir entre Tipos

### De `float` a `int`

Usa `int()` para convertir un float a entero. **Trunca** los decimales (no redondea).

```python
print(int(3.7))    # 3  (no redondea, trunca)
print(int(3.2))    # 3
print(int(9.99))   # 9  (¡no es 10!)
print(int(-2.8))   # -2 (hacia el cero)
```

### De `int` a `float`

Usa `float()` para convertir un entero a decimal. Agrega `.0` al final.

```python
print(float(5))     # 5.0
print(float(100))   # 100.0
print(float(-7))    # -7.0
```

### Convertir desde texto

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

## 6. Redondear Números

El redondeo facilita la interpretación de los valores calculados al limitar la cantidad de decimales que se muestran en pantalla. También permite aproximar valores decimales al entero más próximo.

### Sintaxis de `round()`

```
round(number, ndigits)
         │         └── cantidad de decimales (si se omite, el resultado es entero)
         └── valor a redondear
```

| Parámetro  | Descripción                                              |
|------------|----------------------------------------------------------|
| `number`   | El valor a redondear                                     |
| `ndigits`  | Cantidad de decimales. Si se omite, devuelve un entero   |

### Ejemplos de uso

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

## 7. Números Grandes y Pequeños

### Notación científica

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

### Separador visual (guión bajo)

Para números largos, puedes usar `_` como separador visual. Python lo ignora completamente.

```python
poblacion = 8_000_000_000
precio = 1_500_000.50

print(poblacion)  # 8000000000
print(precio)     # 1500000.5
```

---

## 8. Errores Comunes

### División por cero

Dividir por cero causa un error. Python no puede calcular algo dividido entre nada.

```python
print(10 / 0)
# ZeroDivisionError: division by zero

print(10 // 0)
# ZeroDivisionError: integer division by zero

print(10 % 0)
# ZeroDivisionError: integer modulo by zero
```

### Precisión de floats

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

## 9. Resumen — Cheatsheet de Números

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

## Tabla de Referencia

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
