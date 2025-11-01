#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

n = int(input("Coloque un numero: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

for i in range(1, n + 1):
    print(f"El factorial entre 1 y {n} es {factorial(i)}")

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

pos = int(input("Coloque un numero: "))

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)

for i in range(1, pos + 1):
    print(f"En la posicion {i} el factorial entre 1 y {pos} es {fibonacci(i)}")