#1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios: ● Naranja = 1200 ● Manzana = 1500 ● Pera = 2300

precios_fruta = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_fruta["Naranja"] = 1200
precios_fruta["Manzana"] = 1500
precios_fruta["Pera"] = 2300

print(precios_fruta)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: ● Banana = 1330 ● Manzana = 1700 ● Melón = 2800

precios_fruta["Banana"] = 1330
precios_fruta["Manzana"] = 1700
precios_fruta["Melón"] = 2800

print(precios_fruta)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

for clave, valor in precios_fruta.items():
    print(f"{clave}")

#4) Escribí un programa que permita almacenar y consultar números telefónicos. • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

for i in range(5):
    nombre = input("Coloque el nombre de la persona: ")
    numero = input("Coloque el numero de la persona: ")
    contactos[nombre] = numero

consultar = input("Coloque el nombre de la persona que quiere buscar: ")

if consultar in contactos:
    print(f"El numero de {consultar} es: {contactos[consultar]}")
else:
    print("Ese contacto no existe!!")

#5)Solicita al usuario una frase e imprime: • Las palabras únicas (usando un set). • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresá una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:")
print(palabras_unicas)

contador = {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print("Cantidad de veces que aparece cada palabra:")
print(contador)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(1):
    nombre = input("Nombre del alumno: ")
    nota1 = float(input("Coloque la primera nota: "))
    nota2 = float(input("Coloque la segunda nota: "))
    nota3 = float(input("Coloque la tercera nota: "))
    alumnos[nombre] = (nota1, nota2, nota3)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre} su promedio es: {promedio}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: • Mostrá los que aprobaron ambos parciales. • Mostrá los que aprobaron solo uno de los dos. • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).



#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario: • Consultar el stock de un producto ingresado. • Agregar unidades al stock si el producto ya existe. • Agregar un nuevo producto si no existe.

productos = {"Nafta Comun" : 12000, "Nafta Premium" : 15000, "Diesel Comun" : 8000, "Diesel Premium" : 23000}

print(productos.get(input("Coloque el producto que quiere revisar: ")))

modificar = input("¿Que producto quiere modificar(Nafta Comun, Nafta Premium, Diesel Comun o Diesel Premium)?")

if modificar in productos:
    nuevo_valor = input(f"Coloque el nuevo valor de {modificar}: ")
    productos[modificar] = nuevo_valor
    print("Modificacion exitosa!!!")
else:
    print("No existe ese producto.")

agregar = input("Coloque el nombre del producto que quiere agregar: ")
cantidad = input("Coloque la cantidad del producto: ")

productos[agregar] = cantidad

print("Producto nuevo agregado!!")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("Lunes", "07:00"): "Gimnasio",
    ("Lunes", "08:30"): "Reunion",
    ("Martes", "10:00"): "Dentista",
    ("Miercoles", "16:00"): "Entrenamiento",
    ("Jueves", "20:00"): "Cena con amigos",
    ("Viernes", "21:00"): "Cine",
}

dia = input("Coloque el dia: ")
hora = input("Coloque el horario: ")

clave = (dia, hora)

if clave in agenda:
    print(agenda[clave])
else:
    print("En ese dia y horario no tienes ningun evento.")

#