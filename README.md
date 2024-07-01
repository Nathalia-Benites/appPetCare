# AppPetCare
AppPetCare es una iniciativa orientada a la creación de una plataforma dedicada a la venta de productos para el cuidado de mascotas domésticas, específicamente perros y gatos, facilitando al usuario la adquisición de estos y brindándole un servicio al cliente excepcional.

Tiene un menú de navegación que permite acceder rápidamente a la pantalla principal, categorías de productos, historial y estado de pedidos, perfil de usuario, notificaciones y soporte. AppPetCare mantiene a los usuarios informados sobre promociones, ofertas y actualizaciones de pedidos a través de notificaciones. 

---
***Categorías:***

- **Alimentos:** Pepas, snacks y suplementos.
- **Juguetes:** Diversos tipos de juguetes clasificados por tamaño y tipo de mascota.
- **Ropa y Accesorios:** Ropa para diferentes tamaños, collares y correas.
- **Salud y Cuidado:** Productos de higiene, vitaminas y productos para el cuidado dental.
---
## Modelo Relacional
![image](https://github.com/Nathalia-Benites/appPetCare/assets/167949641/baab40c1-d4dc-4170-960d-1dc1ee403253)

____
**SCRIPT SQL**

[Modelo Script](https://github.com/Nathalia-Benites/appPetCare/blob/main/Modelo%20relacional.sql)

***Tablas Principales:***

|Tabla	| Descripción|
|-------|-------------|
| Usuarios |Almacena información básica de los usuarios que incluye nombre, correo electrónico, contraseña, teléfono y fecha de creación.|
| Direcciones | Permite a cada usuario gestionar múltiples direcciones de envío asociadas a su cuenta.|
| CategoriasProductos| Define las diferentes categorías bajo las cuales se clasifican los productos.|
|Productos |Contiene detalles específicos de cada producto como nombre, descripción, precio, stock, tamaño, color y la categoría a la que pertenece.|
|CarritosCompras |Registra los carritos activos de cada usuario mientras navegan y agregan productos antes de realizar un pedido.|
|ProductosCarrito |Relaciona los productos específicos que están en cada carrito de compras junto con la cantidad seleccionada por el usuario.|
|Pedidos |Almacena información sobre los pedidos realizados por los usuarios, incluyendo detalles como fecha, estado, monto total, dirección de envío y método de pago.|
|DetallesPedido |Guarda los productos específicos incluidos en cada pedido, junto con la cantidad y el precio en el momento de la compra.|
|OpinionesProductos| Permite a los usuarios dejar opiniones y calificaciones sobre los productos que han comprado.|
|Notificaciones| Registra las notificaciones enviadas a los usuarios, como alertas de pedidos, promociones u otros mensajes importantes.|
|MensajesChat |Gestiona los mensajes enviados por los usuarios a través del sistema de soporte al cliente.|
|MétodosPago| Almacena la información de los métodos de pago asociados a cada usuario, como números de tarjeta y detalles de vencimiento.|



## Desarrollo de propuesta
Para esta propuesta se ha considerado los suguientes aspectos que se automatizará:

- **Registro de usuarios:** Sistema de registro y autenticación mediante correo electrónico y número de teléfono para padres y usuarios interesados en productos para perros y gatos.
  
- **Gestión de Pedidos:** Módulo para la realización, seguimiento y gestión de pedidos, incluyendo opciones de entrega y retiro del mismo. Cada producto incluye detalles como galería de imágenes, descripción, tamaños y colores disponibles, precios y reseñas de usuarios. Los productos pueden añadirse al carrito de compras con opciones para modificar cantidades y eliminar productos.
  
- **Base de Datos Relacional:** Implementación de una base de datos relacional que almacena y gestiona información detallada sobre con los usuarios, productos, pedidos, opiniones, notificaciones, métodos de pago y más.
  
- **Interfaz de Administración:** Desarrollo de un panel de control para la gestión de productos, categorías, precios, promociones y stock.
  
- **Integración de Métodos de Pago:** El proceso de compra permite seleccionar direcciones de envío y métodos de pago (tarjeta de crédito, PayPal, etc.) antes de confirmar el pedido. Los usuarios pueden seguir el estado de sus pedidos y revisar el historial de compras anteriores. 
  
- **Soporte y Atención al Cliente:** Implementación de un sistema automatizado de soporte al cliente que incluye opciones como chat en vivo, correo electrónico y atención telefónica para una respuesta rápida a consultas y problemas.
----
  ***Beneficios esperados:***
-----------------------
Se espera que AppPetCare:
- Transforme la manera en que los dueños de mascotas acceden y adquieren productos para sus mascotas. La aplicación busca ofrecer una experiencia de compra conveniente, permitiendo a los usuarios realizar pedidos desde cualquier lugar y en cualquier momento a través de una plataforma. 
- Optimice la gestión de inventarios y pedidos mediante tecnologías avanzadas, lo que reducirá los tiempos de espera y mejorará la disponibilidad de productos. 
- En términos de servicio al cliente, proporcione soporte rápido y personalizado, asegurando una experiencia de usuario satisfactoria y segura. 
