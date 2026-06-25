mi_numero = 13
print(f"{type(mi_numero)}: {mi_numero}\n"
      f"La multiplicación de mi número por si mismo es: {mi_numero * mi_numero}")

mi_float = .13
print(f"{type(mi_float)}: {mi_float}\n"
      f"La multiplicación de mi_float por mi_numero es: {mi_float * mi_float}\n"
      f"y el resultado es de tipo: {type(mi_float * mi_float)}")

edad = int(input("Escribe edad: "))
#print("Tu próximo cumple tendrás:" + str((edad) + 1))
print(f"Tu próximo cumple tendrás: {edad + 1} años")