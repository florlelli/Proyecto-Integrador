import clientes, ventas, empleados, productos, informes

def menu():
    print("1. Gestionar clientes. ")
    print("2. Gestionar empleados.")
    print("3. Gestionar productos.")
    print("4. Gestionar ventas.")
    print("5. Generar informes.")
    print("6. Salir.")

while True:
    menu()
    opcion = int(input("Escriba su opción: "))
    if opcion == 1:
         clientes.menu_clientes()
    elif opcion == 2:
         empleados.menu_empleados()
    elif opcion == 3:
         productos.menu_productos()
    elif opcion == 4:
         ventas.menu_ventas()
    elif opcion == 5:
         informes.menu_informes()    
    elif opcion == 6:
        break
    else:
         print("Opción no válida. Intente de nuevo.")