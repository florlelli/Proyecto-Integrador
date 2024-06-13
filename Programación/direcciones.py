import baseDeDatos

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
        print("1. Mostrar direcciones.")
        print("2. A definir.")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_direcciones()
        elif opcion == "2":
            a_definir()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
