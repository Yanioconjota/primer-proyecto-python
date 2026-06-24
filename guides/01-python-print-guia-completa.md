# Guía Completa de `print()` en Python

`print()` es la primera instrucción que aprendes en Python. Su trabajo es simple: mostrar texto o números en la pantalla.

> 💡 Todo lo que pongas dentro de los paréntesis de `print()` aparecerá en la consola de Python.

---

## 1. Lo Básico

### Mostrar texto

Para mostrar texto, escríbelo entre comillas dentro de los paréntesis.

```python
print("Hola, mundo")
# → Hola, mundo

print("Bienvenido a Python")
# → Bienvenido a Python

print("¡Esto es muy fácil!")
# → ¡Esto es muy fácil!
```

### Mostrar números

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

### Línea vacía

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

## 2. Comillas Simples y Dobles

### Ambas funcionan igual

Python acepta comillas simples `'texto'` o dobles `"texto"`.

```python
print("Hola")   # → Hola
print('Hola')   # → Hola
```

### Cuando el texto tiene comillas

```python
print("Él dijo 'hola' y se fue")
# → Él dijo 'hola' y se fue

print('Ella respondió "adiós"')
# → Ella respondió "adiós"
```

> 💡 **Tip:** La mayoría de programadores usan comillas dobles `"texto"` por costumbre. Lo importante es ser consistente.

---

## 3. Imprimir Varias Cosas a la Vez

### Separar con comas

Puedes poner varios elementos separados por comas. Python los imprime con un espacio entre cada uno.

```python
print("Hola", "mundo")
# → Hola mundo

print("El resultado es:", 42)
# → El resultado es: 42

print("Suma:", 10, "+", 5, "=", 15)
# → Suma: 10 + 5 = 15
```

### Cambiar el separador con `sep`

```python
print("A", "B", "C")           # → A B C
print("A", "B", "C", sep="-")  # → A-B-C
print("A", "B", "C", sep="")   # → ABC
print(2024, 12, 25, sep="/")   # → 2024/12/25
print(14, 30, 00, sep=":")     # → 14:30:0
```

---

## 4. Controlar los Saltos de Línea

### Comportamiento normal

Cada `print()` termina con un salto de línea automático.

```python
print("Línea 1")
print("Línea 2")
print("Línea 3")
```

### Cambiar el final con `end`

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

## 5. Caracteres Especiales

### Secuencias de escape

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

## 6. Texto en Varias Líneas

### Comillas triples

```python
print("""
Bienvenido al sistema.
Por favor, siga las instrucciones.
Gracias por su visita.
""")
```

### Crear menús o arte ASCII

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
