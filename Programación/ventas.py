def registrar_venta():
    print("Función registrar_venta llamada.")

def mostrar_ventas():
    print("Función mostrar_ventas llamada.")

def modificar_venta():
    print("Función modificar_venta llamada.")

def eliminar_venta():
    print("Función eliminar_venta llamada.")

def menu_ventas():
    while True:
        print("\nMenú Ventas:")
        print("1. Registrar Venta")
        print("2. Mostrar Ventas")
        print("3. Modificar Venta")
        print("4. Eliminar Venta")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            mostrar_ventas()
        elif opcion == "3":
            modificar_venta()
        elif opcion == "4":
            eliminar_venta()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
