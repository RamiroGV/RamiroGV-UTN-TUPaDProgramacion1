#1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt", "w") as archivo:
    archivo.write("Nombre,Precio,Cantidad\n")
    archivo.write("Producto: Leche,Precio $1200,Cantidad: 3\n")
    archivo.write("Producto: Yerba,Precio $1900,Cantidad: 5\n")
    archivo.write("Producto: Manteca,Precio $800,Cantidad: 8\n")

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.

archivo = open("producto.txt", "a")
archivo.write(input("Coloque el producto que quiere agregar: ".capitalize()))
archivo.write(input("Coloque el precio del producto: "))
archivo.write(input("Coloque la cantidad del producto : "))
archivo.close()

#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre.capitalize(),
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.

buscar = input("Ingrese el nombre del producto que quiere buscar: ")

encontrado = False

for prod in productos:
    if prod["nombre".capitalize()] == buscar:
        print(prod)
        encontrado = True
if not encontrado:
    print("No se encontro el producto!!")

#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

with open("productos.txt", "w") as archivo:
    for prod in productos:
        archivo.write(f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n") 