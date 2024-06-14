import baseDeDatos

def agregar_direccion():
    Localidad = input("Ingrese la localidad: ")  
    Código_postal = input("Ingrese el código postal: ")
    Calle = input("Ingrese la calle: ")
    id_cliente = input("Ingrese el id del cliente: ")

    query = "INSERT INTO direcciones (Localidad, Código_postal, Calle, Clientes_idClientes) VALUES (%s, %s, %s, %s)" 
    values = (Localidad, Código_postal, Calle, id_cliente) 
    
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit() 
    print("Dirección registrado.")
    print(values)

def mostrar_direcciones():
    query = "SELECT * FROM direcciones"
    baseDeDatos.cursor.execute(query)
    direcciones = baseDeDatos.cursor.fetchall()
    
    for direcciones in direcciones:
        print(direcciones)


def modificar_direccion():
    id = input("Ingrese el id de la dirección: ")
    print("Ingrese qué desea cambiar: ")
    print("Localidad - Código_Postal - Calle - Clientes_idClientes")
    columna = input("Ingrese qué desea cambiar: ")
    cambio = input("Ingrese el cambio: ")
    
    columnas_permitidas = ["Localidad", "Código_Postal", "Calle", "Clientes_idClientes"]
    if columna not in columnas_permitidas: 
        print("La columna ingresada no es válida.")
        return
    
    query = "UPDATE direcciones SET {} = %s WHERE idDirecciones = %s".format(columna)
    values = (cambio, id)
 
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit()

def eliminar_direccion():
    id = int(input("Ingrese el id de la dirección: "))
    query = "DELETE FROM direcciones WHERE idDirecciones = %s"
    values = (id,)

    baseDeDatos.cursor.execute(query,values)
    baseDeDatos.conn.commit()

def menu_direcciones():
    while True:
        print("\nMenú direcciones:")
        print("1. Agregar dirección.") #CREATE crear
        print("2. Mostrar direcciones.") #READ leer o mostrar
        print("3. Modificar dirección.") #UPDATE actualizar o modificar
        print("4. Eliminar dirección.") #DELETE eliminar
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_direccion()
        elif opcion == "2":
            mostrar_direcciones()
        elif opcion == "3":
            modificar_direccion()
        elif opcion == "4":
            eliminar_direccion()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
