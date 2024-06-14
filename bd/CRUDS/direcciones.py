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


