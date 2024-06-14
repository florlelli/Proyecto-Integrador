# Proyecto

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

## Descripción del proyecto
Nuestro proyecto consiste en desarrollar un sistema que gestione el proceso de venta y la satisfacción del cliente. Las principales funcionalidades incluyen:

- Registro de clientes.
- Registro de productos.
- Gestión de ventas.
- Evaluación de la satisfacción del cliente.
- Gestión de empleados.
- Gestión de detalle de venta.

## Detalle de la Aplicación Modularizada
La aplicación se ha estructurado de manera modular para facilitar su mantenimiento y escalabilidad. A continuación, se detalla la estructura de archivos y su contenido:

1. **index.py**:
    - **Descripción**: Este es el archivo principal de la aplicación. Contiene el menú principal desde el cual se puede acceder a la gestión de clientes, empleados, productos, ventas y la generación de informes.
    - **Funciones**: Implementa el menú principal y llama a los submenús correspondientes.

2. **cliente.py**:
    - **Descripción**: Este archivo contiene las funciones CRUD (Crear, Leer, Actualizar, Eliminar) para la entidad de Cliente.
    - **Funciones**: `agregar_cliente`, `mostrar_clientes`, `modificar_cliente`, `eliminar_cliente`, `menu_clientes`.
    - **Uso**: Gestiona la información de los clientes del comercio.

3. **empleado.py**:
    - **Descripción**: Este archivo contiene las funciones CRUD para la entidad de Empleado.
    - **Funciones**: `agregar_empleado`, `mostrar_empleados`, `modificar_empleado`, `eliminar_empleado`, `menu_empleados`.
    - **Uso**: Gestiona la información de los empleados del comercio.

4. **producto.py**:
    - **Descripción**: Este archivo contiene las funciones CRUD para la entidad de Producto.
    - **Funciones**: `agregar_producto`, `mostrar_productos`, `modificar_producto`, `eliminar_producto`, `menu_productos`.
    - **Uso**: Gestiona la información de los productos disponibles en el comercio.

5. **venta.py**:
    - **Descripción**: Este archivo contiene las funciones CRUD para la entidad de Venta.
    - **Funciones**: `registrar_venta`, `mostrar_ventas`, `modificar_venta`, `eliminar_venta`, `menu_ventas`.
    - **Uso**: Gestiona la información de las ventas realizadas en el comercio.

6. **informes.py**:
    - **Descripción**: Este archivo contiene la función para la generación de informes.
    - **Funciones**: `generar_informe`, `menu_informes`.
    - **Uso**: Permite la generación de informes basados en los datos de ventas.

## Uso de la Aplicación
Para ejecutar la aplicación, usa el siguiente comando en la terminal:

**python index.py**

Sigue las instrucciones en pantalla para navegar por el menú principal y gestionar las diferentes entidades.

## Base de Datos
Diseñamos una base de datos MySQL siguiendo el modelo entidad-relación (DER) y convertimos este modelo en un modelo relacional. La base de datos contiene tablas para cada entidad con relaciones bien definidas. También hemos incluido scripts SQL para crear la estructura de la base de datos, insertar datos iniciales y realizar consultas.

## Navegación del Repositorio
El repositorio está organizado de la siguiente manera:

1. **Carpeta aplicacion**: Contiene todos los archivos fuente .py.

   - **index.py**: Archivo principal de la aplicación.
   - **cliente.py**: Funciones CRUD para la entidad Cliente.
   - **empleado.py**: Funciones CRUD para la entidad Empleado.
   - **producto.py**: Funciones CRUD para la entidad Producto.
   - **venta.py**: Funciones CRUD para la entidad Venta.
   - **informes.py**: Generación de informes.

2. **Carpeta bd**: Contiene los scripts SQL para la base de datos y los diagramas de entidad-relación.

   - **estructura.sql**: Script para crear la estructura de la base de datos.
   - **datos_iniciales.sql**: Script para insertar datos iniciales en la base de datos.

3. **Archivo README.md**: Contiene la descripción del proyecto, instrucciones de uso y detalles de instalación.



