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
