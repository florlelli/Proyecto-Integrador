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

def menu_empleados():
    while True:
        print("\nMenú empleados:")
        print("1. Agregar empleado.") #CREATE crear
        print("2. Mostrar empleados.") #READ leer o mostrar
        print("3. Modificar empleado.") #UPDATE actualizar o modificar
        print("4. Eliminar empleado.") #DELETE eliminar
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            mostrar_empleados()
        elif opcion == "3":
            modificar_empleado()
        elif opcion == "4":
            eliminar_empleado()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

