#1. Una sola tabla. (mostrando todos los datos).
#Muestra todos los productos.
SELECT * FROM productos;

#2. Una sola tabla (mostrando algunas columnas).
#Muestra los nombres de los empleados
SELECT Nombre FROM empleado;

#3. Una sola tabla con where. 
#Mostrar todos los productos Samsung
SELECT * FROM Productos
WHERE Nombre LIKE '%samsung%';

#4. Una sola tabla con where utilizando between.
#Mostrar los empleados con fecha de ingreso superior a un año
SELECT * FROM empleado
WHERE Fecha_ingreso BETWEEN '20-01-01' AND '23-06-12'
ORDER BY Fecha_ingreso; 

#5. Una sola tabla con where utilizando limit.
#Mostrar las ventas con un total mayor a 200mil
SELECT * FROM ventas 
WHERE total > 200000
LIMIT 3;

#6. Más de una tabla con inner join:
#Muestra las ventas con más de un producto comprado usando detalle_ventas. 
SELECT ventas.idVentas, detalle_ventas.Productos_idProductos, detalle_ventas.Precio, detalle_ventas.Cantidad, ventas.Total
FROM detalle_ventas
INNER JOIN ventas ON detalle_ventas.Ventas_idVentas = ventas.idVentas
WHERE detalle_ventas.Cantidad > 1;

#7. Más de una tabla con inner join y filtros. 
#Muestra los empleados por su id, nombre y célula pero que tienen puntaje de 5
SELECT empleado.idEmpleado, empleado.Nombre, empleado.Supervisor_Célula, satisfacción_cliente.Puntos, satisfacción_cliente.Ventas_idVentas
FROM satisfacción_cliente
INNER JOIN empleado ON satisfacción_cliente.Empleado_idEmpleado = empleado.idEmpleado
WHERE satisfacción_cliente.Puntos > 4
ORDER BY empleado.idEmpleado;

#8. Una sola tabla con group by usando alguna función agregada.
#Muestra las sumatoria de todas las ventas que se hiceron por mes.
SELECT MONTH(Fecha) AS Mes, SUM(Total) AS Ventas_totales
FROM ventas
GROUP BY MONTH(Fecha);

