# Proyecto de la universidad (Como iniciarlo)

Este proyecto es un proyecto para la universidad, sin ningún fin de lucro. Es un proyecto dedicado a manejar y generar pdfs para proyectos arquitectónicos

## Instalación de Dependencias

para instalar las dependencias es necesario activar el entorno virtual del proyecto, a menos que quiera instalar todo de forma global (esto es para Windows), haga click [aquí](https://docs.python.org/es/3/library/venv.html) para abrir la documentación de los entorno virtuales en python. En este caso, se activará el entorno virtual de la carpeta de proyecto.

para instalar las dependencias, si estas usando un entorno virtual, puedes usar el siguiente comando:

```bash
pip install -r requirements.txt
```

si no estas usando un entorno virtual, puedes instalar las dependencias de forma manual, usando como guia el archivo `requirements.txt`.

## Base De Datos (proyecto_universidad)

Para este proyecto es vital tener XAMPP(Cross-Platform, Apache, MariaDB, PHP, y Perl) o un entorno LAMP(Linux, Apache, Mysql, PHP) para iniciar el proyecto, haga click [aquí](https://www.apachefriends.org/es/download.html) para descargar XAMPP, Para instalar lamp en su maquina con linux haga click [aquí](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04-es)

Este proyecto tiene un archivo `.env` para manejar las variables de entorno, esto incluye las credenciales de la base de datos. para usarlas, puede crear este archivo y copiar el contenido del archivo `.env.example` a este. posteriormente en su manejado de base de datos, puede crear una base de datos y una tabla. puede usar las sentencias que se encuentra en el archivo `database.sql` que se encuentra en la raíz del proyecto.

Si ejecuta la sentencia que esta en el archivo `database.sql` esto le va a crear la base de datos y las tablas ademas le va a agregar un usuario administrador para iniciar sesión.
