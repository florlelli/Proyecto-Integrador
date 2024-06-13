import baseDeDatos

def mostrar_empleados():
    query = "SELECT * FROM empleado"
    baseDeDatos.cursor.execute(query)
    empleado = baseDeDatos.cursor.fetchall()
    
    for empleado in empleado:
        print(empleado)


def modificar_empleado():
    print("Función modificar_empleado llamada.")

def a_definir():
    print("Función llamada.")

def menu_empleados():
    while True:
        print("\nMenú empleados:")
        print("1. Mostrar empleados.")
        print("2. A definir.")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_empleados()
        elif opcion == "2":
            a_definir()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

