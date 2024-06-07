empleado = { }
def agregarEmpleado():
    id_empleado = input("Ingrese un número identificador de empleado: ")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    puesto = input("Ingrese el puesto: ")
    empleado[id_empleado] = {'nombre': nombre, 'apellido': apellido,'puesto': puesto}

def mostrarEmpleado():
    print("Mostrando todos los empleados:")
    print(empleado)

def modificarEmpleado():
    dato = str(input(("Escriba el id del empleado: ")))
    print(empleado[dato])
    modif = str(input("Escriba qué campo desea modificar: "))
    empleado[dato][f"{modif}"] = input(f"Ingrese el nuevo {modif}: ")
    print(f"Modifiación: {empleado[dato]}")

def eliminarEmpleado():
     eliminar = input("Ingrese el id del empleado: ")
     print(empleado[eliminar])
     del empleado[eliminar]
     print("Eliminado.")
     