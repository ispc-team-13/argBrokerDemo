-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS ARGBrokerDemo;
USE ARGBrokerDemo;

-- Crear la tabla Usuario con el campo de contraseña y Cuil
CREATE TABLE IF NOT EXISTS Usuario (
    ID_Usuario INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Contrasena VARCHAR(255) NOT NULL, 
    Cuil VARCHAR(20) NOT NULL UNIQUE,  -- Nuevo campo Cuil
    Saldo_Inicial DECIMAL(10, 2) DEFAULT 1000000.00,
    Saldo_Actual DECIMAL(10, 2) DEFAULT 1000000.00,
    Perfil_Inversor ENUM('conservador', 'medio', 'agresivo') NOT NULL
);

-- Crear la tabla Acción
CREATE TABLE IF NOT EXISTS Accion (
    ID_Accion INT AUTO_INCREMENT PRIMARY KEY,
    Simbolo VARCHAR(10) NOT NULL UNIQUE,
    Nombre_Empresa VARCHAR(100) NOT NULL
);

-- Crear la tabla Transacción
CREATE TABLE IF NOT EXISTS Transaccion (
    ID_Transaccion INT AUTO_INCREMENT PRIMARY KEY,
    ID_Usuario INT NOT NULL,
    ID_Accion INT NOT NULL,
    Fecha DATETIME NOT NULL,
    Tipo ENUM('compra', 'venta') NOT NULL,
    Cantidad INT NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL,
    Comision DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario),
    FOREIGN KEY (ID_Accion) REFERENCES Accion(ID_Accion)
);

-- Crear la tabla Cotización
CREATE TABLE IF NOT EXISTS Cotizacion (
    ID_Cotizacion INT AUTO_INCREMENT PRIMARY KEY,
    ID_Accion INT NOT NULL,
    Ultimo_Operado DECIMAL(10, 2),
    Cantidad_Compra_Diaria INT,
    Precio_Compra_Actual DECIMAL(10, 2),
    Precio_Venta_Actual DECIMAL(10, 2),
    Cantidad_Venta_Diaria INT,
    Apertura DECIMAL(10, 2),
    Minimo_Diario DECIMAL(10, 2),
    Maximo_Diario DECIMAL(10, 2),
    Ultimo_Cierre DECIMAL(10, 2),
    FOREIGN KEY (ID_Accion) REFERENCES Accion(ID_Accion)
);

-- Crear la tabla Portafolio
CREATE TABLE IF NOT EXISTS Portafolio (
    ID_Portafolio INT AUTO_INCREMENT PRIMARY KEY,
    ID_Usuario INT NOT NULL,
    ID_Accion INT NOT NULL,
    Cantidad INT NOT NULL,
    Valor_Comprometido DECIMAL(10, 2) NOT NULL DEFAULT 0,
    Ganancia_Perdida DECIMAL(10, 2),
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario),
    FOREIGN KEY (ID_Accion) REFERENCES Accion(ID_Accion)
);

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
WHERE U.ID_Usuario = 2;

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

-- modificacion de comuna valor comprometido
ALTER TABLE Portafolio MODIFY COLUMN Valor_Comprometido DECIMAL(10, 2) DEFAULT 0;