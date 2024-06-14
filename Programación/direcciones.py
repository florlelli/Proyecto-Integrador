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


def modificar_direcciones():
    print("Función modificar_direcciones llamada.")

def a_definir():
    print("Función llamada.")

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
            a_definir()
        elif opcion == "4":
            a_definir()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
