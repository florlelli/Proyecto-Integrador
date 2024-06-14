import baseDeDatos
def consulta_uno():
    precio = int(input("Mostrar los productos que tengan un precio mayor a: "))
    query = "SELECT * FROM productos WHERE precio > %s;"
    values = (precio,)
 
    baseDeDatos.cursor.execute(query, values)
    productos = baseDeDatos.cursor.fetchall()
    
    for productos in productos:
        print(productos)







def menu_consultas():
    while True:
        print("\nMenú consultas:")
        print("1. Consulta: Mostrar los productos que tengan un precio mayor a un valor.")
        print("2. Consulta: Mostrar ventas de acuerdo a la fecha.")
        print("3. Consulta: Mostrar clientes que tengan teléfonos registrados.")
        print("4. Consulta: Mostrar empleados por célula.")
        print("5. Consulta: Mostrar clientes que residan en Córdoba.")
        print("6. Consulta: Mostrar datos de empleados y supervisores por célula")
        print("7. Consulta: Mostrar ventas por tipo de pago")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            consulta_uno()
        elif opcion == "2":
            print("consulta")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
