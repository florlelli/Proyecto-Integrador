import baseDeDatos

def agregar_venta():
    Fecha = input("Ingrese el Fecha: ")  
    Total = input("Ingrese el Total: ")
    id_empleado = input("Ingrese el id del empleado: ")
    id_cliente = input("Ingrese el id del cliente: ")
    id_métodopago = input("Ingrese el id de método de pago: ")

    query = "INSERT INTO ventas (Fecha, Total, Empleado_idEmpleado, Clientes_idClientes, MétodoPago_idMétodopago) VALUES (%s, %s, %s, %s, %s)" 
    values = (Fecha, Total, id_empleado, id_cliente, id_métodopago) 
    
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit() 
    print("Venta registrada.")
    print(values)

def mostrar_ventas():
    query = "SELECT * FROM ventas"
    baseDeDatos.cursor.execute(query)
    ventas = baseDeDatos.cursor.fetchall()
    
    for ventas in ventas:
        print(ventas)


def modificar_venta(): 
    id = input("Ingrese el id de la venta: ")
    print("Ingrese qué desea cambiar: ")
    print("Fecha - Total - Empleado_idEmpleado - Clientes_idClientes - MétodoPago_idMétodoPago")
    columna = input("Ingrese qué desea cambiar: ")
    cambio = input("Ingrese el cambio: ")
    
    columnas_permitidas = ["Fecha", "Total", "Empleado_idEmpleado", "Clientes_idClientes", "MétodoPago_idMétodoPago"]
    if columna not in columnas_permitidas: 
        print("La columna ingresada no es válida.")
        return
    
    query = "UPDATE ventas SET {} = %s WHERE idVentas = %s".format(columna)
    values = (cambio, id)
 
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit()

def eliminar_venta():
    id = int(input("Ingrese el id la venta: "))
    query = "DELETE FROM ventas WHERE idVentas = %s"
    values = (id,)

    baseDeDatos.cursor.execute(query,values)
    baseDeDatos.conn.commit()


