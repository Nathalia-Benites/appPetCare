# AppPetCare
Escribir sobre el contexto de su solución.

AppPetCare es una aplicación dedicada al cuidado de perros y gatos que permite al usuario comprar en línea alimentos, juguetes, ropa, accesorios y productos de salud para su mascota. Incluye funciones de registro e inicio de sesión. Su menú de navegación facilita el acceso a categorías de productos, historial y estado de pedidos, perfil de usuario con opciones de dirección y formas de pago, notificaciones de ofertas y promociones, una sección de preguntas frecuentes y soporte mediante chat. Brinda un catálogo con filtros de búsqueda, descripciones de los productos con opciones de compra y seguimiento de pedidos hasta la entrega.

## Modelo Relacional
- Adjuntar modelo
  
*Usuarios (Usuarios)*

- usuario_id (PK)
- correo_electronico
- contraseña
- nombre
- telefono
- fecha_creacion

*Direcciones (Direcciones)* 

- direccion_id (PK)
- usuario_id (FK)
- direccion
- ciudad
- estado
- codigo_postal
- pais
  
*Categorías de Productos (CategoriasProductos)*

- categoria_id (PK)
- nombre_categoria

*Productos (Productos)*

- producto_id (PK)
- nombre
- descripcion
- precio
- stock
- categoria_id (FK)
- talla
- color

*Carritos de Compras (CarritosCompras)*

- carrito_id (PK)
- usuario_id (FK)

*Productos en el Carrito (ProductosCarrito)*

- producto_carrito_id (PK)
- carrito_id (FK)
- producto_id (FK)
- cantidad

*Pedidos (Pedidos)*

- pedido_id (PK)
- usuario_id (FK)
- fecha_pedido
- estado
- monto_total
- direccion_id (FK)
- metodo_pago

*Detalles del Pedido (DetallesPedido)*

- detalle_pedido_id (PK)
- pedido_id (FK)
- producto_id (FK)
- cantidad
- precio

*Opiniones de Productos (OpinionesProductos)*

- opinion_id (PK)
- producto_id (FK)
- usuario_id (FK)
- calificacion
- texto_opinion
- fecha_opinion

*Notificaciones (Notificaciones)*

- notificacion_id (PK)
- usuario_id (FK)
- tipo
- mensaje
- estado
- fecha_creacion

*Mensajes de Chat (MensajesChat)*

- mensaje_id (PK)
- usuario_id (FK)
- mensaje
- fecha_envio

*Métodos de Pago (MetodosPago)*

- metodo_pago_id (PK)
- usuario_id (FK)
- numero_tarjeta
- titular_tarjeta
- fecha_expiracion
- cvv

*Relaciones*

Un usuario puede tener múltiples direcciones (1:N).
Un usuario puede tener un solo carrito de compras (1:1).
Un carrito de compras puede contener múltiples productos (1:N).
Un usuario puede realizar múltiples pedidos (1:N).
Un pedido puede tener múltiples detalles de pedido (1:N).
Un producto pertenece a una categoría (1:1).
Un producto puede tener múltiples opiniones (1:N).
Un usuario puede escribir múltiples opiniones (1:N).
Un usuario puede recibir múltiples notificaciones (1:N).
Un usuario puede enviar múltiples mensajes de chat (1:N).
Un usuario puede tener múltiples métodos de pago registrados (1:N).


## Desarrollo de propuesta
- Escribir sobre la solución a realizar.

Se va a desarrollar la aplicación de la siguiente manera: 

*1. Pantalla de Inicio y Registro*

- Bienvenida y un breve tutorial sobre cómo usar la aplicación.
- Registro con correo electrónico y número de teléfono.
- Inicio de sesión con credenciales de usuario existentes.
- Recuperación de la contraseña en caso de olvido.
  
*2. Menú de Navegación*

- Inicio: Acceso a la pantalla principal y categorías de productos.
- Productos: Listado completo de productos para perros y gatos.
- Pedidos: Historial de pedidos y estado actual de los pedidos.
- Perfil: Información personal del usuario, direcciones de envío y métodos de pago.
- Notificaciones: Alertas sobre ofertas, promociones y actualizaciones de pedidos.
- Chat: Acceso a soporte al cliente y preguntas sobre en.
  
*3. Catálogo de Productos*

Categorías:
- Alimentos: Subcategorías para perros y gatos (Pepas, snacks, suplementos).
- Juguetes: Diversos tipos de juguetes clasificados por tamaño y tipo de mascota.
- Ropa y Accesorios: Ropa para diferentes tamaños, collares y correas.
- Salud y Cuidado: Productos de higiene, vitaminas y productos para el cuidado dental.
  
Filtros y Búsqueda:
- Filtros avanzados por tamaño, precio, marca y color.
- Barra de búsqueda para encontrar productos específicos rápidamente.
  
*4. Detalles del Producto*

- Galería de imágenes del producto.
- Detalles sobre el producto, materiales, instrucciones de uso.
- Opciones de tamaños y colores.
- Información sobre el precio y posibles descuentos.
- Opiniones de otros usuarios y calificación promedio.
  
Añadir al Carrito:
- Selección de la cantidad a comprar.
- Opción para agregar el producto al carrito de compras.
  
*5. Carrito de Compras*

Vista del Carrito:
- Lista de todos los productos añadidos al carrito.
- Subtotal, impuestos, costos de envío.
- Opción para modificar cantidades o eliminar productos.
  
Proceso de Compra:
- Selección o adición de una dirección de envío.
- Selección de método de pago (tarjeta de crédito o PayPal).
- Confirmación del pedido.
  
*6. Seguimiento del Pedido*

Estado del Pedido:
- Pendiente: Pedido recibido y en proceso de preparación.
- Enviado: Pedido enviado y en camino.
- Entregado: Pedido entregado al cliente.
  
Historial de Pedidos:
- Listado de pedidos anteriores con opción para repetir compra.
  
*7. Perfil del Usuario*

Información Personal:
- Datos de Usuario: Nombre, correo electrónico, teléfono.
- Direcciones de envío
- Métodos de Pago
  
*8. Notificaciones y Promociones*

- Alertas sobre descuentos y promociones.
- Notificaciones sobre el estado del pedido.

*9. Centro de Ayuda*

- Respuestas a preguntas frecuentes.
- Contacto con Soporte en Chat en vivo, correo electrónico y número de teléfono.

Ejemplos de uso:

1. Abres la aplicación y te registras con tu correo.
2. Navegas a la categoría de "Ropa para Perros".
3. Filtras por tamaño y añades un abrigo al carrito.
4. Vas al carrito, seleccionas tu dirección de envío y método de pago.
5. Confirmas el pedido y recibes notificaciones sobre el estado del mismo.


