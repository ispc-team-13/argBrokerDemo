-- Insertar datos en la tabla Usuario
INSERT INTO Usuario (Nombre, Apellido, Email, Saldo_Inicial, Saldo_Actual, Perfil_Inversor)
VALUES 
('Juan', 'Pérez', 'juan.perez@example.com', 1000000.00, 1000000.00, 'conservador'),
('Ana', 'García', 'ana.garcia@example.com', 1000000.00, 1000000.00, 'medio'),
('Carlos', 'López', 'carlos.lopez@example.com', 1000000.00, 1000000.00, 'agresivo');

-- Insertar datos en la tabla Acción
INSERT INTO Accion (Simbolo, Nombre_Empresa)
VALUES 
('AAPL', 'Apple Inc.'),
('GOOGL', 'Alphabet Inc.'),
('AMZN', 'Amazon.com Inc.');

-- Insertar datos en la tabla Cotizacion
INSERT INTO Cotizacion (ID_Accion, Ultimo_Operado, Cantidad_Compra_Diaria, Precio_Compra_Actual, Precio_Venta_Actual, Cantidad_Venta_Diaria, Apertura, Minimo_Diario, Maximo_Diario, Ultimo_Cierre)
VALUES
(1, 150.25, 1000, 150.00, 150.50, 800, 149.50, 148.00, 151.00, 149.75),
(2, 2750.00, 500, 2745.00, 2755.00, 450, 2730.00, 2700.00, 2760.00, 2725.00),
(3, 3450.75, 600, 3450.00, 3455.00, 580, 3440.00, 3400.00, 3470.00, 3435.00);

-- Insertar datos en la tabla Transaccion
INSERT INTO Transaccion (ID_Usuario, ID_Accion, Fecha, Tipo, Cantidad, Precio, Comision)
VALUES
(1, 1, '2024-05-01 10:00:00', 'compra', 10, 150.00, 1.50),
(2, 2, '2024-05-01 11:00:00', 'compra', 5, 2750.00, 2.75),
(3, 3, '2024-05-01 12:00:00', 'compra', 2, 3450.00, 3.45);

-- Insertar datos en la tabla Portafolio
INSERT INTO Portafolio (ID_Usuario, ID_Accion, Cantidad, Valor_Comprometido, Ganancia_Perdida)
VALUES
(1, 1, 10, 1500.00, 5.00),
(2, 2, 5, 13750.00, 25.00),
(3, 3, 2, 6900.00, 10.00);