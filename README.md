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

## Descripción del Proyecto

Nuestro proyecto consiste en desarrollar un sistema que gestione el proceso de venta y la satisfacción del cliente. Las principales funcionalidades incluyen:

- Registro de clientes.
- Registro de productos.
- Gestión de ventas.
- Evaluación de la satisfacción del cliente.
- Gestión de empleados.

## Análisis y Diseño del Proyecto

### Menú Principal (Pseudocódigo)

```pseudocode
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
