# SNOWCENTER

## Descripción del Proyecto
Este proyecto es una página web de venta online dedicada a la comercialización de equipos de snowboard, accesorios de esquí y otros productos relacionados. La plataforma ha sido desarrollada utilizando Python 3.11.0 y Django 4.2, proporcionando una experiencia de usuario fluida y eficiente.

### Estado del Proyecto
El proyecto se encuentra en desarrollo activo. Se están implementando nuevas funcionalidades y mejoras para optimizar la experiencia del usuario y la gestión del inventario.

### Tecnologías Utilizadas
1. Lenguaje de Programación: Python 3.11.0
2. Framework: Django 4.2
3. Frontend: HTML, CSS, JavaScript 

## Instalación
Para instalar el proyecto en tu entorno local en Windows, sigue estos pasos:

A. Clona el repositorio:
git clone https://github.com/rgalant77/Proyecto_Final.git

B. Ejecuta las migraciones:

python manage.py migrate

C. Inicia el servidor de desarrollo:

python manage.py runserver

## Uso
Una vez que el servidor esté en funcionamiento, puedes acceder a la aplicación en tu navegador en http://127.0.0.1:8000/. Desde allí, los usuarios pueden registrarse, iniciar sesión y explorar los productos disponibles para la compra a traves de las diversas urls de nuestra pagina.

## Funcionalidades Clave
1. Botón de Búsqueda: Permite a los usuarios buscar productos específicos y agregar información relacionada.
2. Navegación por Categorías: La barra de navegación (navbar) incluye tres solapas principales:

   A. Snowboard: Accede a todos los productos relacionados con snowboard.

   B. Esquí: Explora los equipos y accesorios para esquí.

   C.Accesorios: Encuentra una variedad de accesorios útiles para ambos deportes.

   D.Nosotros: nuestra misión es ofrecerte los mejores productos para que disfrutes al máximo de tus actividades en la montaña.

   E.ListaSnowboard: Encuentra toda la variedad de nuestros catálogo de equipos de snowboard para nuestro deportes favorito.

   F.CrearSnowboard: Aqui solo podran acceder de forma directa los superusuarios para modificar la variedad de nuestros catálogo de equipos de snowboard.

3. Gestión de Usuarios:
   - Iniciar Sesión: Los usuarios pueden acceder a su cuenta.
   - Crear Cuenta: Permite a nuevos usuarios registrarse en la plataforma.
   - Cerrar Sesión: Opción para que los usuarios cierren su sesión activa.
   - Editar Usuario: Los usuarios autenticados pueden editar su perfil, incluyendo la opción de subir un avatar.

4. Gestión de Productos:
   - Los superusuarios tienen la capacidad de agregar nuevos productos al inventario, asegurando que solo los usuarios con privilegios adecuados puedan realizar cambios en la base de datos.


## Contacto
Para preguntas o más información sobre este proyecto, puedes contactarme a través de mi correo electrónico: [dario@galant.com]. 