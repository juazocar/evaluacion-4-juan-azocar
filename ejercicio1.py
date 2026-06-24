def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            print("Opción inválida. Debe ingresar un número entre 1 y 6.")
        except ValueError:
            print("Error. Debe ingresar un número entero.")


def validar_titulo(titulo):
    return titulo.strip() != ""


def validar_copias(copias):
    return copias >= 0


def validar_prestamo(prestamo):
    return prestamo > 0


def agregar_libro(libros):
    titulo = input("Ingrese el título del libro: ")

    if not validar_titulo(titulo):
        print("El título no puede estar vacío ni contener solo espacios.")
        return

    try:
        copias = int(input("Ingrese la cantidad de copias: "))
    except ValueError:
        print("Las copias deben ser un número entero.")
        return

    if not validar_copias(copias):
        print("Las copias deben ser un número entero mayor o igual que cero.")
        return

    try:
        prestamo = int(input("Ingrese el período de préstamo en días: "))
    except ValueError:
        print("El período de préstamo debe ser un número entero.")
        return

    if not validar_prestamo(prestamo):
        print("El período de préstamo debe ser mayor que cero.")
        return

    libro = {
        "titulo": titulo,
        "copias": copias,
        "prestamo": prestamo,
        "disponible": False
    }

    libros.append(libro)
    print("Libro agregado correctamente.")


def buscar_libro(libros, titulo):
    for i in range(len(libros)):
        if libros[i]["titulo"] == titulo:
            return i
    return -1


def mostrar_datos_libro(libro, posicion):
    print(f"\nLibro encontrado en la posición {posicion}")
    print(f"Título: {libro['titulo']}")
    print(f"Copias: {libro['copias']}")
    print(f"Préstamo: {libro['prestamo']}")
    print(f"Disponible: {libro['disponible']}")


def eliminar_libro(libros):
    titulo = input("Ingrese el título del libro que desea eliminar: ")
    posicion = buscar_libro(libros, titulo)

    if posicion == -1:
        print(f"El libro '{titulo}' no se encuentra registrado.")
    else:
        libros.pop(posicion)
        print("Libro eliminado correctamente.")


def actualizar_disponibilidad(libros):
    for libro in libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False

    print("Disponibilidad actualizada correctamente.")


def mostrar_libros(libros):
    actualizar_disponibilidad(libros)

    if len(libros) == 0:
        print("No existen libros registrados.")
        return

    print("\n=== LISTA DE LIBROS ===")

    for libro in libros:
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"

        print(f"\nTítulo: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado}")
        print("********************************************")


def main():
    libros = []

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_libro(libros)

        elif opcion == 2:
            titulo = input("Ingrese el título del libro a buscar: ")
            posicion = buscar_libro(libros, titulo)

            if posicion == -1:
                print("Libro no encontrado.")
            else:
                mostrar_datos_libro(libros[posicion], posicion)

        elif opcion == 3:
            eliminar_libro(libros)

        elif opcion == 4:
            actualizar_disponibilidad(libros)

        elif opcion == 5:
            mostrar_libros(libros)

        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break


main()
