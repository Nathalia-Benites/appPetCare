-- Eliminar la base de datos si existe
DROP DATABASE IF EXISTS petCare;

-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS petCare;

-- Usar la base de datos
USE petCare;

-- Crear la tabla CATEGORIA
CREATE TABLE CATEGORIA (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(50) NOT NULL
);

-- Crear la tabla PRODUCTO
CREATE TABLE PRODUCTO (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(200) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    id_categoria INT,
    stock INT NOT NULL DEFAULT 0,
    FOREIGN KEY (id_categoria) REFERENCES CATEGORIA(id_categoria) ON DELETE CASCADE
);

-- Crear la tabla CLIENTE
CREATE TABLE CLIENTE (
    cedula VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    correo VARCHAR(100),
    telefono VARCHAR(15),
    ciudad VARCHAR(50)
);

-- Crear la tabla MASCOTA
CREATE TABLE MASCOTA (
    id_mascota INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    especie VARCHAR(50) NOT NULL,
    raza VARCHAR(50),
    fecha_nacimiento DATE,
    cedula_usuario VARCHAR(10),
    FOREIGN KEY (cedula_usuario) REFERENCES CLIENTE(cedula) ON DELETE CASCADE
);

-- Crear la tabla VENTA
CREATE TABLE VENTA (
    id_venta INT PRIMARY KEY AUTO_INCREMENT,
    cantidad INT NOT NULL,
    cedula_cliente VARCHAR(10) NOT NULL,
    id_producto INT NOT NULL,
    FOREIGN KEY (cedula_cliente) REFERENCES CLIENTE(cedula) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id_producto) ON DELETE CASCADE
);

-- Crear la tabla PEDIDO
CREATE TABLE PEDIDO (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    cedula_cliente VARCHAR(10) NOT NULL,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cedula_cliente) REFERENCES CLIENTE(cedula) ON DELETE CASCADE
);

-- Crear la tabla DETALLE_PEDIDO
CREATE TABLE DETALLE_PEDIDO (
    id_detalle INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES PEDIDO(id_pedido) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id_producto) ON DELETE CASCADE
);

-- Crear la tabla CITA
CREATE TABLE CITA (
    id_cita INT PRIMARY KEY AUTO_INCREMENT,
    tipo_cita ENUM('Peluqueria', 'Veterinaria', 'Vacunación', 'Desparasitacion') NOT NULL,
    fecha DATE NOT NULL,
    cedula_cliente VARCHAR(10) NOT NULL,
    FOREIGN KEY (cedula_cliente) REFERENCES CLIENTE(cedula) ON DELETE CASCADE
);

-- Insertar datos en la tabla CATEGORIA
INSERT INTO CATEGORIA(nombre_categoria) VALUES('Alimentos'), ('Juguetes'), ('Ropa y Accesorios'), ('Salud y Cuidado');

-- Insertar datos en la tabla PRODUCTO
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES
('Pepas', 3.50, 1, 100), ('Snacks', 2.25, 1, 150), ('Suplementos', 10.00, 1, 80),
('Pelota pequeña', 4.00, 2, 200), ('Juguete de cuerda', 6.50, 2, 120), ('Ratón de peluche', 3.25, 2, 300),
('Camiseta para perro', 12.00, 3, 50), ('Collar ajustable', 8.00, 3, 75), ('Cama para mascotas', 25.00, 3, 30),
('Casa para mascotas', 50.00, 3, 20), ('Plato para mascotas', 5.00, 3, 100),
('Champú para mascotas', 7.99, 4, 60), ('Vitaminas', 15.99, 4, 40), ('Pipetas antipulgas', 12.50, 4, 35),
('Pastillas antiparasitarias', 8.00, 4, 50), ('Pasta dental para mascotas', 5.50, 4, 70), ('Cepillo dental', 4.00, 4, 90),
('Crema para la piel', 9.99, 4, 45), ('Arena para gatos', 10.50, 4, 80);

-- Insertar datos en la tabla CLIENTE
INSERT INTO CLIENTE(cedula, nombre, direccion, telefono, ciudad, correo) VALUES
('1234567890', 'Simon Bolivar', 'Kra11#9-56', '7702291', 'Cali', 'simon.bolivar@example.com'),
('4561237890', 'Mark Zuckerberg', 'Cll 21#95-52', '+57-315291', 'Medellin', 'mark.zuckerberg@example.com');

-- Insertar datos en la tabla MASCOTA
INSERT INTO MASCOTA (nombre, especie, raza, fecha_nacimiento, cedula_usuario) VALUES
('Rex', 'Perro', 'Labrador', '2020-05-10', '1234567890'),
('Miau', 'Gato', 'Siames', '2021-04-20', '4561237890');

-- Insertar datos en la tabla PEDIDO
INSERT INTO PEDIDO (cedula_cliente, fecha, total) VALUES
('1234567890', '2023-05-01', 120.50), 
('4561237890', '2023-05-02', 85.75);

-- Insertar datos en la tabla DETALLE_PEDIDO
INSERT INTO DETALLE_PEDIDO (id_pedido, id_producto, cantidad, precio) VALUES
(1, 1, 3, 10.50), (1, 2, 1, 15.75), (2, 2, 2, 20.50), (2, 3, 1, 25.25);

-- Insertar datos en la tabla VENTA
INSERT INTO VENTA (cantidad, cedula_cliente, id_producto) VALUES
(1, '1234567890', 1), (2, '4561237890', 2);

