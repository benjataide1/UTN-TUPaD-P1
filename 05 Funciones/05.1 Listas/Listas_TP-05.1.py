
# Actividad 1

lista_numeros = list(range(4, 101, 4))

# Actividad 2

lista_elementos = ["Hello World", 23, "UTN", True, 3.75]
print("Penultimo: ", lista_elementos[-1])

# Actividad 3

lista_vacia = []

lista_vacia.append("Animal")
lista_vacia.append("Jorge")
lista_vacia.append("Lautaro")

print(lista_vacia)


# Actividad 4

animales = ["perro", "gato", "conejo", "pez"]
animales[2] = "loro"
animales[-1] = "oso"

print(animales)

# Actividad 5

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
""" La funcion max(), elimina el numero mas alto de la lista "numeros" """

# Actividad 6

lista_salto = list(range(10, 31, 5))
print(lista_salto[0:2])

# Actividad 7

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "Clio"
autos[2] = "GTX"

print(autos)

# Actividad 8

dobles = []
dobles.append(10)
dobles.append(20)
dobles.append(30)

print(dobles)

# Actividad 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

compras[2].append("Jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

# Actividad 10

lista_anidada = [15,True,[25.5,57.9,30.6],False]
print(lista_anidada)