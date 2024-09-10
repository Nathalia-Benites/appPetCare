-- Eliminar la base de datos si existe
DROP DATABASE IF EXISTS petCare;

-- Crear la base de datos
CREATE DATABASE petCare;
USE petCare;

-- Crear la tabla CATEGORIA
CREATE TABLE CATEGORIA (
    id_categoria INT(10) PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(50) NOT NULL
);

-- Crear la tabla PRODUCTO
CREATE TABLE PRODUCTO (
    id_producto INT(10) PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(200) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    id_categoria INT(10),
    stock INT(10) NOT NULL DEFAULT 0,  -- Agregado stock
    FOREIGN KEY (id_categoria) REFERENCES CATEGORIA(id_categoria)
);

-- Crear la tabla CLIENTE
CREATE TABLE CLIENTE (
    cedula VARCHAR(10) PRIMARY KEY, -- Cedula como PRIMARY KEY
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    correo_electronico VARCHAR(100),
    telefono VARCHAR(15),
    ciudad VARCHAR(50)
);

-- Crear la tabla MASCOTA
CREATE TABLE Mascota (
    id_mascota INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    especie VARCHAR(50) NOT NULL,
    raza VARCHAR(50),
    fecha_nacimiento DATE,
    cedula_usuario VARCHAR(10), -- Cedula del cliente
    FOREIGN KEY (cedula_usuario) REFERENCES CLIENTE(cedula)
);

-- Crear la tabla VENTA
CREATE TABLE VENTA (
    id_venta INT(10) PRIMARY KEY AUTO_INCREMENT,
    cantidad INT(10) NOT NULL,
    cedula_cliente VARCHAR(10) NOT NULL,  -- Cambiado de id_cliente a cedula_cliente
    id_producto INT(10) NOT NULL,
    FOREIGN KEY (cedula_cliente) REFERENCES CLIENTE(cedula),
    FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id_producto)
);

-- Crear la tabla PEDIDO
CREATE TABLE PEDIDO (
    id_pedido INT(10) PRIMARY KEY AUTO_INCREMENT,
    cedula_cliente VARCHAR(10) NOT NULL, -- Cambiado de id_cliente a cedula_cliente
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cedula_cliente) REFERENCES CLIENTE(cedula)
);

-- Crear la tabla DETALLE_PEDIDO
CREATE TABLE DETALLE_PEDIDO (
    id_detalle INT(10) PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT(10) NOT NULL,
    id_producto INT(10) NOT NULL,
    cantidad INT(10) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES PEDIDO(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id_producto)
);

-- Insertar datos en la tabla CATEGORIA
INSERT INTO CATEGORIA(nombre_categoria) VALUES('Alimentos');
INSERT INTO CATEGORIA(nombre_categoria) VALUES('Juguetes');
INSERT INTO CATEGORIA(nombre_categoria) VALUES('Ropa y Accesorios');
INSERT INTO CATEGORIA(nombre_categoria) VALUES('Salud y Cuidado');

-- Insertar datos en la tabla PRODUCTO para la categoría Alimentos
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Pepas', 3.50, 1, 100);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Snacks', 2.25, 1, 150);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Suplementos', 10.00, 1, 80);

-- Insertar datos en la tabla PRODUCTO para la categoría Juguetes
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Pelota pequeña', 4.00, 2, 200);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Juguete de cuerda', 6.50, 2, 120);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Ratón de peluche', 3.25, 2, 300);

-- Insertar datos en la tabla PRODUCTO para la categoría Ropa y Accesorios
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Camiseta para perro', 12.00, 3, 50);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Collar ajustable', 8.00, 3, 75);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Cama para mascotas', 25.00, 3, 30);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Casa para mascotas', 50.00, 3, 20);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Plato para mascotas', 5.00, 3, 100);

-- Insertar datos en la tabla PRODUCTO para la categoría Salud y Cuidado
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Champú para mascotas', 7.99, 4, 60);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Vitaminas', 15.99, 4, 40);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Pipetas antipulgas', 12.50, 4, 35);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Pastillas antiparasitarias', 8.00, 4, 50);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Pasta dental para mascotas', 5.50, 4, 70);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Cepillo dental', 4.00, 4, 90);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Crema para la piel', 9.99, 4, 45);
INSERT INTO PRODUCTO(descripcion, precio, id_categoria, stock) VALUES('Arena para gatos', 10.50, 4, 80);

