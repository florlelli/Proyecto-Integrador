import baseDeDatos

def mostrar_supervisor():
    query = "SELECT * FROM supervisor"
    baseDeDatos.cursor.execute(query)
    supervisor = baseDeDatos.cursor.fetchall()
    
    for supervisor in supervisor:
        print(supervisor)


def modificar_supervisor():
    print("Función modificar_supervisor llamada.")

def a_definir():
    print("Función llamada.")

def menu_supervisor():
    while True:
        print("\nMenú supervisor:")
        print("1. Mostrar supervisor.")
        print("2. A definir.")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_supervisor()
        elif opcion == "2":
            a_definir()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
