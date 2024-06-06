import clientes

def menu():
    print("1. Cargar datos. ")
    print("2. Mostrar la totalidad de los datos.")
    print("3. Modificar datos.")
    print("4. Eliminar datos.")
    print("2. Generar informes.")
    print("6. Salir.")

def agregar():
    print("1. Clientes.")
    print("2. Empleados. ")
    print("3. Productos.")
    print("4. Ventas.")
    print("5. Satisfacción de cliente.")
    dato = str(input("Escriba el dato que quiere agregar: "))
    if dato.lower() == "1":
        clientes.agregarCliente()
#podemos hacer como en def agregar que imprime todos los datos y después se lo ingresa por número
#o hacer como abajo que no imprime los datos sino que hay que escribir qué es lo que se cambia.
def mostrar():
    dato = str(input("Escriba el dato que quiere mostrar: ")) 
    if dato.lower() == "cliente":   
        clientes.mostrarCliente()  

def modificar():
    dato = str(input("Escriba el dato que quiere modificar: "))
    if dato.lower() == "cliente":   
        clientes.modificarCliente() 

def eliminar():
    dato = str(input("Escriba el dato que quiere eliminar: "))
    if dato.lower() == "cliente":   
        clientes.eliminarCliente() 

def informes():
    print("1. Efectividad de venta.")
    print("2. A definir.")
    dato = str(input("Seleccione el informe: "))
    if dato.lower() == "1":   
        #podemos implementar el algoritmo de gustavo
        print("función correspondiente") 

while True:
    menu()
    opcion_elegida = int(input("Escriba su opción: "))
    if opcion_elegida == 1:
         agregar()
    elif opcion_elegida == 2:
         mostrar()
    elif opcion_elegida == 3:
         modificar()
    elif opcion_elegida == 4:
         eliminar()
    elif opcion_elegida == 5:
         informes()    
    elif opcion_elegida == 6:
        break

