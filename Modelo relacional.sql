CREATE TABLE Usuarios (
    usuario_id INT PRIMARY KEY AUTO_INCREMENT,
    correo VARCHAR(255) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(15),
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX(correo)
);

CREATE TABLE Direcciones (
    direccion_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    codigo_postal VARCHAR(10) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id) ON DELETE CASCADE,
    INDEX(usuario_id)
);

CREATE TABLE CategoriasProductos (
    categoria_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(100) NOT NULL,
    UNIQUE(nombre_categoria)
);

CREATE TABLE Productos (
    producto_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    categoria_id INT NOT NULL,
    talla VARCHAR(20),
    color VARCHAR(30),
    FOREIGN KEY (categoria_id) REFERENCES CategoriasProductos(categoria_id) ON DELETE SET NULL,
    INDEX(categoria_id)
);

CREATE TABLE CarritosCompras (
    carrito_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id) ON DELETE CASCADE,
    INDEX(usuario_id)
);

CREATE TABLE ProductosCarrito (
    producto_carrito_id INT PRIMARY KEY AUTO_INCREMENT,
    carrito_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (carrito_id) REFERENCES CarritosCompras(carrito_id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES Productos(producto_id) ON DELETE CASCADE,
    INDEX(carrito_id),
    INDEX(producto_id)
);

CREATE TABLE Pedidos (
    pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    fecha_pedido DATETIME NOT NULL,
    estado VARCHAR(50) NOT NULL CHECK(estado IN ('Pendiente', 'Enviado', 'Entregado', 'Cancelado')),
    monto_total DECIMAL(10, 2) NOT NULL,
    direccion_id INT NOT NULL,
    metodo_pago VARCHAR(50) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id) ON DELETE CASCADE,
    FOREIGN KEY (direccion_id) REFERENCES Direcciones(direccion_id) ON DELETE SET NULL,
    INDEX(usuario_id),
    INDEX(direccion_id)
);

CREATE TABLE DetallesPedido (
    detalle_pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(pedido_id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES Productos(producto_id) ON DELETE CASCADE,
    INDEX(pedido_id),
    INDEX(producto_id)
);

CREATE TABLE OpinionesProductos (
    opinion_id INT PRIMARY KEY AUTO_INCREMENT,
    producto_id INT NOT NULL,
    usuario_id INT NOT NULL,
    calificacion INT NOT NULL CHECK(calificacion BETWEEN 1 AND 5),
    texto_opinion TEXT,
    fecha_opinion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (producto_id) REFERENCES Productos(producto_id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id) ON DELETE CASCADE,
    INDEX(producto_id),
    INDEX(usuario_id)
);

CREATE TABLE Notificaciones (
    notificacion_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    mensaje TEXT NOT NULL,
    estado VARCHAR(20) NOT NULL CHECK(estado IN ('No Leída', 'Leída')),
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id) ON DELETE CASCADE,
    INDEX(usuario_id)
);

CREATE TABLE MensajesChat (
    mensaje_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    mensaje TEXT NOT NULL,
    fecha_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id) ON DELETE CASCADE,
    INDEX(usuario_id)
);

CREATE TABLE MetodosPago (
    metodo_pago_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    numero_tarjeta VARCHAR(16) NOT NULL,
    titular_tarjeta VARCHAR(100) NOT NULL,
    fecha_expiracion DATE NOT NULL,
    cvv VARCHAR(3) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id) ON DELETE CASCADE,
    INDEX(usuario_id)
);

