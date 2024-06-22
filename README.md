# AppPetCare
Escribir sobre el contexto de su solución.

AppPetCare es una aplicación dedicada al cuidado de perros y gatos que permite al usuario comprar en línea alimentos, juguetes, ropa, accesorios y productos de salud para su mascota. Incluye funciones de registro e inicio de sesión. Su menú de navegación facilita el acceso a categorías de productos, historial y estado de pedidos, perfil de usuario con opciones de dirección y formas de pago, notificaciones de ofertas y promociones, una sección de preguntas frecuentes y soporte mediante chat. Brinda un catálogo con filtros de búsqueda, descripciones de los productos con opciones de compra y seguimiento de pedidos hasta la entrega.

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
![image](https://github.com/Nathalia-Benites/appPetCare/assets/167949641/d20f9920-1824-4ffd-85ec-8c76f4e1b4c2)
![image](https://github.com/Nathalia-Benites/appPetCare/assets/167949641/cfedab2b-eee1-47c0-8e29-0f252a98d2b5)
![image](https://github.com/Nathalia-Benites/appPetCare/assets/167949641/8765e0b5-2f18-4ba7-9f74-3940688be18f)
![image](https://github.com/Nathalia-Benites/appPetCare/assets/167949641/d71e42d5-311f-4f7b-a798-1e424794ead0)
![image](https://github.com/Nathalia-Benites/appPetCare/assets/167949641/c2ef68eb-7934-4ea1-a909-21773ae977c2)


## Desarrollo de propuesta
- Escribir sobre la solución a realizar.

Se va a desarrollar la aplicación de la siguiente manera: 

*1. Pantalla de Inicio y Registro*

- Recibir a los usuarios que abran la aplicación por primera vez, con un mensaje de bienvenida y se presentará un breve tutorial interactivo que guíen a los usuarios sobre cómo navegar y utilizar las características clave de la aplicación.
- Implementar un formulario de registro que solicite al usuario su correo electrónico y número de teléfono. Validar estos datos.
- Permitir a los usuarios iniciar sesión con sus credenciales existentes (correo electrónico y contraseña).
- Implementar un proceso seguro para que los usuarios puedan restablecer su contraseña en caso de olvido, utilizando un enlace enviado por correo electrónico o un código de verificación SMS.
  
*2. Menú de Navegación*

- Inicio: Dirigir a los usuarios a la pantalla principal de la aplicación donde podrán acceder a todas las funcionalidades principales y categorías de productos.
- Productos: Listado completo de todos los productos disponibles para perros y gatos, organizados por categorías.
- Pedidos: Acceso al historial de pedidos pasados y ver el estado actual de los pedidos pendientes.
- Perfil: Información personal del usuario, direcciones de envío guardadas y métodos de pago configurados.
- Notificaciones: Alertas sobre ofertas, promociones y actualizaciones importantes relacionadas con los pedidos.
- Chat: Integrar un sistema de soporte al cliente en tiempo real donde los usuarios puedan realizar consultas y recibir asistencia directa.
  
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
- Métodos de pago
  
*8. Notificaciones y Promociones*

- Alertas sobre descuentos y promociones.
- Notificaciones sobre el estado del pedido.

*9. Centro de Ayuda*

- Respuestas a preguntas frecuentes.
- Contacto con Soporte en Chat en vivo, correo electrónico y número de teléfono.

Cómo usarías la apliacación:
1. Abres la aplicación y te registras con tu correo.
2. Navegas a la categoría de "Ropa para Perros".
3. Filtras por tamaño y añades un abrigo al carrito.
4. Vas al carrito, seleccionas tu dirección de envío y método de pago.
5. Confirmas el pedido y recibes notificaciones sobre el estado del mismo.


