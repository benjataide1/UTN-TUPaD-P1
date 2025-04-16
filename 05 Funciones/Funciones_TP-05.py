import math

# Actividad 1


def imprimir_hola_mundo():
    print("Hola Mundo")


imprimir_hola_mundo()


# Actividad 2

def saludar_usuario(nombre):
    return f"Hola {nombre}!"


print(saludar_usuario("Marcos"))

# Actividad 3


def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}"


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

print(informacion_personal(nombre, apellido, edad, residencia))


# Actividad 4

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


radioArea = input("Ingrese el radio para calcular su Area: ")
print(f"El area es {calcular_area_circulo(radioArea)}")

radioPerimetro = input("Ingrese el radio para calcular su perimetro: ")
print(f"El perimetro es {calcular_perimetro_circulo(radioPerimetro)}")


# Actividad 5

def segundos_a_horas(segundos):
    return segundos / 3600


segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"Lo segundo a horas son {segundos_a_horas(segundos)}")


# Actividad 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)


# Actividad 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return [("suma: ", suma), ("Resta: ", resta), ("Multiplicacion: ", multiplicacion), ("Division: ", division)]


numero1 = int(input("Ingrese el Primer Numero: "))
numero2 = int(input("Ingrese el Segundo Numero: "))
tupla = operaciones_basicas(numero1, numero2)


for n in range(len(tupla)):
    print(f"- La {tupla[n][0]} es: {tupla[n][1]}")


# Actividad 8

def calcular_imc(peso, altura):

    return peso / (altura ** 2)


peso = float(input("Ingrese el peso el Kilogramos: "))
altura = float(input("Ingrese la altura: "))

print(f"El IMC es: {calcular_imc(peso, altura)}")


# Actividad 9

def celsius_a_fahrenheit(celsius):
    return (9/5 * celsius) + 32


celsius = float(input("Ingrese la cantidad de celcius a convertir: "))
print(f"La conversion es: {celsius_a_fahrenheit(celsius)}")

# Actividad 10


def calcular_promedio(a, b, c):
    return (a + b + c) / 3


notaA = int(input("Ingrese la Primera Nota: "))
notaB = int(input("Ingrese la Segunda Nota: "))
notaC = int(input("Ingrese la Tercera Nota: "))

print(f"El Promedio es: {calcular_promedio(notaA, notaB, notaC)}")
