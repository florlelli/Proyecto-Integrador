def agregar_cliente():
    print("Función agregar_cliente llamada.")

def mostrar_clientes():
    print("Función mostrar_clientes llamada.")

def modificar_cliente():
    print("Función modificar_cliente llamada.")

def eliminar_cliente():
    print("Función eliminar_cliente llamada.")

def menu_clientes():
    while True:
        print("\nMenú Clientes:")
        print("1. Agregar Cliente")
        print("2. Mostrar Clientes")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
