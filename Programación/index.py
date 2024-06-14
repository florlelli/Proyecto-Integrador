import clientes, ventas, empleados, productos, detalle_ventas, satisfacción_cliente, supervisor, direcciones, consultas
#como el profe julian dijo que no todas las tablas necesitaban tener un crud decidimos no hacer uno para la tabla "MétodoPago" por su simplicidad. 
def menu():
    print("1. Gestionar clientes. ")
    print("2. Gestionar empleados.")
    print("3. Gestionar productos.")
    print("4. Gestionar ventas.")
    print("5. Gestionar detalle de ventas.")
    print("6. Gestionar satisfacción de cliente.")
    print("7. Gestionar supervisor")
    print("8. Gestionar direcciones")
    print("9. Hacer consultas.")
    print("10. Salir.")

while True:
    menu()
    opcion = int(input("Escriba su opción: "))
    if opcion == 1:
         clientes.menu_clientes()   #cada opcion va a llamar a la tabla correspondinete con el nombre del archivo y va a llamar la función del menu de la misma
    elif opcion == 2:
         empleados.menu_empleados()
    elif opcion == 3:
         productos.menu_productos()
    elif opcion == 4:
         ventas.menu_ventas()
    elif opcion == 5:
         detalle_ventas.menu_detalle_ventas()
    elif opcion == 6:
         satisfacción_cliente.menu_satisfacción_cliente()
    elif opcion == 7:
         supervisor.menu_supervisor()
    elif opcion == 8:
         direcciones.menu_direcciones()
    elif opcion == 9:    
         consultas.menu_consultas()     
    elif opcion == 10:
        break
    else:
         print("Opción no válida. Intente de nuevo.")