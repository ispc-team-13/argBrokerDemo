-- Obtener todos los usuarios con sus perfiles inversores:
SELECT Nombre, Apellido, Perfil_Inversor FROM Usuario;
-- Listar todas las acciones disponibles en la base de datos:
SELECT Simbolo, Nombre_Empresa FROM Accion;
-- Mostrar las transacciones realizadas por un usuario específico (por ejemplo, con ID_Usuario
SELECT * FROM Transaccion WHERE ID_Usuario = 1;
-- Calcular el saldo actual de cada usuario:
SELECT Nombre, Apellido, Saldo_Actual FROM Usuario;
-- Listar todas las cotizaciones de una acción específica (por ejemplo, con ID_Accion = 1):
SELECT * FROM Cotizacion WHERE ID_Accion = 1;
-- Mostrar el portafolio completo de un usuario específico (por ejemplo, con ID_Usuario = 2):
SELECT p.ID_Accion, a.Simbolo, a.Nombre_Empresa, p.Cantidad, p.Valor_Comprometido, p.Ganancia_Perdida 
FROM Portafolio p
JOIN Accion a ON p.ID_Accion = a.ID_Accion
WHERE p.ID_Usuario = 2;
-- Mostrar la última cotización de cada acción:
SELECT a.Simbolo, a.Nombre_Empresa, c.Ultimo_Operado, c.Ultimo_Cierre
FROM Accion a
JOIN Cotizacion c ON a.ID_Accion = c.ID_Accion
WHERE c.ID_Cotizacion IN (
    SELECT MAX(ID_Cotizacion) 
    FROM Cotizacion 
    GROUP BY ID_Accion
);
-- Listar todas las compras realizadas en las transacciones:
SELECT * FROM Transaccion WHERE Tipo = 'compra';
-- Obtener el total de comisiones pagadas por un usuario específico (por ejemplo, con ID_Usuario = 3):
SELECT u.Nombre, u.Apellido, SUM(t.Comision) AS Total_Comision
FROM Usuario u
JOIN Transaccion t ON u.ID_Usuario = t.ID_Usuario
WHERE u.ID_Usuario = 3
GROUP BY u.ID_Usuario;












