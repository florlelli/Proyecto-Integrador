def generar_informe():
    print("Función generar_informe llamada.")

def menu_informes():
    while True:
        print("\nMenú Informes:")
        print("1. Generar Informe")
        print("2. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            generar_informe()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
