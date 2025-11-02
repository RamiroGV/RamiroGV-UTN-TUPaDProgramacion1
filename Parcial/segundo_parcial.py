import csv
import os


NOMBRE_ARCHIVO = "catalogo.csv"
FIELDNAMES = ["TITULO", "CANTIDAD"] 

def guardar_catalogo(catalogo):
    """Guarda toda la lista de libros en el archivo CSV, sobrescribiendo el contenido."""
    # Se usa "w" (write) para sobrescribir y asegurar consistencia
    with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=FIELDNAMES)
        escritor.writeheader()
        escritor.writerows(catalogo)

def obtener_catalogo():
    """Lee y devuelve el catálogo desde el archivo. Crea el archivo si no existe."""
    catalogo = []
    
    # Si el archivo no existe, lo crea y lo inicializa vacío
    if not os.path.exists(NOMBRE_ARCHIVO):
        guardar_catalogo(catalogo)
        return catalogo

    # Lee el archivo existente
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            try:
                cantidad = int(fila["CANTIDAD"])
            except ValueError:
                cantidad = 0

            catalogo.append({
                "TITULO": fila["TITULO"], 
                "CANTIDAD": cantidad
            })
                
    return catalogo

def validar_titulo(nombre):
    """Valida que el TITULO no esté vacío."""
    nombre = nombre.strip()
    if not nombre:
        print("El título no puede ser vacío.")
        return False
    return True

def validar_cantidad_entera(cantidad_str):
    """Valida si la cadena representa un número entero NO NEGATIVO (>= 0)."""

    cantidad_str = cantidad_str.strip()
    
    # Chequeo de signo
    if cantidad_str.startswith('-'):
        print("La cantidad no puede ser negativa.")
        return False
        
    # Chequeo de dígitos
    if not cantidad_str.isdigit():
        print("La cantidad debe ser un número entero (sin puntos o letras).")
        return False
        
    return True

def obtener_indice_libro(nombre_buscado, catalogo):
    """Busca un TITULO y devuelve su índice en la lista. Retorna -1 si no se encuentra."""
    nombre_buscado = nombre_buscado.strip().lower()

    for i, libro in enumerate(catalogo):
        if libro["TITULO"].strip().lower() == nombre_buscado: 
            return i
    return -1

# FUNCIONALIDADES DEL MENÚ

def agregar_titulo(catalogo):
    print("\n=== AGREGAR TÍTULO INDIVIDUAL ===")
    
    # Bucle para asegurar un título válido y no duplicado
    while True:
        titulo = input("Ingrese TITULO del libro: ").strip()
        if not validar_titulo(titulo):
            continue
            
        if obtener_indice_libro(titulo, catalogo) != -1:
            print(f"ERROR: El título '{titulo}' ya existe en el catálogo.")
            continue
        break
        
    # Bucle para asegurar cantidad válida
    while True:
        cantidad_str = input("Ingrese CANTIDAD inicial de ejemplares (>= 0): ").strip()
        if validar_cantidad_entera(cantidad_str):
            break
            
    cantidad = int(cantidad_str)

    nuevo_libro = {"TITULO": titulo, "CANTIDAD": cantidad}
    catalogo.append(nuevo_libro)
    guardar_catalogo(catalogo)
    print(f"\n¡Libro '{titulo}' (Stock: {cantidad}) agregado exitosamente!") 


# Ingresar múltiples títulos
def ingresar_multiples_titulos():
    print("\n=== INGRESAR MÚLTIPLES TÍTULOS ===")
    catalogo = obtener_catalogo()
    
    while True:
        num_libros_str = input("¿Cuántos libros desea cargar?: ").strip()
        if validar_cantidad_entera(num_libros_str) and int(num_libros_str) > 0:
            num_libros = int(num_libros_str)
            break
        print("Por favor, ingrese un número entero positivo para la cantidad de libros a cargar.")
        
    for i in range(num_libros):
        print(f"\n--- Libro {i + 1} de {num_libros} ---")
        
        while True:
            titulo = input("  Ingrese TITULO: ").strip()
            if not validar_titulo(titulo):
                continue
            
            if obtener_indice_libro(titulo, catalogo) != -1:
                print(f"El título '{titulo}' ya existe. Ingrese otro.")
                continue
            break
            
        while True:
            cantidad_str = input("Ingrese CANTIDAD inicial (>= 0): ").strip()
            if validar_cantidad_entera(cantidad_str):
                cantidad = int(cantidad_str)
                break
                
        nuevo_libro = {"TITULO": titulo, "CANTIDAD": cantidad}
        catalogo.append(nuevo_libro)

    guardar_catalogo(catalogo) # Guardar todos los nuevos libros de una vez
    print(f"\n¡{num_libros} libros agregados exitosamente al catálogo!")


# Ingresar ejemplares (sumar cantidad a existente)
def ingresar_ejemplares(catalogo):
    print("\n=== AUMENTAR STOCK DE LIBRO ===")
    titulo = input("Ingrese TITULO del libro para aumentar su stock: ").strip()
    
    indice = obtener_indice_libro(titulo, catalogo)
    
    if indice == -1:
        print(f"El título '{titulo}' no se encuentra en el catálogo.")
        return
        
    while True:
        aumento_str = input("Ingrese la cantidad de ejemplares a SUMAR: ").strip()
        # Permitimos 0 para la validación, pero pedimos un valor positivo para el aumento
        if validar_cantidad_entera(aumento_str) and int(aumento_str) > 0:
            aumento = int(aumento_str)
            break
        print("Debe ingresar un número entero positivo para aumentar el stock.")
        
    catalogo[indice]["CANTIDAD"] += aumento
    guardar_catalogo(catalogo)
    print(f"\n¡Stock de '{titulo}' actualizado! Nueva CANTIDAD: {catalogo[indice]['CANTIDAD']}")


