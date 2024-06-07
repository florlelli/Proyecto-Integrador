def agregar_empleado():
    print("Función agregar_empleado llamada.")

def mostrar_empleados():
    print("Función mostrar_empleados llamada.")

def modificar_empleado():
    print("Función modificar_empleado llamada.")

def eliminar_empleado():
    print("Función eliminar_empleado llamada.")

def menu_empleados():
    while True:
        print("\nMenú Empleados:")
        print("1. Agregar Empleado")
        print("2. Mostrar Empleados")
        print("3. Modificar Empleado")
        print("4. Eliminar Empleado")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            mostrar_empleados()
        elif opcion == "3":
            modificar_empleado()
        elif opcion == "4":
            eliminar_empleado()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

