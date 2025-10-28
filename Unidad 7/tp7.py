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

contador = 0

contactos = {}

for i in range(2):
    nombre = input("Coloque el nombre de la persona: ")
    numero = input("Coloque el numero de la persona: ")
    contactos[nombre] = numero

consultar = input("Coloque el nombre dela persona que quiere buscar: ")

if consultar in contactos:
    print(f"El numero de {consultar} es: {contactos[consultar]}")
else:
    print("Ese contacto no existe!!")

#