-- Insertar datos en la tabla CLIENTE
INSERT INTO CLIENTE(cedula, nombre, direccion, telefono, ciudad, correo_electronico) VALUES('1234567890','Simon Bolivar', 'Kra11#9-56', '7702291', 'Cali', 'simon.bolivar@example.com');
INSERT INTO CLIENTE(cedula, nombre, direccion, telefono, ciudad, correo_electronico) VALUES('4561237890','Mark Zuckerberg', 'Cll 21#95-52', '+57-315291', 'Medellin', 'mark.zuckerberg@example.com');
INSERT INTO CLIENTE(cedula, nombre, direccion, telefono, ciudad, correo_electronico) VALUES('7894561230','Drew Barrymore', 'Kra52#65-05', '3125359456', 'Cali', 'drew.barrymore@example.com');
INSERT INTO CLIENTE(cedula, nombre, direccion, telefono, ciudad, correo_electronico) VALUES('7418529630','Larry Page', 'Cll 05#52-95', '7872296', 'Tunja', 'larry.page@example.com');
INSERT INTO CLIENTE(cedula, nombre, direccion, telefono, ciudad, correo_electronico) VALUES('1472583690','Tom Delonge', 'Cll 52#65-56', '7992293', 'Medellin', 'tom.delonge@example.com');
INSERT INTO CLIENTE(cedula, nombre, direccion, telefono, ciudad, correo_electronico) VALUES('8529637410','Simon Bolivar', 'Kra 21#65-52', '982295', 'Bogota', 'simon.bolivar@example.com');
INSERT INTO CLIENTE(cedula, nombre, direccion, telefono, ciudad, correo_electronico) VALUES('2589631470','Mark Hoppus', 'Cll 11#95-9', '8952294', 'Bogota', 'mark.hoppus@example.com');
INSERT INTO CLIENTE(cedula, nombre, direccion, telefono, ciudad, correo_electronico) VALUES('9638527410','Britney Spears', 'Cll 05#52-56', '7705295', 'Tunja', 'britney.spears@example.com');
INSERT INTO CLIENTE(cedula, nombre, direccion, telefono, ciudad, correo_electronico) VALUES('3692581470','John Forbes Nash', 'Kra 21#05-56', '776622966', 'Cali', 'john.nash@example.com');
INSERT INTO CLIENTE(cedula, nombre, direccion, telefono, ciudad, correo_electronico) VALUES('1597534860','Tom Delonge', 'Kra05#65-05', '6702293', 'Medellin', 'tom.delonge@example.com');

-- Insertar datos en la tabla MASCOTA
INSERT INTO Mascota (nombre, especie, raza, fecha_nacimiento, cedula_usuario) VALUES ('Rex', 'Perro', 'Labrador', '2020-05-10', '1234567890');
INSERT INTO Mascota (nombre, especie, raza, fecha_nacimiento, cedula_usuario) VALUES ('Miau', 'Gato', 'Siames', '2021-04-20', '4561237890');

-- Insertar datos en la tabla PEDIDO
INSERT INTO PEDIDO (cedula_cliente, fecha, total) VALUES ('1234567890', '2023-05-01', 120.50);
INSERT INTO PEDIDO (cedula_cliente, fecha, total) VALUES ('4561237890', '2023-05-02', 85.75);

-- Insertar datos en la tabla DETALLE_PEDIDO
INSERT INTO DETALLE_PEDIDO (id_pedido, id_producto, cantidad, precio) VALUES (1, 1, 3, 10.50);
INSERT INTO DETALLE_PEDIDO (id_pedido, id_producto, cantidad, precio) VALUES (1, 2, 1, 15.75);
INSERT INTO DETALLE_PEDIDO (id_pedido, id_producto, cantidad, precio) VALUES (2, 2, 2, 20.50);
INSERT INTO DETALLE_PEDIDO (id_pedido, id_producto, cantidad, precio) VALUES (2, 3, 1, 25.25);

-- Insertar datos en la tabla VENTA
INSERT INTO VENTA (cantidad, cedula_cliente, id_producto) VALUES (1, '1234567890', 1);
INSERT INTO VENTA (cantidad, cedula_cliente, id_producto) VALUES (2, '4561237890', 2);
INSERT INTO VENTA (cantidad, cedula_cliente, id_producto) VALUES (3, '7894561230', 3);
