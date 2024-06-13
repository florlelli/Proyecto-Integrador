import baseDeDatos

def mostrar_ventas():
    query = "SELECT * FROM ventas"
    baseDeDatos.cursor.execute(query)
    ventas = baseDeDatos.cursor.fetchall()
    
    for ventas in ventas:
        print(ventas)


def modificar_venta():
    print("Función modificar_venta llamada.")

def a_definir():
    print("Función llamada.")

def menu_ventas():
    while True:
        print("\nMenú ventas:")
        print("1. Mostrar ventas.")
        print("2. A definir.")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_ventas()
        elif opcion == "2":
            a_definir()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
