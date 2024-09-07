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

-- Crear la tabla CLIENTE sin contraseña
CREATE TABLE CLIENTE (
    id_cliente INT(10) PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(50) NOT NULL,
    telefono VARCHAR(50) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    correo VARCHAR(100) NOT NULL
);

-- Crear la tabla VENTA
CREATE TABLE VENTA (
    id_venta INT(10) PRIMARY KEY AUTO_INCREMENT,
    cantidad INT(10) NOT NULL,
    id_cliente INT(10) NOT NULL,
    id_producto INT(10) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id_producto)
);

-- Crear la tabla PEDIDO
CREATE TABLE PEDIDO (
    id_pedido INT(10) PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT(10) NOT NULL,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente)
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
INSERT INTO CLIENTE(id_cliente, nombre, direccion, telefono, ciudad, correo) VALUES(123,'Simon Bolivar', 'Kra11#9-56', '7702291', 'Cali', 'simon.bolivar@example.com');
INSERT INTO CLIENTE(id_cliente, nombre, direccion, telefono, ciudad, correo) VALUES(456,'Mark Zuckerberg', 'Cll 21#95-52', '+57-315291', 'Medellin', 'mark.zuckerberg@example.com');
INSERT INTO CLIENTE(id_cliente, nombre, direccion, telefono, ciudad, correo) VALUES(789,'Drew Barrymore', 'Kra52#65-05', '3125359456', 'Cali', 'drew.barrymore@example.com');
INSERT INTO CLIENTE(id_cliente, nombre, direccion, telefono, ciudad, correo) VALUES(741,'Larry Page', 'Cll 05#52-95', '7872296', 'Tunja', 'larry.page@example.com');
INSERT INTO CLIENTE(id_cliente, nombre, direccion, telefono, ciudad, correo) VALUES(147,'Tom Delonge', 'Cll 52#65-56', '7992293', 'Medellin', 'tom.delonge@example.com');
INSERT INTO CLIENTE(id_cliente, nombre, direccion, telefono, ciudad, correo) VALUES(852,'Simon Bolivar', 'Kra 21#65-52', '982295', 'Bogota', 'simon.bolivar@example.com');
INSERT INTO CLIENTE(id_cliente, nombre, direccion, telefono, ciudad, correo) VALUES(258,'Mark Hoppus', 'Cll 11#95-9', '8952294', 'Bogota', 'mark.hoppus@example.com');
INSERT INTO CLIENTE(id_cliente, nombre, direccion, telefono, ciudad, correo) VALUES(963,'Britney Spears', 'Cll 05#52-56', '7705295', 'Tunja', 'britney.spears@example.com');
INSERT INTO CLIENTE(id_cliente, nombre, direccion, telefono, ciudad, correo) VALUES(369,'John Forbes Nash', 'Kra 21#05-56', '776622966', 'Cali', 'john.nash@example.com');
INSERT INTO CLIENTE(id_cliente, nombre, direccion, telefono, ciudad, correo) VALUES(159,'Tom Delonge', 'Kra05#65-05', '6702293', 'Medellin', 'tom.delonge@example.com');
INSERT INTO CLIENTE(id_cliente, nombre, direccion, telefono, ciudad, correo) VALUES(753,'Sergey Brin', 'Cll 11#65-11', '9702299', 'Medellin', 'sergey.brin@example.com');
INSERT INTO CLIENTE(id_cliente, nombre, direccion, telefono, ciudad, correo) VALUES(153,'Emma Watson', 'Kra 9#9-95', '31569638', 'Tunja', 'emma.watson@example.com');

-- Insertar datos en la tabla VENTA
INSERT INTO VENTA(cantidad, id_cliente, id_producto) VALUES(5, 123, 1);
INSERT INTO VENTA(cantidad, id_cliente, id_producto) VALUES(6, 123, 2);
INSERT INTO VENTA(cantidad, id_cliente, id_producto) VALUES(7, 123, 3);
INSERT INTO VENTA(cantidad, id_cliente, id_producto) VALUES(8, 123, 4);
INSERT INTO VENTA(cantidad, id_cliente, id_producto) VALUES(2, 456, 5);
INSERT INTO VENTA(cantidad, id_cliente, id_producto) VALUES(4, 741, 6);
INSERT INTO VENTA(cantidad, id_cliente, id_producto) VALUES(5, 741, 7);
INSERT INTO VENTA(cantidad, id_cliente, id_producto) VALUES(10, 456, 8);
