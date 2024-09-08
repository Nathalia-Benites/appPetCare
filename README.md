# AppPetCare
A la hora de cuidar a nuestras mascotas debemos de considerar varios aspectos como alimentación, salud, baños y juegos. Pero tenemos a la tecnología como aliada para suministrar servicios que garanticen la calidad en los insumos. Es el caso de AppPetCare, es una iniciativa orientada a la creación de un programa dedicado a la venta de productos para el cuidado de mascotas domésticas, específicamente perros y gatos, facilitando al usuario su adquisición y brindándole un servicio al cliente excepcional. 


***Categorías:***

- **Alimentos:** Pepas, snacks y suplementos.
- **Juguetes:** Diversos clasificados por tamaño y tipo de mascota.
- **Ropa y Accesorios:** Ropa para diferentes tamaños, collares, correas, camas, casas, platos.
- **Salud y Cuidado:** Productos de higiene, vitaminas, pipetas, pastillas, pasta dental, cepillos, champús, cremas, arenas.
 
---
## Modelo Relacional
![modeloEntidadRelacion](https://github.com/user-attachments/assets/8a206c21-e6c6-458e-ad3e-cee124e69001)

-----
***Tablas Principales:***

|Tabla	| Descripción|
|-------|-------------|
| Cliente |Almacena la información básica de los usuarios, incluyendo nombre, dirección, correo electrónico, número de teléfono, ciudad, correo.|
| Categoria del Producto|	Define las diferentes categorías bajo las cuales se clasifican los productos, como juguetes, ropa, alimentos, y productos de higiene.|
|Productos |Contiene detalles específicos de cada producto, como nombre, descripción, precio, stock disponible, tamaño, color, y la categoría a la que pertenece.|
|Pedidos |Almacena la información de los pedidos realizados por los usuarios, incluyendo la fecha del pedido, estado (pendiente, enviado, entregado), monto total, dirección de envío, y el método de pago utilizado|
|Detalles del Pedido |Guarda los productos específicos incluidos en cada pedido, junto con la cantidad solicitada, precio unitario, y el monto total del detalle de pedido.|
|Métodos de Pago| Almacena la información de los métodos de pago asociados a cada usuario, como el número de tarjeta, fecha de vencimiento, y tipo de tarjeta (crédito/débito).|
| Mascota |Registra cada mascota asociada a un usuario específico, proporcionando detalles como nombre, especie, raza, fecha de nacimiento, y una referencia al usuario propietario.|
|Direccion_Envio|Almacena las direcciones de envío asociadas a los usuarios, incluyendo dirección, ciudad, estado/región, código postal, y país.|

------
## Desarrollo de propuesta
Para esta propuesta se considerará la automatización y gestión de los siguientes aspectos:

1. **Registro y Gestión de Usuarios:** Incluye la capacidad para registrar usuarios, gestionar direcciones de envío y métodos de pago, asegurando que cada cliente pueda administrar sus datos y opciones de pago.

2. **Administración de Productos:** Facilita el registro y manejo de productos en diferentes categorías, permitiendo un control sobre el inventario y la disponibilidad de cada artículo.

3. **Procesamiento de Pedidos:** Permite la creación y gestión de pedidos, incluyendo la adición y eliminación de productos en los pedidos, así como el cálculo del total con IVA y la generación de facturas detalladas.

4. **Seguridad en el Almacenamiento de Datos:** Implementa el almacenamiento seguro de los datos de las tarjetas de crédito mediante hashing, protegiendo así la información sensible de los usuarios.
----
  ***Beneficios esperados:***
-----------------------
- La automatización de los procesos de registro, pedido y gestión de productos mejora la eficiencia operativa y reduce el tiempo necesario para realizar estas tareas manualmente.

- El uso de hashing para almacenar datos de tarjetas de crédito garantiza que la información sensible de los usuarios esté protegida contra accesos no autorizados.

- La capacidad para gestionar el stock de productos en tiempo real permite un control más preciso y evita problemas de sobreventa o falta de stock.

- La implementación de una interfaz intuitiva para el manejo de pedidos y productos mejora la experiencia del usuario, haciendo que el proceso de compra sea más fluido y satisfactorio.

- La generación de facturas detalladas al finalizar un pedido asegura que los usuarios reciban un resumen claro de sus compras, incluyendo los productos adquiridos, el total a pagar y los impuestos aplicables.
