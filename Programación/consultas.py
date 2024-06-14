import baseDeDatos
def consulta_uno():
    precio = int(input("Mostrar los productos que tengan un precio mayor a: "))
    query = "SELECT * FROM productos WHERE precio > %s;"
    values = (precio,)
    baseDeDatos.cursor.execute(query, values)
    productos = baseDeDatos.cursor.fetchall()  
    for productos in productos:
        print(productos)

def consulta_dos(): #las ventas registradas van desde el mes de enero y febrero de este año
    fecha_uno = input("En formato año-mes-día, ingresa la primera fecha: ")
    fecha_dos = input("Ingresa la segunda fecha: ")
    query = "SELECT * FROM ventas WHERE Fecha BETWEEN  %s AND %s;"
    values = fecha_uno, fecha_dos
    baseDeDatos.cursor.execute(query, values)
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas)        

def consulta_tres():
    query = "SELECT * FROM clientes WHERE Teléfono IS NOT NULL;"
    baseDeDatos.cursor.execute(query)
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas)        

def consulta_cuatro():
    célula = input("Ingrese la célula que desa filtrar: ")
    query = "SELECT * FROM empleado WHERE Supervisor_Célula = %s;"
    values = (célula,)
    baseDeDatos.cursor.execute(query, values)
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas)

def consulta_cinco():
    query = "SELECT clientes.idClientes, clientes.Nombre, direcciones.Localidad FROM direcciones INNER JOIN clientes ON direcciones.Clientes_idClientes = clientes.idClientes WHERE direcciones.Localidad  = 'Córdoba';"
    baseDeDatos.cursor.execute(query)    
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas)    

def consulta_seis():
    query = "SELECT empleado.idEmpleado, empleado.Nombre, empleado.Apellido, supervisor.Célula, supervisor.Nombre, supervisor.Apellido FROM supervisor INNER JOIN empleado ON supervisor.Célula = empleado.Supervisor_Célula  ORDER BY supervisor.Célula;"
    baseDeDatos.cursor.execute(query)    
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas) 

def consulta_siete():
    query = "SELECT ventas.idVentas, ventas.Clientes_IdClientes, métodopago.Tipo FROM métodopago INNER JOIN ventas ON métodopago.idMétodoPago = ventas.MétodoPago_idMétodoPago;" 
    baseDeDatos.cursor.execute(query)    
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas) 

def menu_consultas():
    while True:
        print("\nMenú consultas:")
        print("1. Consulta: Mostrar los productos que tengan un precio mayor a un valor ingresado.")
        print("2. Consulta: Mostrar ventas las ventas realizadas entre dos fechas.")
        print("3. Consulta: Mostrar clientes que tengan teléfonos registrados.")
        print("4. Consulta: Mostrar empleados por célula.")
        print("5. Consulta: Mostrar clientes que residan en Córdoba.")
        print("6. Consulta: Mostrar datos de empleados y supervisores por célula")
        print("7. Consulta: Mostrar ventas por tipo de pago")
        print("8. Volver.")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            consulta_uno()
        elif opcion == "2":
            consulta_dos()
        elif opcion == "3":
            consulta_tres()
        elif opcion == "4":
            consulta_cuatro()
        elif opcion == "5":
            consulta_cinco()
        elif opcion == "6":
            consulta_seis()
        elif opcion == "7":
            consulta_siete()
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
