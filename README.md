# Proyecto de la universidad (Como iniciarlo)

Este proyecto es un proyecto para la universidad, sin ningún fin de lucro. Es un proyecto dedicado a manejar y generar pdfs para proyectos arquitectónicos

## Base De Datos (proyecto_universidad)

Este proyecto consta actualmente de dos tablas en la base de datos, tenemos una tabla dedicada unicamente  a los usuarios, que es la tabla de usuarios. por defecto necesitaremos crear uno que sea un administrador. por lo que este sera el unico que crearemos directamente en la base de datos

### Tabla de Usuarios

Debes ejecutar esta sentencia sql para crear la tabla de usuarios

```sql
    CREATE TABLE usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        cedula VARCHAR(40),
        rol ENUM('admin', 'user', 'guest') NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL, avatar VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        deleted_at TIMESTAMP NULL DEFAULT NULL
    );
```

para crear el usuario administrador, ejecuta esta sentencia

```sql
INSERT INTO usuarios (nombre, cedula, rol, email, password, avatar)
VALUES ('Admin', '0011223344', 'admin', 'admin@ejemplo.com', '$2y$10$2iHXFO1BcJT9si.1laGbRObBaryVVrCza7sJsXLQaUT4.7aT5ewKS', NULL);
```

| ID | Nombre | Email | Cedula | Rol | Contraseña | Avatar |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Admin | <admin@ejemplo.com> | 0011223344 | admin | admin | NULL|

### Tabla de Sesiones

Debes ejecutar esta sentencia para crear la tabla de sesiones

```sql
CREATE TABLE sesiones_de_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    fecha_y_hora_de_inicio DATETIME,
    fecha_y_hora_finalizacion DATETIME,
    estado BOOLEAN NOT NULL DEFAULT 1,
);

ALTER TABLE sesiones_de_usuarios
ADD CONSTRAINT sesiones_de_usuarios_ibfk_1
FOREIGN KEY (usuario_id)
REFERENCES usuarios(id)
ON DELETE CASCADE;
```
