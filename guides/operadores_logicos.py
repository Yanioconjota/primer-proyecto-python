# Se permiten valores encadenados pero puede ser confuso
mi_bool = 4 < 5 < 6
print(mi_bool)

# Es más legible la comparación mediante el uso de operadores lógicos

# and se fija que se cumplan 2 condiciones
mi_bool = 4 < 5 and 5 > 6
print(mi_bool)

mi_bool = (4 < 5) and (5 == 2 + 3)
print(mi_bool)

mi_bool = (55 == 55) and ("perro" == "perro")
print(mi_bool)

# or se fija que se cumpla al menos una condición
mi_bool = (10 == 10) or ("perro" == "Perro")
print(mi_bool)

texto = "esta frase es breve"

mi_bool = ("frase" in texto) or (1 > 9)
print(mi_bool)

# No se cumple ninguna condición
mi_bool = ("frase" not in texto) or (1 > 9)
print(mi_bool)

# Es la negación de una condición, es una doble negación
mi_bool = not ("a" == "a")
print(mi_bool)

# Como la condición es falsa, entonces not mostrará verdadero
mi_bool = not ("a" != "a")
print(mi_bool)