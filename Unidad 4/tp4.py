#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = input("Coloque un numnero entero: ")

if numero.startswith("-"):
    cantidad = len(numero) - 1
else:
    cantidad = len(numero)

print("El numero tiene,", cantidad  ,"digitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

suma = 0

num1 = int(input("Coloque un numero: "))
num2 = int(input("Coloque otro numero: "))

if (num1 > num2):
    for i in range(num2 + 1, num1):
        suma += i
else:
    (num2 > num1)
    for i in range(num1 + 1, num2):
        suma += i
print(f"La suma de los numero entre ", num1 ,"y", num2 , "es: ", suma ,".")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

corte = 0
suma = 0


numero = int(input("Ingrese un numero(0 para terminar): "))

while numero != corte:
    suma += numero
    numero = int(input("Ingrese un numero(0 para terminar): "))

print("La suma total es de: ", suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

numeros =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numero_secreto = numeros[0]
adivinanza = -1
intentos = 0

numero = int(input("Adivina el numero entre 0 al 9, coloque su eleccion: "))

while numero != numero_secreto:
    adivinanza = int(input("Ingrese su otro numero: "))
    intentos += 1
    if adivinanza == numero_secreto:
        print=("Acertaste, fueron", intentos ,"intetos")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

suma = 0

num1 = 0
num2 = int(input("Coloque otro numero entero positivo: "))

if     (num2 > num1):
    for i in range(num1 + 1, num2):
        suma += i
else:
    (num1 > num2)
    print("Su numero es negativo.")
print(f"La suma de los numero entre ", num1 ,"y", num2 , "es: ", suma ,".")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
positivos = 0
negativos = 0


for i in range(100):
    numero = int(input(f"Ingrese el número {i+1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"\nCantidad de números pares:" , pares,)
print(f"Cantidad de números impares: ", impares, )
print(f"Cantidad de números positivos:" , positivos,)
print(f"Cantidad de números negativos: ", negativos,)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).


cantidad = 100  
suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

media = suma / cantidad

print(f"\nLa media de los {cantidad} números ingresados es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número positivo: "))

numero_invertido = 0
num = numero

while num > 0:
    digito = num % 10
    numero_invertido = numero_invertido * 10 + digito
    num = num // 10

print(f"El número invertido es:" ,numero_invertido)