import baseDeDatos

def agregar_supervisor():
    nombre = input("Ingrese el nombre: ")  
    apellido = input("Ingrese el apellido: ")
    célula = input("Ingrese la célula: ")

    query = "INSERT INTO supervisor (Nombre, Apellido, Célula) VALUES (%s, %s, %s)" 
    values = (nombre, apellido, célula) 
    
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit() 
    print("Supervisor registrado.")
    print(values)

def mostrar_supervisor():
    query = "SELECT * FROM supervisor"
    baseDeDatos.cursor.execute(query)
    supervisor = baseDeDatos.cursor.fetchall()
    
    for supervisor in supervisor:
        print(supervisor)


def modificar_supervisor():
    id = input("Ingrese el id del supervisor: ")
    print("Ingrese qué desea cambiar: ")
    print("Nombre - Apellido - Célula")
    columna = input("Ingrese qué desea cambiar: ")
    cambio = input("Ingrese el cambio: ")
    
    columnas_permitidas = ["Nombre", "Apellido", "Célula"]
    if columna not in columnas_permitidas:
        print("La columna ingresada no es válida.")
        return
    
    query = "UPDATE supervisor SET {} = %s WHERE idSupervisor = %s".format(columna) 
    values = (cambio, id)
 
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit()

def eliminar_supervisor():
    id = int(input("Ingrese el id del supervisor: "))
    query = "DELETE FROM supervisor WHERE idSupervisor = %s"
    values = (id,)

    baseDeDatos.cursor.execute(query,values)
    baseDeDatos.conn.commit()

def menu_supervisor():
    while True:
        print("\nMenú supervisor:")
        print("1. Agregar supervisor.") #CREATE crear
        print("2. Mostrar supervisor.") #READ leer o mostrar
        print("3. Modificar supervisor.") #UPDATE actualizar o modificar
        print("4. Eliminar supervisor.") #DELETE eliminar
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_supervisor()
        elif opcion == "2":
            mostrar_supervisor()
        elif opcion == "3":
            modificar_supervisor()
        elif opcion == "4":
            eliminar_supervisor()
        else:
            print("Opción no válida. Intente de nuevo.")
