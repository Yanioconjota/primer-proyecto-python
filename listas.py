#Guarda similitudes con los strings
mi_lista = ["hola", 4, 6.7, "l"]
print(type(mi_lista))
print(mi_lista[::-1])

numeros = [1, 2, 3]
numeros2 = [4, 5, 6]
numeros3 = numeros + numeros2
print(numeros3)

#Pero a diferencia de los strings, no son inmutables
numeros3[0] = 'Uno'
print(numeros3)

numeros3.append(7)
print(numeros3)

numeros3.pop()
print(numeros3)

elemento_eliminado = numeros3.pop(2)
print(elemento_eliminado, numeros3)

otra_lista = ["C", "D", "M", "A"]
lista_ordenada = otra_lista.sort()
print(lista_ordenada, type(lista_ordenada))

otra_lista.sort()
print(otra_lista)

otra_lista.reverse()
print(otra_lista)