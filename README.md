# AppPetCare
Escribir sobre el contexto de su solución
Las personas que aman a sus mascotas siempre buscarán maneras de cuidar a sus fieles compañeritos. En respuesta a esta necesidad, surge AppPetCare, una aplicación innovadora diseñada para proporcionar un conjunto completo de herramientas y servicios que faciliten la gestión del cuidado de las mascotas.

## Modelo Relacional
- Adjuntar modelo
Usuarios
- ID_Usuario (PK)
- Nombre
- Email
- Contraseña
- Dirección
- Teléfono

Mascotas
- ID_Mascota (PK)
- Nombre
- Tipo (Perro, Gato, Peces, Conejos)
- Raza
- Fecha_Nacimiento
- ID_Usuario (FK)

Citas
- ID_Cita (PK)
- Fecha
- Hora
- Tipo_Servicio (Veterinario, Grooming, etc.)
- ID_Mascota (FK)

Comentarios
- ID_Comentario (PK)
- ID_Articulo (FK)
- ID_Usuario (FK)
- Contenido
- Fecha_Publicación

Red_Social
- ID_Post (PK)
- ID_Usuario (FK)
- Contenido
- Fecha_Publicación


## Desarrollo de propuesta
- Escribir sobre la solución a realizar.
AppPetCare es una aplicación que permite la creación de un perfil personalizado para cada mascota, donde se registra su información de salud, historial médico, vacunas y notas importantes.
Los usuarios podrán programar y gestionar citas con veterinarios, envío de recordatorios automáticos para vacunas, tratamientos y visitas programadas. Una comunidad en línea donde los usuarios pueden compartir fotos, experiencias y consejos.
