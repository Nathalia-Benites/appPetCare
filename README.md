# AppPetCare
***Introducción***
----
AppPetCare es una aplicación que ayuda a las clínicas veterinarias a gestionar a sus clientes, mascotas, productos, ventas, citas y pedidos. Es fácil de usar y te ayudará a mantener todo en orden

----

***Contexto del Problema***
---
En una clínica veterinaria, hay mucha información que manejar: datos de los clientes, sus mascotas, productos en inventario, ventas realizadas, citas para consultas y pedidos de productos. Si todo se hace a mano o con sistemas separados, puede ser confuso y propenso a errores. AppPetCare resuelve esto al juntar toda esta información en un solo lugar.

***Análisis de Requerimientos***
Aquí están las cosas que AppPetCare necesita hacer:

- **Gestionar Clientes:** Añadir, actualizar, eliminar y ver los datos de los clientes.
- **Gestionar Mascotas:** Mantener información sobre las mascotas, como su nombre, especie, raza y edad.
- **Gestionar Productos:** Registrar y gestionar los productos que se venden en la clínica.

    **Categorías de productos:**

    - **Alimentos:** Pepas, snacks y suplementos.
    - **Juguetes:** Diversos clasificados por tamaño y tipo de mascota.
    - **Ropa y Accesorios:** Ropa para diferentes tamaños, collares, correas, camas, casas, platos.
    - **Salud y Cuidado:** Productos de higiene, vitaminas, pipetas, pastillas, pasta dental, cepillos, champús, cremas, arenas.
    
- **Gestionar Ventas:** Registrar, mostrar y eliminar las ventas de productos.
- **Gestionar Citas:** Programar, ver y cancelar citas para las mascotas.
- **Gestionar Pedidos:** Registrar, mostrar y eliminar los pedidos de productos realizados por los clientes. 

---
## ***Modelo Relacional***
![modeloEntidadRelacion](https://github.com/user-attachments/assets/8a206c21-e6c6-458e-ad3e-cee124e69001)

-----
***Diseño del Sistema***
---

**Programa con Acceso a Datos**

La aplicación está escrita en Python y usa MySQL para almacenar la información. Aquí está cómo funciona:

- Conexión a la Base de Datos: Al iniciar la aplicación, se conecta a la base de datos MySQL. Cuando terminas, se cierra la conexión.
- Menú Principal: Muestra opciones para gestionar Clientes, Mascotas, Productos, Ventas, Citas y Pedidos.
- Gestión de Datos: Cada sección te permite registrar nuevos datos, ver los datos existentes, y actualizar o eliminar datos cuando sea necesario.

***Guía de Uso***

- Iniciar el Programa: Ejecuta el archivo principal. La aplicación se conectará a la base de datos y mostrará el menú principal.
- Seleccionar una Opción del Menú: Elige qué parte de la aplicación quieres usar: Clientes, Mascotas, Productos, Ventas, Citas o Pedidos.

***Operaciones:***

- Registrar: Introduce la información para añadir nuevos registros.
- Mostrar: Ve la información que ya está registrada.
- Actualizar/Eliminar: Modifica o borra registros existentes.
- Salir: Elige "Salir" del menú principal para cerrar la aplicación y desconectar la base de datos.

