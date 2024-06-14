import baseDeDatos

def agregar_producto():
    nombre = input("Ingrese el nombre: ")  
    Descripción = input("Ingrese la descripción (opcional): ")
    Precio = input("Ingrese el precio: ")

    Descripción = Descripción or None

    query = "INSERT INTO productos (Nombre, Descripción, Precio) VALUES (%s, %s, %s)" 
    values = (nombre, Descripción, Precio) 
    
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit() 
    print("Producto registrado.")
    print(values)

def mostrar_productos():
    query = "SELECT * FROM productos"
    baseDeDatos.cursor.execute(query)
    productos = baseDeDatos.cursor.fetchall()
    
    for productos in productos:
        print(productos)


def modificar_producto():
    id = input("Ingrese el id del producto: ")
    print("Ingrese qué desea cambiar: ")
    print("Nombre - Descripción - Precio")
    columna = input("Ingrese qué desea cambiar: ")
    cambio = input("Ingrese el cambio: ")
    
    columnas_permitidas = ["Nombre", "Descripción", "Precio"]
    if columna not in columnas_permitidas: 
        print("La columna ingresada no es válida.")
        return
    
    query = "UPDATE productos SET {} = %s WHERE idProductos = %s".format(columna)
    values = (cambio, id)
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit()

def eliminar_producto():
    id = int(input("Ingrese el id del producto: "))
    query = "DELETE FROM productos WHERE idProductos = %s"
    values = (id,)

    baseDeDatos.cursor.execute(query,values)
    baseDeDatos.conn.commit()

def menu_productos():
    while True:
        print("\nMenú productos:")
        print("1. Agregar producto.") #CREATE crear
        print("2. Mostrar productos.") #READ leer o mostrar
        print("3. Modificar producto.") #UPDATE actualizar o modificar
        print("4. Eliminar producto.") #DELETE eliminar
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")