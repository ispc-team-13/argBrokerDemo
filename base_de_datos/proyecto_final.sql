CREATE DATABASE nombre_de_tu_base_de_datos;

USE nombre_de_tu_base_de_datos;

CREATE TABLE Usuario (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    saldo_inicial DECIMAL(10,2)
);

CREATE TABLE Accion (
    simbolo VARCHAR(50) PRIMARY KEY,
    nombre_empresa VARCHAR(100),
    ultimo_operado DECIMAL(10,2),
    cantidad_compra_diaria INT,
    precio_compra_actual DECIMAL(10,2),
    precio_venta_actual DECIMAL(10,2),
    cantidad_venta_diaria INT,
    apertura DECIMAL(10,2),
    minimo_diario DECIMAL(10,2),
    maximo_diario DECIMAL(10,2),
    ultimo_cierre DECIMAL(10,2)
);

CREATE TABLE Transaccion (
    id INT PRIMARY KEY,
    usuario_id INT,
    accion_simbolo VARCHAR(50),
    tipo VARCHAR(10),
    cantidad INT,
    precio DECIMAL(10,2),
    comision DECIMAL(10,2),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id),
    FOREIGN KEY (accion_simbolo) REFERENCES Accion(simbolo)
);

CREATE TABLE Portafolio (
    usuario_id INT,
    simbolo VARCHAR(50),
    cantidad INT,
    total_invertido DECIMAL(10,2),
    saldo DECIMAL(10,2),
    ganancia_perdida DECIMAL(10,2),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id),
    FOREIGN KEY (simbolo) REFERENCES Accion(simbolo)
);
