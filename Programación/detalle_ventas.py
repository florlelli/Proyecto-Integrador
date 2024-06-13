import baseDeDatos

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
        print("1. Mostrar detalle_ventas.")
        print("2. A definir.")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_detalle_ventas()
        elif opcion == "2":
            a_definir()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")