import menus

while True:
    menus.menu_principal()
    opcion = int(input("Escriba su opción: "))
    if opcion == 1:
         menus.menu_clientes()   #cada opcion va a llamar al menu 
    elif opcion == 2:
         menus.menu_empleados()
    elif opcion == 3:
         menus.menu_productos()
    elif opcion == 4:
         menus.menu_ventas()
    elif opcion == 5:
         menus.menu_detalle_ventas()
    elif opcion == 6:
         menus.menu_satisfacción_cliente()
    elif opcion == 7:
         menus.menu_supervisor()
    elif opcion == 8:
         menus.menu_direcciones()
    elif opcion == 9:    
         menus.menu_consultas()     
    elif opcion == 10:
        break
    else:
         print("Opción no válida. Intente de nuevo.")