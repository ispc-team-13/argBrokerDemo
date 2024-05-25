-- Crear la base de datos
CREATE DATABASE ARGBrokerDemo;
USE ARGBrokerDemo;

-- Crear la tabla Usuario
CREATE TABLE Usuario (
    ID_Usuario INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Saldo_Inicial DECIMAL(10, 2) DEFAULT 1000000.00,
    Saldo_Actual DECIMAL(10, 2) DEFAULT 1000000.00,
    Perfil_Inversor ENUM('conservador', 'medio', 'agresivo') NOT NULL
);

-- Crear la tabla Acción
CREATE TABLE Accion (
    ID_Accion INT AUTO_INCREMENT PRIMARY KEY,
    Simbolo VARCHAR(10) NOT NULL UNIQUE,
    Nombre_Empresa VARCHAR(100) NOT NULL
);

-- Crear la tabla Transacción
CREATE TABLE Transaccion (
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
CREATE TABLE Cotizacion (
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
CREATE TABLE Portafolio (
    ID_Portafolio INT AUTO_INCREMENT PRIMARY KEY,
    ID_Usuario INT NOT NULL,
    ID_Accion INT NOT NULL,
    Cantidad INT NOT NULL,
    Valor_Comprometido DECIMAL(10, 2) NOT NULL,
    Ganancia_Perdida DECIMAL(10, 2),
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario),
    FOREIGN KEY (ID_Accion) REFERENCES Accion(ID_Accion)
);
