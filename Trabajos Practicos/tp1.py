#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre1 = "Marcos"

print(f" Hola {nombre1}!")

#Ejercicio 3
nombre2 = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
residencia = input("Ingrese lugar de residencia:")

print(f"Soy {nombre2} {apellido}, tengo {edad} y vivo en {residencia}. ")

#Ejercicio 4
pi = 3.1416
radio = input("Ingrese el radio:")

area = pi*(int(radio)**2)
perimetro = 2 * pi * int(radio)

print(f"Su area es {area} y su perimetro es {perimetro}")

#Ejercicio 5
segundos = input("ingrese cantidad de segundos:")

horas = int(segundos) / 3600

print(f"Los segundos ingresados son {horas} horas.")

#Ejercicio 6
numero = input("Coloque un numero:")

multiplos = int(numero)*2, int(numero)*3, int(numero)*4, int(numero)*5, int(numero)*6, int(numero)*7, int(numero)*8, int(numero)*9,
print (f"Sus multiplos son {multiplos}")

#Ejercicio 7
numero1 = int(input("Coloque un numero distinto de 0:"))
numero2 = int(input("Coloque otro numnero distiento de 0:"))

suma = numero1 + numero2
divisor = numero1/numero2
multiplicacion = numero1 * numero2
resta = numero1 - numero2

print(f"La suma de los dos numeros es {suma}, La division de los dos numeros es {divisor}, La multiplicacion de los dos numeros es {multiplicacion}, La resta de los dos numeros es {resta}")

#Ejercicio 8
altura = input("Coloque su altura en metros:")
peso = input("Coloque su peso en kilogramos:")

masaCorporal = float(altura) / int(peso)

print(f"Su indice de masa corporal es de {masaCorporal}.")

#Ejercicio 9
termperatura1 = input("Coloque la temperatura en grados Celsius:")

temperatura2 = ((9/5)*float(termperatura1)) + 32

print(f"Su temperatura en grados Fahrenheit es: {temperatura2}.")

#Ejercicio 10
numero1 = input("Coloque su primer numero:")
numero2 = input("Coloque su segundo numero:")
numero3 = input("Coloque su tercer numero:")

promedio = (float(numero1) + float(numero2) + float(numero3))/3

print(f"El promedio de sus tres nunero es: {promedio}.") 