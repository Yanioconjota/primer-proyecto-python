serie = "N-02"

""" if serie == "N-01":
  print("Samsung")
elif serie == "N-02":
  print("Nokia")
elif serie == "N-03":
  print("Motorola")
else:
  print("No conozco el fabricante") """
  
  
match serie:
  case "N-01":
    print("Samsung")
  case "N-02":
    print("Nokia")
  case "N-03":
    print("Motorola")
  case _:
    print("No conozco el fabricante")
  
cliente = {"nombre": "Juan", "edad": 25, "ocupacion": "Programador", "ciudad": "Madrid"}
pelicula = {"titulo": "The Dark Knight", "ficha_tecnica": {"protagonista": "Christian Bale", "director": "Christopher Nolan", "anio": 2008}}
libro = {"titulo": "1984", "autor": "George Orwell", "publicacion": 1949}

elemento = [cliente, pelicula, libro]

for e in elemento:
  match e:
    case {"nombre": nombre, "edad": edad, "ocupacion": ocupacion, "ciudad": ciudad}:
      print("Es un cliente")
      print(nombre, edad, ocupacion, ciudad)
    case {"titulo": titulo, "ficha_tecnica": {"protagonista": protagonista, "director": director, "anio": anio}}:
      print("Es una pelicula")
      print(titulo, protagonista, director, anio)
    case {"titulo": titulo, "autor": autor, "publicacion": publicacion}:
      print("Es un libro")
      print(titulo, autor, publicacion)
    case _:
      print("No se que es este elemento")
      print(e)
      
      