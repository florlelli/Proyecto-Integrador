SELECT 
    ventas.id_venta, 
    clientes.nombre AS nombre_cliente, 
    productos.nombre AS nombre_producto, 
    ventas.fecha_venta, 
    ventas.monto_total
FROM 
    ventas
INNER JOIN 
    clientes ON ventas.id_cliente = clientes.id_cliente
INNER JOIN 
    productos ON ventas.id_producto = productos.id_producto
WHERE 
    ventas.fecha_venta BETWEEN '2023-01-01' AND '2023-12-31'
    AND ventas.monto_total > 200.000;
