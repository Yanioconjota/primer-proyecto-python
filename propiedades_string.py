
nombre = "Carina"
#nombre[0] = "K" no permite el cambio porque el string es inmutable
nombre = "Karina" #Permitido porque sobreescrivimos la variable
n1 = "Ka"
n2 = "rina"

print(nombre)
print(n1 + n2)
print(f"{n1 * 5} Un string es multiplicable de la misma forma en que se puede concatenar")

#Un string puede ser multilíneas
poema = "Arriba de aquel cerrito\nHay una mata de ají\nDonde buscan los pollitos\nMuchas cosas para ti."
poema2 = """Arriba de aquel cerrito
Hay una mata de auyama
Donde buscan los pollitos
Muchas cosas para tu mama."""
print(poema)
print(poema2)

print("pollito" in poema)
print("ají" in poema2)
print("sol" not in poema)
print(f"El poema tiene {len(poema)} caracteres")
print(poema.find("Auyama".lower()))
print(poema.find("Ají".lower()))
