# AppPetCare
Escribir sobre el contexto de su solución.

AppPetCare es una iniciativa orientada a la creación de una plataforma dedicada a la venta de productos para el cuidado de mascotas domésticas, especificamente perros y gatos. Tiene un menú de navegación que permite acceder rápidamente a la pantalla principal, categorías de productos, historial y estado de pedidos, perfil de usuario, notificaciones y soporte al cliente. AppPetCare mantiene a los usuarios informados sobre promociones, ofertas y actualizaciones de pedidos a través de notificaciones. 

---
***Categorías:***
- Alimentos: Pepas, snacks y suplementos.
- Juguetes: Diversos tipos de juguetes clasificados por tamaño y tipo de mascota.
- Ropa y Accesorios: Ropa para diferentes tamaños, collares y correas.
- Salud y Cuidado: Productos de higiene, vitaminas y productos para el cuidado dental.
---
## Modelo Relacional
- Adjuntar modelo
  
*Usuarios (Usuarios)*

- usuario_id (PK)
- correo 
- contraseña
- nombre
- telfono
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

*SCRIPT SQL*

[Modelo Script](https://github.com/Nathalia-Benites/appPetCare/blob/main/Modelo%20relacional.sql)



## Desarrollo de propuesta
- Escribir sobre la solución a realizar.

Para esta propuesta se ha considerado los suguientes aspectos que se automatizará:

- Registro de usuarios: Sistema de registro y autenticación mediante correo electrónico y número de teléfono para padres y usuarios interesados en productos para perros y gatos.
  
- Gestión de Pedidos: Módulo para la realización, seguimiento y gestión de pedidos, incluyendo opciones de entrega y retiro en tienda. Cada producto incluye detalles como galería de imágenes, descripción, tamaños y colores disponibles, precios y reseñas de usuarios. Los productos pueden añadirse al carrito de compras con opciones para modificar cantidades y eliminar productos.
  
- Base de Datos Relacional: Implementación de una base de datos relacional que almacena y gestiona información detallada sobre productos, usuarios, pedidos, inventarios y transacciones.
  
- Interfaz de Administración: Desarrollo de un panel de control para la gestión de productos, categorías, precios, promociones y control de inventarios.
  
- Integración de Métodos de Pago: El proceso de compra permite seleccionar direcciones de envío y métodos de pago (tarjeta de crédito, PayPal, etc.) antes de confirmar el pedido. Los usuarios pueden seguir el estado de sus pedidos y revisar el historial de compras anteriores. 
  
- Soporte y Atención al Cliente: Implementación de un sistema automatizado de soporte al cliente que incluye opciones como chat en vivo, correo electrónico y atención telefónica para una respuesta rápida a consultas y problemas.


Cómo usarías la aplicación:
1. Abres la aplicación y te registras con tu correo.
2. Navegas a la categoría de "Ropa para Perros".
3. Filtras por tamaño y añades un abrigo al carrito.
4. Vas al carrito, seleccionas tu dirección de envío y método de pago.
5. Confirmas el pedido y recibes notificaciones sobre el estado del mismo.


