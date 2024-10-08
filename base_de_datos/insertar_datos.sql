-- Insertar usuarios con el campo CUIL
INSERT INTO Usuario (Nombre, Apellido, Email, Saldo_Inicial, Saldo_Actual, Perfil_Inversor, Contrasena, CUIL) VALUES 
('Nahuel', 'Gonzalez', 'nahuel@example.com', 1000000.00, 1000000.00, 'medio', 'password1', '20-12345678-9'),
('Sofia', 'Martinez', 'sofia@example.com', 1000000.00, 1000000.00, 'agresivo', 'password2', '20-23456789-0'),
('Gaston', 'Lopez', 'gaston@example.com', 1000000.00, 1000000.00, 'conservador', 'password3', '20-34567890-1'),
('Eric', 'Ramirez', 'eric@example.com', 1000000.00, 1000000.00, 'medio', 'password4', '20-45678901-2'),
('Agustin', 'Fernandez', 'agustin@example.com', 1000000.00, 1000000.00, 'agresivo', 'password5', '20-56789012-3');

-- Insertar acciones
INSERT INTO Accion (Simbolo, Nombre_Empresa) VALUES 
('AAPL', 'Apple Inc.'),
('GOOGL', 'Alphabet Inc.'),
('AMZN', 'Amazon.com Inc.'),
('TSLA', 'Tesla Inc.'),
('MSFT', 'Microsoft Corporation');

-- Insertar cotizaciones
INSERT INTO Cotizacion (ID_Accion, Ultimo_Operado, Cantidad_Compra_Diaria, Precio_Compra_Actual, Precio_Venta_Actual, Cantidad_Venta_Diaria, Apertura, Minimo_Diario, Maximo_Diario, Ultimo_Cierre) VALUES
(1, 150.00, 100, 150.00, 151.00, 80, 148.00, 147.50, 151.50, 149.00),
(2, 2800.00, 50, 2790.00, 2805.00, 40, 2785.00, 2770.00, 2820.00, 2795.00),
(3, 3300.00, 200, 3295.00, 3305.00, 120, 3280.00, 3270.00, 3350.00, 3290.00),
(4, 720.00, 150, 715.00, 725.00, 90, 710.00, 705.00, 730.00, 718.00),
(5, 290.00, 300, 289.00, 292.00, 250, 288.00, 287.00, 295.00, 290.50);

-- Insertar transacciones
INSERT INTO Transaccion (ID_Usuario, ID_Accion, Fecha, Tipo, Cantidad, Precio, Comision) VALUES
(1, 1, NOW(), 'compra', 10, 150.00, 1.50),   -- Nahuel compra 10 acciones de Apple
(1, 2, NOW(), 'compra', 5, 2800.00, 2.80),  -- Nahuel compra 5 acciones de Alphabet
(2, 3, NOW(), 'venta', 2, 3300.00, 3.30),   -- Sofía vende 2 acciones de Amazon
(3, 4, NOW(), 'compra', 20, 720.00, 0.72),   -- Gastón compra 20 acciones de Tesla
(4, 5, NOW(), 'compra', 15, 290.00, 0.29),   -- Eric compra 15 acciones de Microsoft
(5, 1, NOW(), 'venta', 3, 150.00, 0.15);      -- Agustín vende 3 acciones de Apple

-- Insertar portafolios
INSERT INTO Portafolio (ID_Usuario, ID_Accion, Cantidad, Valor_Comprometido, Ganancia_Perdida) VALUES
(1, 1, 10, 1500.00, 0.00),    -- Nahuel tiene 10 acciones de Apple
(1, 2, 5, 14000.00, 0.00),     -- Nahuel tiene 5 acciones de Alphabet
(2, 3, 2, 6600.00, 0.00),      -- Sofía tiene 2 acciones de Amazon
(3, 4, 20, 14400.00, 0.00),    -- Gastón tiene 20 acciones de Tesla
(4, 5, 15, 4350.00, 0.00),     -- Eric tiene 15 acciones de Microsoft
(5, 1, 3, 450.00, 0.00);        -- Agustín tiene 3 acciones de Apple