# Mostrar catálogo
def mostrar_catalogo():
    print("\n=== LISTADO COMPLETO DEL CATÁLOGO ===")
    catalogo = obtener_catalogo()
    
    if not catalogo:
        print("El catálogo está vacío.")
        return
        
    print(f"{'TÍTULO':<40} | {'CANTIDAD':>10}")
    print("-" * 52)
    for libro in catalogo:
        print(f"{libro['TITULO']:<40} | {libro['CANTIDAD']:>10}")
    print("----------------------------------------------------\n")


# Consultar disponibilidad
def consultar_disponibilidad():
    print("\n=== CONSULTAR DISPONIBILIDAD ===")
    catalogo = obtener_catalogo()
    titulo = input("Ingrese TITULO del libro a consultar: ").strip()

    indice = obtener_indice_libro(titulo, catalogo)

    if indice == -1:
        print(f"ERROR: El título '{titulo}' no se encuentra en el catálogo.")
        return
    
    cantidad = catalogo[indice]["CANTIDAD"]
    print(f"\nEl libro '{catalogo[indice]['TITULO']}' tiene {cantidad} ejemplares disponibles.")


# Listar agotados
def listar_agotados():
    print("\n=== TÍTULOS AGOTADOS (CANTIDAD == 0) ===")
    catalogo = obtener_catalogo()
    agotados = [libro["TITULO"] for libro in catalogo if libro["CANTIDAD"] == 0]

    if not agotados:
        print("No hay títulos agotados. ¡Stock completo!")
        return

    for titulo in agotados:
        print(f"- {titulo}")
    print("------------------------------------------\n")


# Actualizar ejemplares (Préstamo/Devolución)
def actualizar_ejemplares():
    print("\n=== PRÉSTAMO / DEVOLUCIÓN ===")
    catalogo = obtener_catalogo()
    
    titulo = input("Ingrese TITULO del libro: ").strip()
    indice = obtener_indice_libro(titulo, catalogo)

    if indice == -1:
        print(f"ERROR: El título '{titulo}' no se encuentra en el catálogo.")
        return

    while True:
        operacion = input("¿Es [P]réstamo o [D]evolución? (P/D): ").strip().upper()
        if operacion in ('P', 'D'):
            break
        print("Opción no válida. Ingrese 'P' para Préstamo o 'D' para Devolución.")

    libro = catalogo[indice]
    
    if operacion == 'P':
        if libro["CANTIDAD"] > 0:
            libro["CANTIDAD"] -= 1
            guardar_catalogo(catalogo)
            print(f"\nPréstamo de '{libro['TITULO']}' exitoso. Nuevo stock: {libro['CANTIDAD']}")
        else:
            print(f"\nERROR: No se puede prestar '{libro['TITULO']}'. Stock actual: {libro['CANTIDAD']} (agotado).")
    
    elif operacion == 'D':
        libro["CANTIDAD"] += 1
        guardar_catalogo(catalogo)
        print(f"\nDevolución de '{libro['TITULO']}' exitosa. Nuevo stock: {libro['CANTIDAD']}")


def eliminar_titulo(catalogo):
    """Elimina un producto del catálogo."""
    print("\n=== ELIMINAR TÍTULO ===")
    
    titulo = input("Ingrese TITULO del libro a eliminar: ").strip()
    indice = obtener_indice_libro(titulo, catalogo)

    if indice == -1:
        print(f"ERROR: El título '{titulo}' no se encuentra en el catálogo.")
        return

    del catalogo[indice]
    guardar_catalogo(catalogo)
    print(f"\nEl título '{titulo}' fue eliminado correctamente.")


# MENÚ PRINCIPAL

def mostrar_menu():
    """Muestra el menú interactivo y dirige las opciones."""
    catalogo = obtener_catalogo()
    
    while True:
        print("\n" + "="*30)
        print("====== MENÚ DE LA BIBLIOTECA ======")
        print("1. Ingresar Títulos")
        print("2. Ingresar Ejemplares")
        print("3. Mostrar Catálogo")
        print("4. Consultar Disponibilidad")
        print("5. Listar Agotados")
        print("6. Agregar Título ")
        print("7. Actualizar Ejemplares")
        print("8. Eliminar Título")
        print("9. Salir")
        print("="*30)
        
        opcion = input("Ingrese opción: ").strip()

        match opcion:
            case "1":
                ingresar_multiples_titulos()
            case "2":
                ingresar_ejemplares(catalogo)
            case "3":
                mostrar_catalogo()
            case "4":
                consultar_disponibilidad()
            case "5":
                listar_agotados()
            case "6":
                agregar_titulo(catalogo)
            case "7":
                actualizar_ejemplares()
            case "8":
                eliminar_titulo(catalogo)
            case "9":
                print("Saliendo... ¡Gracias por usar la aplicación!")
                break
            case _:
                print("ERROR: La opción seleccionada no es válida.")

if __name__ == "__main__":
    mostrar_menu()