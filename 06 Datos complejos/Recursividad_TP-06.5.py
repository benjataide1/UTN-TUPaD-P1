

# Ejercicio 1

def factorial_recursivo(num):
    if (num == 1):
        return 1
    else:
        return num * factorial_recursivo(num - 1)


num = int(input("Ingrese un Numero a factoriar: "))

for i in range(1, num + 1):
    print(f"{i}! = {factorial_recursivo(i)}")


# Ejercicio 2

def fibonacci_recursivo(num):
    if (num == 0):
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_recursivo(num - 1) + fibonacci_recursivo(num - 2)


posicion = int(input("Ingrese una posición para la serie de Fibonacci: "))


for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci_recursivo(i)}")


# Ejercicio 3

def potencia_recursivo(base, exponente):
    if (exponente == 0):
        return 1
    else:
        return base * potencia_recursivo(base, exponente - 1)


base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia_recursivo(base, exponente)
print(f"{base}^{exponente} = {resultado}")


# Ejercicio 4

def decimalBinario_recursivo(num):

    if (num == 1 or num == 0):
        return "1"
    else:
        return decimalBinario_recursivo(num//2) + str(num % 2)


decimal = int(input("Ingrese un Decimal: "))
decimalBinario_recursivo(decimal)