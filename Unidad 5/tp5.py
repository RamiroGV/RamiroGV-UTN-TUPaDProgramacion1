#1)Crear una lista con las notas de 10 estudiantes. •Mostrar la lista completa. •Calcular y mostrar el promedio. •Indicar la nota más alta y la más baja.

notas = [8, 7, 9, 6, 10, 5, 7, 8, 9, 6]

print("Notas de los estudiantes:")
for i, nota in enumerate(notas, start=1):
    print(f"Estudiante {i}: {nota}")

promedio = sum(notas) / len(notas)
print("Promedio:", promedio)

print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

#2)Pedir al usuario que cargue 5 productos en una lista. •Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). •
#Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

productos_ordenados = sorted(productos)
print("\nProductos ordenados alfabéticamente:")
for p in productos_ordenados:
    print(p)

producto_eliminar = input("\nIngrese el producto que desea eliminar: ")

if producto_eliminar in productos:
    productos.remove(producto_eliminar)
    print("\nLista actualizada:")
    for p in productos:
        print(p)
else:
    print("\nEl producto no se encontró en la lista.")

#3)Generar una lista con 15 números enteros al azar entre 1 y 100. •Crear una lista con los pares y otra con los impares. •Mostrar cuántos números tiene cada lista.

numeros = []
for i in range(15):
    n = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(n)

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Números ingresados:", numeros)
print("Números pares:", pares, "Cantidad:", len(pares))
print("Números impares:", impares, "Cantidad:", len(impares))

#4)Dada una lista con valores repetidos: datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]  •Crear una nueva lista sin elementos repetidos. •Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

sinrepetidos = []
for valor in datos:
    if valor not in sinrepetidos:
        sinrepetidos.append(valor)

print("Lista sin repetidos:", sinrepetidos)

#5)Crear una lista con los nombres de 8 estudiantes presentes en clase. •Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. •Mostrar la lista final actualizada.

estudiantes = ["Ana", "Juan", "Lucía", "Pedro", "María", "Carlos", "Sofía", "Luis"]

pregunta = input("¿Desea agregar un estudiante o eliminar uno? (agregar/eliminar): ").lower()

if pregunta == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif pregunta == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
    else:
        print("El estudiante no se encuentra en la lista.")
else:
    print("Opción no válida.")

print("\nLista final de estudiantes:", estudiantes)

#6)Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

numeros = [10, 20, 30, 40, 50, 60, 70]
print("Lista original:", numeros)

numeros = numeros[1:] + numeros 

print("Lista rotada:", numeros)

#7)Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.

temperaturas = [
    [15, 25],  # Lunes
    [16, 26],  # Martes
    [14, 24],  # Miércoles
    [13, 23],  # Jueves
    [15, 27],  # Viernes
    [17, 28],  # Sábado
    [16, 26]   # Domingo
]

print("Temperaturas de la semana (mín, máx):")
for i, temp in enumerate(temperaturas, start=1):
    print(f"Día {i}: Mínima = {temp[0]}, Máxima = {temp[1]}")

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.• Mostrar el promedio de cada estudiante.• Mostrar el promedio de cada materia.

notas = [
    [8, 7, 9],   # Estudiante 1
    [6, 8, 7],   # Estudiante 2
    [9, 9, 10],  # Estudiante 3
    [5, 6, 7],   # Estudiante 4
    [8, 7, 6]    # Estudiante 5
]

print("Promedio de cada estudiante:")
for i, estudiante in enumerate(notas, start=1):
    promedio = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i}: {promedio:.2f}")

print("\nPromedio de cada materia:")
for j in range(3):
    suma_materia = sum(notas[j])
    promedio_materia = suma_materia / 5
    print(f"Materia {j+1}: {promedio_materia:.2f}")

#9)Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).• Inicializarlo con guiones "-" representando casillas vacías.• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".• Mostrar el tablero después de cada jugada.

tablero = [["-" for _ in range(3)] for _ in range(3)]

print("Tablero inicial:")
for fila in tablero:
    print(" ".join(fila))
print()

for turno in range(9):
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"Turno del jugador {jugador}")
    
    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))
    
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada, intente de nuevo.")
        turno -= 1
        continue

    for fila_tablero in tablero:
        print(" ".join(fila_tablero))
    print()

#10 Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.• Mostrar el total vendido por cada producto.• Mostrar el día con mayores ventas totales.• Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [5, 3, 4, 2, 6, 3, 4],  # Producto 1
    [2, 4, 3, 5, 1, 2, 3],  # Producto 2
    [6, 5, 7, 6, 5, 6, 7],  # Producto 3
    [3, 2, 4, 3, 2, 4, 3]   # Producto 4
]

totales_productos = []
for i, producto in enumerate(ventas, start=1):
    total = sum(producto)
    totales_productos.append(total)
    print(f"Producto {i}: {total}")

totales_dias = [sum(ventas[j]) for j in range(7)]
dia_mayor = totales_dias.index(max(totales_dias)) + 1
print(f"\nDía con mayores ventas totales: Día {dia_mayor} con {max(totales_dias)} ventas")

producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
print(f"Producto más vendido en la semana: Producto {producto_mas_vendido} con {max(totales_productos)} ventas")