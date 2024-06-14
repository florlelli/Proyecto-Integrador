INSERT INTO productos(idProductos,Nombre,Descripción,Precio)
VALUES (01,'MotoG24','celular',360000),(02,'SamsungGalaxyA54','celular',690000),(03,'SamsungGalaxyS24','celular',1800000),
(04,'MotoG84','celular',590000);

SELECT * FROM productos;
SELECT * FROM productos WHERE Precio BETWEEN 360000 AND 590000;
SELECT * FROM productos WHERE Nombre='SamsungGalaxyA54';
SELECT * FROM productos WHERE Precio <1000000 LIMIT 2;
