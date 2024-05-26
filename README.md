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
## Análisis: 
El proyecto se basa en un sistema de gestión de ventas. Se podrá almacenar información sobre ventas, clientes, productos y empleados.
Las principales funcionalidades son las siguientes:
- Administrar inventario: Se podrá hacer una gestión sobre el inventario al recopilar información sobre los productos. Guardará su código de producto, nombre, estado de stock, precio.
- Gestionar ventas: Cada venta se registrará y se podrá hacer un relevamiento con la información administrada para otras funcionalidades. Guardará código de venta, fecha, monto final.
- Registrar clientes: Guardará nombre, apellido, dni, teléfono, dirección y correo electrónico.
- Registrar empleados: Guardará código de empleado, nombre, apellido, dni.
- Satisfacción del cliente: En base a la venta y el cliente guardará un puntaje al rendimiento del empleado para hacer un seguimiento de su desempeño.



```pseudocode
### Menú Principal (Pseudocódigo) - 

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




