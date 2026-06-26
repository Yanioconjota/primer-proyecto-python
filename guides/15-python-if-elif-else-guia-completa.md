# Guía Completa de Control de Flujo — `if` / `elif` / `else`

El **control de flujo** determina el orden en que el código de un programa se va ejecutando. En Python, el flujo está controlado por tres mecanismos:

| Mecanismo | Descripción |
|-----------|-------------|
| **Estructuras condicionales** | Ejecutan código solo si se cumple una condición (`if`) |
| **Loops** | Repiten código un número de veces o mientras se cumpla una condición |
| **Funciones** | Agrupan código reutilizable que se ejecuta cuando se la llama |

> Esta guía cubre las **estructuras condicionales**. Los loops se cubren en la siguiente guía.

---

## 1. Estructura `if` básica

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

## 2. `if` / `else`

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

## 3. `if` / `elif` / `else`

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

## 4. Condiciones compuestas

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

## 5. `if` anidado

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

## 6. Condicional en una línea (ternario)

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

## 7. `match` / `case` *(Python 3.10+)*

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

## Resumen General

| Estructura | Cuándo usarla |
|-----------|---------------|
| `if` solo | Una sola condición, sin alternativa |
| `if` / `else` | Dos caminos posibles |
| `if` / `elif` / `else` | Tres o más caminos posibles |
| `if` anidado | Condición dentro de otra condición |
| Ternario | `if`/`else` simple en una línea |
| `match`/`case` | Comparar una variable contra valores fijos (Python 3.10+) |

### Reglas clave

| Regla | Detalle |
|-------|---------|
| Indentación obligatoria | 4 espacios por nivel |
| Los dos puntos `:` | Siempre al final de `if`, `elif` y `else` |
| `elif` y `else` son opcionales | Pueden no aparecer |
| Se pueden usar varios `elif` | Sin límite de cantidad |
| Solo se ejecuta el primer bloque `True` | El resto se saltea |
