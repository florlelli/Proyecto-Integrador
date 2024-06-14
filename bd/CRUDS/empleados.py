import baseDeDatos

def agregar_empleado():
    nombre = input("Ingrese el nombre: ")  
    apellido = input("Ingrese el apellido: ")
    fecha = input("Digite la fecha de ingreso: ")
    supervisor_celula = input("Ingrese la célula: ")

    query = "INSERT INTO empleado (Nombre, Apellido, Fecha_ingreso, Supervisor_Célula) VALUES (%s, %s, %s, %s)" 
    values = (nombre, apellido, fecha, supervisor_celula) 
    
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit() 
    print("Empleado registrado.")
    print(values)

def mostrar_empleados():
    query = "SELECT * FROM empleado"
    baseDeDatos.cursor.execute(query)
    empleado = baseDeDatos.cursor.fetchall()
    
    for empleado in empleado:
        print(empleado)


def modificar_empleado():
    id = input("Ingrese el id del empleado: ")
    print("Ingrese qué desea cambiar: ")
    print("Nombre - Apellido - Fecha_ingreso - Supervisor_Célula")
    columna = input("Ingrese qué desea cambiar: ")
    cambio = input("Ingrese el cambio: ")
    
    columnas_permitidas = ["Nombre", "Apellido", "Fecha_ingreso", "Supervisor_Célula"]
    if columna not in columnas_permitidas: 
        print("La columna ingresada no es válida.")
        return
    
    query = "UPDATE empleado SET {} = %s WHERE idEmpleado = %s".format(columna)
    values = (cambio, id)
 
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit()

def eliminar_empleado():
    id = int(input("Ingrese el id del empleado: "))
    query = "DELETE FROM empleado WHERE idEmpleado = %s"
    values = (id,)

    baseDeDatos.cursor.execute(query,values)
    baseDeDatos.conn.commit()



