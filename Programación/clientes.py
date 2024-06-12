import baseDeDatos

def mostrar_clientes():
    query = "SELECT * FROM clientes"
    baseDeDatos.cursor.execute(query)
    lista_clientes = baseDeDatos.cursor.fetchall()
    
    for cliente in lista_clientes:
        print(cliente)


def modificar_cliente():
    print("Función modificar_cliente llamada.")

def a_definir():
    print("Función llamada.")

def menu_clientes():
    while True:
        print("\nMenú Clientes:")
        print("1. Mostrar Clientes.")
        print("2. A definir.")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_clientes()
        elif opcion == "2":
            a_definir()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
