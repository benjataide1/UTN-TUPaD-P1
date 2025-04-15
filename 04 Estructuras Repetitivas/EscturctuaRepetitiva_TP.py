from random import randint as ran


# Actividad 1


for i in range(0, 101, 1):
    print(i)


num = input("Ingrese un numero para ver la cantidad de digitios: ")
print(len(num))


# Actividad 3


inicio = int(input("Ingrese un Numeo para iniciar la iteracion: "))
final = int(input("Ingrese un Numero hasta donde quiere iterar: "))

count = 0
for i in range(inicio + 1, final):
    print(i)
    count += i

print(f"El total es:{count}")


# Actividadd 4

count = 0
condicion = True
while condicion:
    num = int(input("Ingrese un numero: "))
    if (num != 0):
        count += num
    elif (num == 0):
        print(f"El total acomulado es:{count}")
        condicion = False


# Actividad 5

aleatorio = ran(0, 9)
intentos = 0
num = 0
while aleatorio:
    num = int(input("Ingrese un numero para adividar el Num aleatorio: "))
    if (num == aleatorio):
        print(f"Felicidades el numero es {aleatorio}")
        num = aleatorio
        aleatorio = False
    intentos += 1

print(f"Total de intentos {intentos}- El numero es:{num}")


# Actividad 6

for i in range(100, -1, -1):
    if (i % 2 == 0):
        print(f"Los numeros pares son {i}")


# Actividad 7

num = int(input("Ingrese un numero para indicar el final de la iteracion: "))
count = 0
for i in range(0, num):
    count += i
print(f"La suma de los numeros es:{count}")


# Actividad 8


pares = 0
impares = 0
negativos = 0
positivos = 0
contador = 0
while contador < 100:

    num = int(input("Ingresa un numero: "))
    if (num > 0):
        if (num % 2 == 0 and num > 0):
            pares += 1
        else:
            impares += 1
        positivos += 1
    else:
        negativos += 1

    contador += 1

print(
    f"Pares:{pares}, Impares:{impares},Negativos:{negativos},Positivos:{positivos}")


# Actividad 9


total = 0
contador = 0
while contador < 10:

    num = int(input("Ingresa un numero: "))
    total += num
    contador += 1

print(f"La Media es {total / contador}")


# Actividad 10

num = input("Ingrese un Numero: ")
numReverso = ""
count = len(num)

while (count > 0):
    numReverso += num[count-1]
    count -= 1

print(f"El numero reverso es: {numReverso}")
