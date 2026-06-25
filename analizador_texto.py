"""
1. Pedir un input de text (x)
2. Ingresar 3 letras a elección (x)
3. Devolver cuantas veces se repiten las letras que eligió (almacenar en variables) (x)
4. Cuantas palabras hay en todo el texto. Puedes convertir el texto en una lista y medir su longitud (x)
5. Devolver la primera letra y la última (x)
6. Devolver el texto invirtiendo el orden de las palabras (x)
7. Buscar si la palabra Python aparece en el texto. Usar booleanos para verificar si se encuentra y un diccionario para asociar el booleano a un string para mostrar al usuario (x)
"""
"Python es un lenguaje versátil, claro y potente, ideal para automatización, análisis de datos, inteligencia artificial, web y aprendizaje rápido hoy."

parrafo = input("Ingrese un texto: ")
letras = []

letras.append(input("Ingrese la letra 1: ").lower())
letras.append(input("Ingrese la letra 2: ").lower())
letras.append(input("Ingrese la letra 3: ").lower())

letra1_count = parrafo.count(letras[0])
letra2_count = parrafo.count(letras[1])
letra3_count = parrafo.count(letras[2])

palabrasLista = parrafo.split()
palabrasListaReversa = palabrasLista[::-1]
parrafoInvertido = " ".join(palabrasListaReversa)

cantidadPalabras = len(palabrasLista)
primeraPalabra = palabrasLista[0]
ultimaPalabra = palabrasLista[len(palabrasLista)-1]
respuestas = { True: "Si", False: "No" }
aparecePython = "python" in parrafo.lower()
mensaje = respuestas[aparecePython]

print(f"""
parrafo: {parrafo}
primera letra: {letras[0]} cantidad: {letra1_count}
segunda letra: {letras[1]} cantidad: {letra2_count}
tercera letra: {letras[2]} cantidad: {letra3_count}

cantidad de palabras: {cantidadPalabras}
primera palabra: {primeraPalabra}
última palabra: {ultimaPalabra}
primer letra: {parrafo[0]}
última letra: {parrafo[len(parrafo)-1]}
parrafo invertido: {parrafoInvertido}
aparece la palabra python: {mensaje}

""")