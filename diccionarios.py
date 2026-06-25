mi_diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
}

print(mi_diccionario)
print(type(mi_diccionario))

mi_otro_diccionario = {
    "clave1": "valor1",
    "clave1": "valor2",
}
print(f"{mi_otro_diccionario} notese que el valor de clave 1 se reescribe")

resultado = mi_diccionario["clave1"]
print(resultado)

cliente = {
    "nombre": "Juan",
    "apellido": "Fuentes",
    "edad": 20,
    "peso": 80.5,
    "altura": 1.85
}

# Podemos imprimir una clave seleccionándola como índice
print(cliente, cliente["apellido"])

dic = {
    "c1": 55,
    "c2": [10,20,30],
    "c3": {"a1": 100, "a2": 200, "a3": 300}
}
print(dic)
print(dic["c2"][1])

dic1 = {
    "clave1": ["a", "b", "c"],
    "clave2": ["d", "e", "f"],
}

print(dic1["clave2"][1].upper())
dic1["clave3"] = ["g", "h", "i"]
print(dic1)

dic1["clave3"].append("j")
print(dic1)

print(dic1.keys())
print(dic1.values())
print(dic1.items())