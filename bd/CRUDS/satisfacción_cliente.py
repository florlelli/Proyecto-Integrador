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
    id = input("Ingrese el id de satisfacción_cliente: ")
    print("Ingrese qué desea cambiar: ")
    print("Puntos - Clientes_idClientes - Empleado_idEmpleado - Ventas_idVentas")
    columna = input("Ingrese qué desea cambiar: ")
    cambio = input("Ingrese el cambio: ")
    
    columnas_permitidas = ["Puntos", "Clientes_idClientes", "Empleado_idEmpleado", "Ventas_idVentas"]
    if columna not in columnas_permitidas: 
        print("La columna ingresada no es válida.")
        return
    
    query = "UPDATE satisfacción_cliente SET {} = %s WHERE idSatisfacción_Cliente = %s".format(columna)
    values = (cambio, id)
 
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit()

def eliminar_satisfacción_cliente():
    id = int(input("Ingrese el id satisfacción_cliente: "))
    query = "DELETE FROM satisfacción_cliente WHERE idSatisfacción_Cliente = %s"
    values = (id,)

    baseDeDatos.cursor.execute(query,values)
    baseDeDatos.conn.commit()

