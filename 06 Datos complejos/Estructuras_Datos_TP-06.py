import math
from collections import deque

# Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
                  1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 3800

print("-" * 30)
print(precios_frutas)

# Actividad 2
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

# Activiad 3
print(precios_frutas.keys())

for fruta in precios_frutas:
    print([fruta], end=" ")

# Activdad 4


class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(
            f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")


persona = Persona("Marcos", "Argentina", "32")
persona.saludar()

# Actividad 5


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        print(f"El area de un Circulo es: {math.pi * (self.radio ** 2)}")

    def calcular_perimetro(self):
        print(f"El perimetro de un Circulo es: {2 * math.pi * self.radio}")


circulo1 = Circulo(20)
circulo1.calcular_area()
circulo1.calcular_perimetro()


# Actividad 6
def balanceado(cadena):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in "({[":
            pila.append(caracter)
        elif caracter in ")}]":
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()

    return len(pila) == 0


# Resultados con el formato visual como en la imagen:
print(f"balanceado('({{[]}})') ➝ {balanceado('({[]})')}")
print(f"balanceado('({{[}})')  ➝ {balanceado('({[}')}")


# Actividad 7

class Turno_Banco:
    def __init__(self):
        self.cliente = deque()

    def agregar_cliente(self, cliente):
        self.cliente.append(cliente)

    def atender_cliente(self):
        # 🔄 Quitamos el primer elemento
        return self.cliente.popleft() if not self.esta_vacia() else "La cola está vacía"

    def esta_vacia(self):
        return len(self.cliente) == 0


turno = Turno_Banco()
turno.agregar_cliente("Marcos")
turno.agregar_cliente("Julieta")
turno.agregar_cliente("Juan")

# Mostramos nuestra cola
for e in turno.cliente:
    print(e)

print("-" * 30)

print(turno.atender_cliente())
# Mostramos nuestra cola pero sin el atendido
for e in turno.cliente:
    print(e)

# Actividad 8 y 9


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevoNodo = Nodo(dato)
        nuevoNodo.siguiente = self.cabeza
        self.cabeza = nuevoNodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("Siguiente -> None")


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior


lista = ListaEnlazada()
lista.insertar(10)
lista.insertar(20)
lista.mostrar()
lista.invertir()
lista.mostrar()
