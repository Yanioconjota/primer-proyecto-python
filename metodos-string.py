texto = "Este es un texto"
resultado = texto
print(resultado.upper())
print(f"{resultado[2:8].upper()} Aplica el método en los caracteres seleccionados")
print(texto.split())
print(f"{texto.split("t")} usa como separador el caracter que recibe como parámetro")

a = "aprender"
b = "python"
c = "es"
d = "importante"
e = " ".join([a,b,c,d])

print(f"{e} une los elementos recibidos aplicando el primero como separador")
print(texto.find("s"))
print(texto.replace("texto","string"))

#Reemplazar 2 palabras
frase = "Si la implementación es difícil, puede ser una mala idea"
print(frase.replace("difícil", "fácil").replace("mala", "buena"))

