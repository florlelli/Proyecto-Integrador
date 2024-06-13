import baseDeDatos

def menu_consultas():
    while True:
        print("\nMenú ventas:")
        print("1. Consulta 1")
        print("2. A definir.")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("consulta")
        elif opcion == "2":
            print("consulta")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
