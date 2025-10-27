#1. Crear una función llamada imprimir_hola_mundo que imprima po pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Coloque su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

nombre = input("Coloque su nombre: ")
apellido = input("coloque su apellido: ")
edad = input("coloque su edad: ")
residencia = input("coloque su lugar de residencia: ")
informacion = informacion_personal(nombre, apellido, edad, residencia)
print(informacion)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_ circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

pi = 3.14

def calcular_area_circulo(radio):
    return pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

radio = float(input("Coloque el radio: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print (f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos/3600

segundos = int(input("Coloque cantidad de segundos: "))
horas = segundos_a_horas(segundos)

print(f"La cantidad de horas de {segundos} segundos es: {horas}")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    return numero*1, numero*2, numero*3, numero*4, numero*5, numero*6, numero*7, numero*8, numero*9, numero*10

numero = int(input("Coloque un numero: "))
tabla = tabla_multiplicar(numero)

print(f"Su numero es {numero} y su tabla de multiplicar de 1 al 10 es: {tabla}.")