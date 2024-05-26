# Proyecto de Introducción a la Programación

## Integrantes del Grupo

- **Nombre:** Brenda Tamara 
  - **Apellido:** Amaya
  - **DNI:** 41846601
  - **Correo Electrónico:** brendaamaya9@gmail.com 
  - **GitHub:** [AmayaBrendaTamara](https://github.com/amayabren)

- **Nombre:** María Florencia
  - **Apellido:** Gimenez
  - **DNI:** 33029489
  - **Correo Electrónico:** floxi87@gmail.com
  - **GitHub:** [MaríaFlorenciaGimenez](https://github.com/Floxi87)

- **Nombre:** José Augusto
  - **Apellido:** Lazarte
  - **DNI:** 28763838
  - **Correo Electrónico:** augusto.lazarte81@gmail.com
  - **GitHub:** [JoséAugustoLazarte](https://github.com/AugustoLaz)

- **Nombre:** Florencia
  - **Apellido:** Lelli
  - **DNI:** 40574799
  - **Correo Electrónico:** florlelli6@gmail.com
  - **GitHub:** [FlorenciaLelli](https://github.com/florlelli)

- **Nombre:** María Cecilia
  - **Apellido:** Linares
  - **DNI:** 33171021
  - **Correo Electrónico:** mcecilialinares@gmail.com
  - **GitHub:** [MaríaCeciliaLinares](https://github.com/cecilinares)

- **Nombre:** Stella Maris
  - **Apellido:** Tita Mascarello
  - **DNI:** 39623753
  - **Correo Electrónico:** stella.tita@mi.unc.edu.ar
  - **GitHub:** [StellaMarisTitaMascarello](https://github.com/StellaTita)
  - 
___________________________________________________________________________________
## Descripción del Proyecto stella

Nuestro proyecto consiste en desarrollar un sistema que gestione el proceso de venta y la satisfacción del cliente. Las principales funcionalidades incluyen:

- Registro de clientes.
- Registro de productos.
- Gestión de ventas.
- Evaluación de la satisfacción del cliente.
- Gestión de empleados.

## Análisis y Diseño del Proyecto

### Menú Principal (Pseudocódigo)
_____________________________________________________ brenda

Análisis: 
El proyecto se basa en un sistema de gestión de ventas. Se podrá almacenar información sobre ventas, clientes, productos y empleados.
Las principales funcionalidades son las siguientes:
- Administrar inventario: Se podrá hacer una gestión sobre el inventario al recopilar información sobre los productos. Guardará su código de producto, nombre, estado de stock, precio.
- Gestionar ventas: Cada venta se registrará y se podrá hacer un relevamiento con la información administrada para otras funcionalidades. Guardará código de venta, fecha, monto final.
- Registrar clientes: Guardará nombre, apellido, dni, teléfono, dirección y correo electrónico.
- Registrar empleados: Guardará código de empleado, nombre, apellido, dni.
- Satisfacción del cliente: En base a la venta y el cliente guardará un puntaje al rendimiento del empleado para hacer un seguimiento de su desempeño.



```pseudocode
________________________________________________________Stella
INICIO
    MIENTRAS verdadero
        MOSTRAR "Bienvenido al Sistema de Ventas"
        MOSTRAR "1. Registrar Cliente"
        MOSTRAR "2. Registrar Producto"
        MOSTRAR "3. Registrar Venta"
        MOSTRAR "4. Evaluar Satisfacción del Cliente"
        MOSTRAR "5. Registrar Empleado"
        MOSTRAR "6. Salir"
        LEER opción
        
        SEGÚN opción HACER
            CASO 1:
                LLAMAR RegistrarCliente()
            CASO 2:
                LLAMAR RegistrarProducto()
            CASO 3:
                LLAMAR RegistrarVenta()
            CASO 4:
                LLAMAR EvaluarSatisfaccion()
            CASO 5:
                LLAMAR RegistrarEmpleado()
            CASO 6:
                MOSTRAR "Gracias por usar el sistema. ¡Adiós!"
                SALIR
            DEFECTO:
                MOSTRAR "Opción no válida. Intente de nuevo."
        FIN SEGÚN
    FIN MIENTRAS
FIN

____________________________________________________________________
### Menú Principal (Pseudocódigo) - Florencia Lelli

```pseudocode
Algoritmo AnalisisDeVentas
	//Programa Principal
	Escribir "Bienvenido al Sistema de Análisis de Ventas de un Comercio"
	Mientras Verdadero Hacer
		Escribir "Menú Principal:"
		Escribir "1. Cargar Datos de Ventas"
		Escribir "2. Generar Informes"
		Escribir "3. Visualizar Datos"
		Escribir "4. Salir"
		Leer opción_usuario
		Si opción_usuario == 1 Entonces
			// Llamar función cargar_datos_ventas
			Escribir "Cargando datos de ventas..."
		SiNo
			Si opción_usuario == 2  Entonces
				// Llamar función generar_informes
				Escribir "Generando informes..."
			SiNo
				Si opción_usuario == 3 Entonces
					// Llamar función visualizar_datos
					Escribir "Visualizando datos..."
				SiNo
					Si opción_usuario == 4 Entonces
						Escribir "Gracias por usar el sistema"
					SiNo
						Escribir "Opción no válida. Intente de nuevo."
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Mientras
FinAlgoritmo


__________________________________________________________
// Mostrar menú de opciones -florencia gimenez
Escribir "Bienvenido al Sistema de Análisis de Ventas 
        Mostrar "Menú del Sistema de Ventas"
        Mostrar "1. Registrar Venta"
        Mostrar "2. Registrar Cliente"
        Mostrar "3. Registrar Empleado"
        Mostrar "4. Calcular Efectividad de Ventas"
        Mostrar "5. Salir"

        // Leer la opción del usuario
        Escribir "Seleccione una opción: "
        Leer opcion

        // Evaluar la opción seleccionada
        Segun opcion Hacer
            Caso 1:
                // Lógica para registrar venta
                ventas <- ventas + 1
                // Aquí puedes agregar la lógica para registrar la venta
            Caso 2:
                // Lógica para registrar cliente
                clientes <- clientes + 1
                // Aquí puedes agregar la lógica para registrar un nuevo cliente
            Caso 3:
                // Lógica para registrar empleado
                empleados <- empleados + 1
                // Aquí puedes agregar la lógica para registrar un nuevo empleado
            Caso 4:
                // Lógica para calcular la efectividad de ventas
                Si ventas > 0 Entonces
                    efectividadVentas <- (ventas / clientes) * 100
                    Mostrar "La efectividad de ventas es: ", efectividadVentas, "%"
                Sino
                    Mostrar "No hay ventas registradas aún."
                FinSi
            Caso 5:
                // Salir del programa
                Mostrar "Saliendo del sistema..."
            De Otro Modo:
                Mostrar "Opción no válida, por favor seleccione una opción del 1 al 5."
        FinSegun
    Hasta Que opcion = 5

FinAlgoritmo

_______________________________________________________________brenda
Algoritmo Menu
	Mientras Verdadero
		Escribir "Bienvenido al menu."
		Escribir "1. Registrar datos"
		Escribir "2. Funcionalidades"
		Escribir "3. Salir"
		Leer opcion
		Si opcion = 1
			Escribir "1. Registrar cliente"
			Escribir "2. Registrar venta"
			Escribir "3. Registrar producto"
			Escribir "4. Registrar empleado"
			Escribir "5. Registrar valoración de venta"
			Escribir  "6. Volver"
			Leer opcion
			Si opcion = 1
				Escribir "Implementando función. Registrando cliente."
			FinSi
			Si opcion = 2
				Escribir "Implementando función. Registrando venta."
			FinSi
			Si opcion = 3
				Escribir "Implementando función. Registrando producto."
			FinSi
			Si opcion = 4
				Escribir "Implementando función. Registrando empleado."
			FinSi
			Si opcion = 5
				Escribir "Implementando función. Registrando valoración de venta."
			FinSi
			Si opcion = 6
				Escribir "Volviendo al menu principal."
			FinSi
		FinSi
		Si opcion = 2
			Escribir "1. Mostrar datos."
			Escribir "2. Evaluar desempeño de empleado."
			Escribir "3. Calcular stock de productos."
			Leer opcion
			Si opcion = 1
				Escribir "Implementando función. Mostrando datos."
			FinSi
			Si opcion = 2
				Escribir "Implementando función. Evaluando desempeño de empleado."
			FinSi
			Si opcion = 3
				Escribir "Implementando función. Calculando stock de productos."
			FinSi
		FinSi
		Si opcion = 3
			Escribir "Break"
		FinSi
	FinMientras
	
FinAlgoritmo


Algoritmo Vendedor
	Definir cantidad_venta, clientes_atendidos, satisfaccion_cliente Como Entero
	Definir efectividad_venta Como Real
	Definir Resultado_satisfacción Como Caracter
	Escribir "Ingrese cantidad de ventas"
	Leer cantidad_venta
	Escribir "Ingrese número de clientes atendidos"
	Leer clientes_atendidos
	efectividad_venta=cantidad_venta/clientes_atendidos
	Escribir "La efectividad de venta del empleado es:", efectividad_venta
	Escribir "Ingrese su satisfacción de 1 a 5"
	Si satisfaccion_cliente>3 Entonces
		Resultado_satisfaccion=Mala
		Leer Mala
	FinSi
	Si satisfaccion_cliente=3 Entonces
		Resultado_satisfaccion=Regular
		Leer Regular
	FinSi
	Si satisfaccion_cliente<3 Entonces
		Resultado_satisfaccion=Buena
		Leer Buena
	FinSi
FinAlgoritmo


