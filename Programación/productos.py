import baseDeDatos

def mostrar_productos():
    query = "SELECT * FROM productos"
    baseDeDatos.cursor.execute(query)
    productos = baseDeDatos.cursor.fetchall()
    
    for productos in productos:
        print(productos)


def modificar_producto():
    print("Función modificar_producto llamada.")

def a_definir():
    print("Función llamada.")

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
            a_definir()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            a_definir()
        elif opcion == "4":
            a_definir()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")