import baseDeDatos

def mostrar_satisfacción_cliente():
    query = "SELECT * FROM satisfacción_cliente"
    baseDeDatos.cursor.execute(query)
    satisfacción_cliente = baseDeDatos.cursor.fetchall()
    
    for satisfacción_cliente in satisfacción_cliente:
        print(satisfacción_cliente)


def modificar_satisfacción_cliente():
    print("Función modificar_satisfacción_cliente llamada.")

def a_definir():
    print("Función llamada.")

def menu_satisfacción_cliente():
    while True:
        print("\nMenú satisfacción_cliente:")
        print("1. Mostrar satisfacción_cliente.")
        print("2. A definir.")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_satisfacción_cliente()
        elif opcion == "2":
            a_definir()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")