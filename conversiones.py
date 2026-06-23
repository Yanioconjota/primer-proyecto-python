"""
num1 = 20
num2 = 30.5
num3 = num1 + num2
num4 = int(num3)
print(f"type de num1: {type(num1)} {num1}\n"
      f"type de num2: {type(num2)} {num2}\n"
      f"type de num3: {type(num3)} {num3} es float al sumar num1 y num2 por conversión implicita\n"
      f"type de num4: {type(num4)} {num4} es integer por conversión explicita. No redondea, solo elimna los decimales\n")
"""
edad = input("Ingrese su edad: ")
print(type(edad))
edad = int(edad)
nueva_edad = edad + 1
print(nueva_edad, type(nueva_edad))