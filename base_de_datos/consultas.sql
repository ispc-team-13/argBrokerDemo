-- Consultar todos los usuarios
SELECT * FROM Usuario;

-- Consultar el saldo actual de todos los usuarios
SELECT Nombre, Apellido, Saldo_Actual FROM Usuario;

-- Consultar las acciones disponibles
SELECT * FROM Accion;

-- Consultar todas las transacciones realizadas por un usuario específico (por ejemplo, ID_Usuario = 1)
SELECT * FROM Transaccion WHERE ID_Usuario = 1;

-- Consultar todas las transacciones de tipo 'compra'
SELECT * FROM Transaccion WHERE Tipo = 'compra';

-- Consultar todas las transacciones de un usuario específico con detalles de acciones
SELECT T.ID_Transaccion, U.Nombre, U.Apellido, A.Nombre_Empresa, T.Fecha, T.Tipo, T.Cantidad, T.Precio
FROM Transaccion T
JOIN Usuario U ON T.ID_Usuario = U.ID_Usuario
JOIN Accion A ON T.ID_Accion = A.ID_Accion
WHERE U.ID_Usuario = 1;

-- Consultar la cotización más reciente para cada acción
SELECT C.ID_Accion, A.Nombre_Empresa, C.Ultimo_Operado, C.Precio_Compra_Actual, C.Precio_Venta_Actual
FROM Cotizacion C
JOIN Accion A ON C.ID_Accion = A.ID_Accion;

-- Consultar el portafolio de un usuario específico (por ejemplo, ID_Usuario = 1)
SELECT P.ID_Portafolio, A.Nombre_Empresa, P.Cantidad, P.Valor_Comprometido, P.Ganancia_Perdida
FROM Portafolio P
JOIN Accion A ON P.ID_Accion = A.ID_Accion
WHERE P.ID_Usuario = 1;

-- Consultar las ganancias y pérdidas de un usuario en su portafolio
SELECT U.Nombre, U.Apellido, SUM(P.Ganancia_Perdida) AS Total_Ganancia_Perdida
FROM Portafolio P
JOIN Usuario U ON P.ID_Usuario = U.ID_Usuario
GROUP BY U.ID_Usuario;

-- Consultar el total de acciones compradas y vendidas por cada usuario
SELECT U.Nombre, U.Apellido, 
       SUM(CASE WHEN T.Tipo = 'compra' THEN T.Cantidad ELSE 0 END) AS Total_Compradas,
       SUM(CASE WHEN T.Tipo = 'venta' THEN T.Cantidad ELSE 0 END) AS Total_Vendidas
FROM Transaccion T
JOIN Usuario U ON T.ID_Usuario = U.ID_Usuario
GROUP BY U.ID_Usuario;

-- Consultar las acciones con su cotización actual y el último operado
SELECT A.Nombre_Empresa, C.Ultimo_Operado, C.Precio_Compra_Actual, C.Precio_Venta_Actual
FROM Cotizacion C
JOIN Accion A ON C.ID_Accion = A.ID_Accion;

-- Consultar el historial de precios de una acción específica (por ejemplo, ID_Accion = 1)
SELECT * FROM Cotizacion WHERE ID_Accion = 1 ORDER BY ID_Cotizacion DESC;

-- Consultar el total de usuarios en la base de datos
SELECT COUNT(*) AS Total_Usuarios FROM Usuario;

-- Consultar el total de acciones en la base de datos
SELECT COUNT(*) AS Total_Acciones FROM Accion;

-- Consultar la cantidad total de transacciones realizadas
SELECT COUNT(*) AS Total_Transacciones FROM Transaccion;

-- Consultar la cantidad de acciones que un usuario tiene en su portafolio
SELECT U.Nombre, U.Apellido, SUM(P.Cantidad) AS Total_Actions
FROM Portafolio P
JOIN Usuario U ON P.ID_Usuario = U.ID_Usuario
GROUP BY U.ID_Usuario;

-- Consultar todas las transacciones con detalles de usuario y acción
SELECT T.ID_Transaccion, U.Nombre, U.Apellido, A.Nombre_Empresa, T.Fecha, T.Tipo, T.Cantidad, T.Precio
FROM Transaccion T
JOIN Usuario U ON T.ID_Usuario = U.ID_Usuario
JOIN Accion A ON T.ID_Accion = A.ID_Accion;

-- Consultar el rendimiento de las acciones en función de las transacciones
SELECT A.Nombre_Empresa, 
       SUM(CASE WHEN T.Tipo = 'compra' THEN T.Cantidad ELSE 0 END) AS Total_Compradas,
       SUM(CASE WHEN T.Tipo = 'venta' THEN T.Cantidad ELSE 0 END) AS Total_Vendidas,
       (SUM(CASE WHEN T.Tipo = 'venta' THEN T.Cantidad ELSE 0 END) - 
        SUM(CASE WHEN T.Tipo = 'compra' THEN T.Cantidad ELSE 0 END)) AS Total_Rendimiento
FROM Transaccion T
JOIN Accion A ON T.ID_Accion = A.ID_Accion
GROUP BY A.ID_Accion;

-- Consultar el saldo total de todos los usuarios y sus ganancias/pérdidas
SELECT U.Nombre, U.Apellido, U.Saldo_Actual, SUM(P.Ganancia_Perdida) AS Total_Ganancia_Perdida
FROM Usuario U
JOIN Portafolio P ON U.ID_Usuario = P.ID_Usuario
GROUP BY U.ID_Usuario;


-- Actualizar el saldo de un usuario específico (por ejemplo, ID_Usuario = 1)
UPDATE Usuario SET Saldo_Actual = 1500.00 WHERE ID_Usuario = 1;

-- Actualizar el nombre de un usuario específico (por ejemplo, ID_Usuario = 1)
UPDATE Usuario SET Nombre = 'Carlos' WHERE ID_Usuario = 1;

-- Actualizar el apellido de un usuario específico (por ejemplo, ID_Usuario = 1)
UPDATE Usuario SET Apellido = 'González' WHERE ID_Usuario = 1;

-- Actualizar el saldo de todos los usuarios (aumentar en un porcentaje, por ejemplo, 10%)
UPDATE Usuario SET Saldo_Actual = Saldo_Actual * 1.10;

-- Actualizar el saldo de todos los usuarios a un nuevo valor (por ejemplo, 2000.00)
UPDATE Usuario SET Saldo_Actual = 2000.00;

