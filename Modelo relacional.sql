CREATE TABLE Usuarios (
    usuario_id INT PRIMARY KEY AUTO_INCREMENT,
    correo VARCHAR(255) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    telefono VARCHAR(20),
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Direcciones (
    direccion_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    direccion VARCHAR(255) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    codigo_postal VARCHAR(20) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id)
);

CREATE TABLE CategoriasProductos (
    categoria_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(255) NOT NULL
);

CREATE TABLE Productos (
    producto_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    categoria_id INT,
    talla VARCHAR(50),
    color VARCHAR(50),
    FOREIGN KEY (categoria_id) REFERENCES CategoriasProductos(categoria_id)
);

CREATE TABLE CarritosCompras (
    carrito_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id)
);

CREATE TABLE ProductosCarrito (
    producto_carrito_id INT PRIMARY KEY AUTO_INCREMENT,
    carrito_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    FOREIGN KEY (carrito_id) REFERENCES CarritosCompras(carrito_id),
    FOREIGN KEY (producto_id) REFERENCES Productos(producto_id)
);

CREATE TABLE Pedidos (
    pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    fecha_pedido DATETIME NOT NULL,
    estado VARCHAR(50) NOT NULL,
    monto_total DECIMAL(10, 2) NOT NULL,
    direccion_id INT,
    metodo_pago VARCHAR(50) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id),
    FOREIGN KEY (direccion_id) REFERENCES Direcciones(direccion_id)
);

CREATE TABLE DetallesPedido (
    detalle_pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    pedido_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(pedido_id),
    FOREIGN KEY (producto_id) REFERENCES Productos(producto_id)
);

CREATE TABLE OpinionesProductos (
    opinion_id INT PRIMARY KEY AUTO_INCREMENT,
    producto_id INT,
    usuario_id INT,
    calificacion INT NOT NULL,
    texto_opinion TEXT,
    fecha_opinion DATETIME NOT NULL,
    FOREIGN KEY (producto_id) REFERENCES Productos(producto_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id)
);

CREATE TABLE Notificaciones (
    notificacion_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    tipo VARCHAR(50),
    mensaje TEXT,
    estado VARCHAR(50),
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id)
);

CREATE TABLE MensajesChat (
    mensaje_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    mensaje TEXT,
    fecha_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id)
);

CREATE TABLE MetodosPago (
    metodo_pago_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    numero_tarjeta VARCHAR(16),
    titular_tarjeta VARCHAR(255),
    fecha_expiracion DATE,
    cvv VARCHAR(3),
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id)
);
