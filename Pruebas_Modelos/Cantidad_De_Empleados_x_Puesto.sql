SELECT puesto, COUNT(*) as cantidad_empleados
FROM empleados
GROUP BY puesto;
