
from statistics import mode, median, mean

import random

# Ejercicio 1

edad_usuario = int(input("Ingrese su edad: "))

if edad_usuario >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


# Ejercicio 2

nota_usuario = int(input("Ingrese su nota: "))

if (nota_usuario >= 6):
    print("Aprobado")
else:
    print("Desaprobado")


# Ejericicio 3

numero = int(input("Ingrese un Numero Par:"))

if (numero % 2 == 0):
    print("Ha ingresado un numero par")
else:
    print("Por fabor, ingrese un numero par")


# Ejercicio 4

edad_usuario = int(input("Ingrese su edad:"))

if (edad_usuario < 12):
    print("Es Niño")
elif (edad_usuario >= 12 and edad_usuario < 18):
    print("Es adolescente")
elif (edad_usuario >= 18 and edad_usuario < 30):
    print("Es Adulto Joven")
else:
    print("Es Adulto mayor")

# Ejercicio 5

password = input("Ingrese su contraseña de 8 a 14 caracteres: ")
if (8 <= len(password) <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if (media > mediana > moda):
    print("Sesgo positivo , cola hacia la derecha")
elif (media < mediana < moda):
    print("Sesgo negativo, Cola hacia la izquieda")
else:
    print("No hay sesgo claro")


# Ejercicio 7

frase = input("Ingrese una frase o palabra: ")
last = frase[-1].upper()

if (last == "A" or last == "E" or last == "I" or last == "O" or last == "U"):
    print(frase + "!")
else:
    print(frase)


# Ejercicio 8

nombre = input("Ingrese su nombre: ")
numero = int(input(" - Ingrese un numero del 1 al 3  \n 1. Si quiere su nombre en mayúsculas. \n 2. Si quiere su nombre en minúsculas. \n 3. Si quiere su nombre con la primera letra mayúscula. \n Numero: "))

if (numero == 1):
    print(nombre.upper())
elif (numero == 2):
    print(nombre.lower())
else:
    print(nombre.title())


# Ejericio 9

magnitud = int(input("Ingrese la magnitud del terremoto: "))

if (magnitud < 3):
    print("Muy leve")
elif (magnitud >= 3 and magnitud < 4):
    print("Ligeramente perceptible")
elif (magnitud >= 4 and magnitud < 5):
    print("Moderado")
elif (magnitud >= 5 and magnitud < 6):
    print("Fuerte")
elif (magnitud >= 6 and magnitud < 7):
    print("Muy fuerte")
else:
    print("Extremo")

# Ejericio 10

hemisferio = input("Ingrese su hemisferio (N para Norte/S para Sur): ")
mes = int(input("Ingrese el mes del 1 al 12: "))
dia = int(input("Ingrese el día: "))

if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"
elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        estacion = "Otoño"
    else:
        estacion = "Primavera"
else:
    estacion = "Fecha no válida"

print(f"La estación actual es: {estacion}")
