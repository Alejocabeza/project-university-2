# Proyecto de la universidad (Como iniciarlo)

Este proyecto es un proyecto para la universidad, sin ningún fin de lucro. Es un proyecto dedicado a manejar y generar pdfs para proyectos arquitectónicos

## Base De Datos (proyecto_universidad)

Este proyecto consta actualmente de dos tablas en la base de datos, tenemos una tabla dedicada unicamente  a los usuarios, que es la tabla de usuarios. por defecto necesitaremos crear uno que sea un administrador. por lo que este sera el unico que crearemos directamente en la base de datos

### Tabla de Usuarios

Debes ejecutar esta sentencia sql para crear la tabla de usuarios

```sql
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        dni VARCHAR(40),
        role ENUM('admin', 'user', 'guest') NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL, 
        avatar VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        deleted_at TIMESTAMP NULL DEFAULT NULL
    );
```

para crear el usuario administrador, ejecuta esta sentencia

```sql
INSERT INTO users (name, dni, role, email, password, avatar)
VALUES ('Admin', '0011223344', 'admin', 'admin@gmail.com', '$2y$10$2iHXFO1BcJT9si.1laGbRObBaryVVrCza7sJsXLQaUT4.7aT5ewKS', NULL); 
```

| ID | Name | Email | DNI | Role | Password | Avatar |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Admin | <admin@ejemplo.com> | 0011223344 | admin | admin | NULL|

### Tabla de Sesiones

Debes ejecutar esta sentencia para crear la tabla de sesiones

```sql
CREATE TABLE user_session (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user INT,
    start_date DATETIME,
    end_date DATETIME,
    is_active BOOLEAN NOT NULL DEFAULT 1
);

ALTER TABLE user_session
ADD CONSTRAINT user_session_ibfk_1
FOREIGN KEY (user)
REFERENCES users(id)
ON DELETE CASCADE;
```

### Tabla de Clientes

Debes ejecutar esta sentencia para crear la tabla de clientes

```sql

CREATE TABLE address (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  location VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  city VARCHAR(100) NOT NULL,
  main_address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  deleted_at TIMESTAMP NULL DEFAULT NULL,
  created_by INT,
  updated_by INT
);

```
