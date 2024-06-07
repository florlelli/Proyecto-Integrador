cliente = { }
def agregarCliente():
    id_cliente = input("Ingrese un número identificador de cliente: ")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    email = input("Ingrese el email: ")
    telefono = input("Ingrese el número de teléfono: ")
    cliente[id_cliente] = {'nombre': nombre, 'apellido': apellido, 'email': email, 'telefono': telefono}

def mostrarCliente():
    print("Mostrando todos los clientes:")
    print(cliente)

def modificarCliente():
    dato = str(input(("Escriba el id del cliente: ")))
    print(cliente[dato])
    modif = str(input("Escriba qué campo desea modificar: "))
    cliente[dato][f"{modif}"] = input(f"Ingrese el nuevo {modif}: ")
    print(f"Modifiación: {cliente[dato]}")

def eliminarCliente():
     eliminar = input("Ingrese el id del cliente: ")
     print(cliente[eliminar])
     del cliente[eliminar]
     print("Eliminado.")



    

