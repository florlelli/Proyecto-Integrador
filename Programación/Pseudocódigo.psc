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
