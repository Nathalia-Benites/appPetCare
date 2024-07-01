# AppPetCare
AppPetCare es una iniciativa orientada a la creación de una plataforma dedicada a la venta de productos para el cuidado de mascotas domésticas, especificamente perros y gatos. Tiene un menú de navegación que permite acceder rápidamente a la pantalla principal, categorías de productos, historial y estado de pedidos, perfil de usuario, notificaciones y soporte al cliente. AppPetCare mantiene a los usuarios informados sobre promociones, ofertas y actualizaciones de pedidos a través de notificaciones. 

---
***Categorías:***
- Alimentos: Pepas, snacks y suplementos.
- Juguetes: Diversos tipos de juguetes clasificados por tamaño y tipo de mascota.
- Ropa y Accesorios: Ropa para diferentes tamaños, collares y correas.
- Salud y Cuidado: Productos de higiene, vitaminas y productos para el cuidado dental.
---
## Modelo Relacional
![image](https://github.com/Nathalia-Benites/appPetCare/assets/167949641/baab40c1-d4dc-4170-960d-1dc1ee403253)


*SCRIPT SQL*

[Modelo Script](https://github.com/Nathalia-Benites/appPetCare/blob/main/Modelo%20relacional.sql)

***Tablas Principales:***

|Tabla	| Descripción
-               - 
| Usuarios	| Almacena información de los usuarios registrados, incluyendo nombre, correo electrónico, número de teléfono y datos de autenticación.
| Productos	Contiene detalles de todos los productos disponibles, como nombre, descripción, categoría, precio, tamaño, color y disponibilidad.
Pedidos	Registra cada pedido realizado por los usuarios, incluyendo detalles como fecha, estado (pendiente, enviado, entregado), productos asociados y dirección de envío.
Direcciones	Gestiona las direcciones de envío de los usuarios para cada pedido, incluyendo nombre del destinatario, dirección completa y datos de contacto.
Métodos de Pago	Almacena los métodos de pago asociados a cada usuario, como tarjetas de crédito, PayPal u otros métodos aceptados.
Reseñas y Valoraciones	Guarda las opiniones y calificaciones de los usuarios sobre los productos, junto con comentarios opcionales.
Configuraciones de Usuario	Administra las preferencias individuales de notificaciones y configuraciones de privacidad para cada usuario.



## Desarrollo de propuesta
Para esta propuesta se ha considerado los suguientes aspectos que se automatizará:

- Registro de usuarios: Sistema de registro y autenticación mediante correo electrónico y número de teléfono para padres y usuarios interesados en productos para perros y gatos.
  
- Gestión de Pedidos: Módulo para la realización, seguimiento y gestión de pedidos, incluyendo opciones de entrega y retiro en tienda. Cada producto incluye detalles como galería de imágenes, descripción, tamaños y colores disponibles, precios y reseñas de usuarios. Los productos pueden añadirse al carrito de compras con opciones para modificar cantidades y eliminar productos.
  
- Base de Datos Relacional: Implementación de una base de datos relacional que almacena y gestiona información detallada sobre productos, usuarios, pedidos, inventarios y transacciones.
  
- Interfaz de Administración: Desarrollo de un panel de control para la gestión de productos, categorías, precios, promociones y control de inventarios.
  
- Integración de Métodos de Pago: El proceso de compra permite seleccionar direcciones de envío y métodos de pago (tarjeta de crédito, PayPal, etc.) antes de confirmar el pedido. Los usuarios pueden seguir el estado de sus pedidos y revisar el historial de compras anteriores. 
  
- Soporte y Atención al Cliente: Implementación de un sistema automatizado de soporte al cliente que incluye opciones como chat en vivo, correo electrónico y atención telefónica para una respuesta rápida a consultas y problemas.




