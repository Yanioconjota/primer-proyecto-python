if 3 > 100:
  print("Es correcto")
else:
  print("Es incorrecto")
  
mascota = "perro"
if mascota == "perro":
  print("Tu mascota es un perro")
elif mascota == "gato":
  print("Tu mascota es un gato")
elif mascota == "pez":
  print("Tu mascota es un pez")
elif mascota == "pajaro":
  print("Tu mascota es un pajaro")
elif mascota == "conejo":
  print("Tu mascota es un conejo")
elif mascota == "hamster":
  print("Tu mascota es un hamster")
elif mascota == "tortuga":
  print("Tu mascota es una tortuga")
else:
  print("No se que mascota tienes")
  
edad = 16
calificacion = 9

if edad > 18:
  print("Eres un adulto")
else:
  print("Eres un menor de edad")
  if calificacion >= 6:
    print("Has aprobado")
  else:
    print("No aprobaste")
  
  
  
""" num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
   print(f"{num1} y {num2} son iguales") """
   
edad = 16
tiene_licencia = False

if edad >= 18:
    if tiene_licencia:
        print("Puedes conducir")
    else:
        print("No puedes conducir. Necesitas contar con una licencia")
else:        
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
    
habla_ingles = True
sabe_python = False


if habla_ingles:
    if sabe_python:
        print("Cumples con los requisitos para postularte")
    else:
        print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas tener conocimientos de inglés")