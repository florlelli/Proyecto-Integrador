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
        print("1. Mostrar productos.")
        print("2. A definir.")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            a_definir()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")