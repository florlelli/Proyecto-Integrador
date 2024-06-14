import baseDeDatos

def agregar_detalle_ventas():
    id_venta = input("Ingrese el id_venta: ")  
    id_producto = input("Ingrese el id_producto: ")
    Precio = input("Ingrese el Precio: ")
    Cantidad = input("Ingrese la cantidad: ")
    descuento = input("Ingrese el descuento: ")
    descuento = descuento or None 

    query = "INSERT INTO detalle_ventas (Ventas_idVentas, Productos_idProductos, Precio, Cantidad, Descuento) VALUES (%s, %s, %s, %s, %s)" 
    values = (id_venta, id_producto, Precio, Cantidad, descuento) 
    
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit() 
    print("detalle_ventas registrado.")
    print(values)

def mostrar_detalle_ventas():
    query = "SELECT * FROM detalle_ventas"
    baseDeDatos.cursor.execute(query)
    detalle_ventas = baseDeDatos.cursor.fetchall()
    
    for detalle_ventas in detalle_ventas:
        print(detalle_ventas)


def modificar_detalle_venta():
    id = input("Ingrese el id de la venta: ")
    print("Ingrese qué desea cambiar: ")
    print("Productos_idProductos, Precio, Cantidad, Descuento")
    columna = input("Ingrese qué desea cambiar: ")
    cambio = input("Ingrese el cambio: ")
    
    columnas_permitidas = ["Productos_idProductos", "Precio", "Cantidad", "Descuento"]
    if columna not in columnas_permitidas: 
        print("La columna ingresada no es válida.")
        return
    
    query = "UPDATE detalle_ventas SET {} = %s WHERE Ventas_idVentas = %s".format(columna)
    values = (cambio, id)
 
    baseDeDatos.cursor.execute(query, values) 
    baseDeDatos.conn.commit()

def eliminar_detalle_venta():
    id = int(input("Ingrese el id de la venta: "))
    query = "DELETE FROM detalle_ventas WHERE Ventas_idVentas = %s"
    values = (id,)

    baseDeDatos.cursor.execute(query,values)
    baseDeDatos.conn.commit()

def menu_detalle_ventas():
    while True:
        print("\nMenú detalle_ventas:")
        print("1. Agregar detalle_venta.") #CREATE crear
        print("2. Mostrar detalle_ventas.") #READ leer o mostrar
        print("3. Modificar detalle_venta.") #UPDATE actualizar o modificar
        print("4. Eliminar detalle_venta.") #DELETE eliminar
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_detalle_ventas()
        elif opcion == "2":
            mostrar_detalle_ventas()
        elif opcion == "3":
            modificar_detalle_venta()
        elif opcion == "4":
            eliminar_detalle_venta()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")