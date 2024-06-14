import baseDeDatos

def agregar_satisfacción_cliente():
    Puntos = input("Ingrese el puntaje de la venta: ")  
    idClientes = input("Ingrese el id del cliente: ")
    idEmpleado = input("Ingrese el id del empleado: ")
    idVentas = input("Ingrese el id de la venta: ")

    query = "INSERT INTO satisfacción_cliente (Puntos, Clientes_idClientes, Empleado_idEmpleado, Ventas_idVentas) VALUES (%s, %s, %s, %s)" 
    values = (Puntos, idClientes, idEmpleado, idVentas) 
    
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit() 
    print("Satisfacción_cliente registrada.")
    print(values)

def mostrar_satisfacción_clientes():
    query = "SELECT * FROM satisfacción_cliente"
    baseDeDatos.cursor.execute(query)
    satisfacción_cliente = baseDeDatos.cursor.fetchall()
    
    for satisfacción_cliente in satisfacción_cliente:
        print(satisfacción_cliente)


def modificar_satisfacción_cliente():
    print("Función modificar_satisfacción_cliente llamada.")

def a_definir():
    print("Función llamada.")

def menu_satisfacción_cliente():
    while True:
        print("\nMenú satisfacción_cliente:")
        print("1. Agregar satisfacción_cliente.") #CREATE crear
        print("2. Mostrar satisfacción_clientes.") #READ leer o mostrar
        print("3. Modificar satisfacción_cliente.") #UPDATE actualizar o modificar
        print("4. Eliminar satisfacción_cliente.") #DELETE eliminar
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_satisfacción_cliente()
        elif opcion == "2":
            mostrar_satisfacción_clientes()
        elif opcion == "3":
            a_definir()
        elif opcion == "4":
            a_definir()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")