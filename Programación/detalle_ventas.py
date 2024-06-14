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
    print("Función modificar_detalle_venta llamada.")

def a_definir():
    print("Función llamada.")

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
            a_definir()
        elif opcion == "4":
            a_definir()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")