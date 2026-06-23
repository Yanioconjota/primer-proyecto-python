nombre = input("Ingresa tu nombre: ")
ventas = float(input("Ingrese el monto total en pesos de tus ventas: "))
comision = round(ventas * 13 / 100, 2)
print(f"{nombre} tu comision del '13%' sobre tus ventas es de: {comision} $ARS")