#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad= int(input("Ingrese su edad: "))

if(edad >= 18):
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota= int(input("Ingrese su nota: "))

if(nota >= 6):
    print("Aprobado!")
else:
    print("Desaprobado.")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num= int(input("Ingrese un numero: "))

if(num % 2 == 0):
    print("Ha ingresado un número par!!")
else:
    print("Por favor, ingrese un numero par.")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.

edad= int(input("Ingrese su edad: "))

if(edad < 12):
    print("Niño/a")
elif(12 <= edad < 18):
    print("Adolescente")
elif(18 <= edad < 30):
    print("Adulto/a joven")
elif(edad > 30):
    print("Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contra= input("Ingrese su contraseña: ")
long= len(contra)

if(8 <= long <= 14):
    print("Ha ingresado una contraseña conrrecta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]

media= statistics.mean(numeros_aleatorios)
mediana= statistics.median([numeros_aleatorios])
moda= statistics.mode([numeros_aleatorios])

print("Media: ",media)
print("Mediana: ",mediana)
print("Moda: ",moda)

if (moda < mediana < media):
    print("La distribucion tiene Sesgo Positivo.")
elif (media < mediana < moda):
    print("La distribucion tiene Sesgo Negativo.")
else:
    print("La distribucion no tiene sesgo.")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Escriba una frase o una palabra: ")

if (frase[-1] == "a"):
    print(frase + "!")
elif (frase[-1] == "e"):
    print(frase + "!")
elif (frase[-1] == "i"):
    print(frase + "!")
elif (frase[-1] == "o"):
    print(frase + "!")
elif (frase[-1] == "u"):
    print(frase + "!")
else:
    print(frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre= input("Ingrese su nombre: ")
eleccion= int(input("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.\nEliga entre 1 o 2 o 3: "))
mayusculas = nombre.upper()
minusculas = nombre.lower()
inicial = nombre.title()

if (eleccion == 1):
    print(mayusculas)
elif(eleccion == 2):
    print(minusculas)
elif(eleccion == 3):
    print(inicial)
else:
    pass

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

escala= int(input("Escriba la magnitud en escala de Richter: "))

if (escala < 3):
    print("Muy Leve")
if (3 <= escala < 4):
    print("Leve")
if (4 <= escala < 5):
    print("Moderado")
if (5 <= escala < 6):
    print("Fuerte")
if (6 <= escala < 7):
    print("Muy Fuerte")
if (escala > 7):
    print("Extremo")
else:
    pass

#10.Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio= input("En que hemisferio se encuenta(N/S): ").upper
mes= int(input("¿En que mes del año se encuentra? (1-12)"))
dia= int(input("¿Que dia es hoy? (1-31)"))
estacion = ""


if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacionnorte = "Invierno"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacionnorte = "Primavera"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacionnorte = "Verano"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacionnorte = "otoño"

if (hemisferio == "N"):
    estacion = estacionnorte
elif (hemisferio == "S"):
    if estacionnorte == "Invierno":
        estacion = "Verano"
    elif estacionnorte == "Verano":
        estacion = "invierno"
    elif estacionnorte == "Primavera":
        estacion = "Otoño"
    else:
        estacion = "Primavera"

print("En el hemisferio", hemisferio + ", el", str(dia) + "/" + str(mes), "es", estacion + ".")