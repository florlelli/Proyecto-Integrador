def agregar_producto():
    print("Función agregar_producto llamada.")

def mostrar_productos():
    print("Función mostrar_productos llamada.")

def modificar_producto():
    print("Función modificar_producto llamada.")

def eliminar_producto():
    print("Función eliminar_producto llamada.")

def menu_productos():
    while True:
        print("\nMenú Productos:")
        print("1. Agregar Producto")
        print("2. Mostrar Productos")
        print("3. Modificar Producto")
        print("4. Eliminar Producto")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
