CREATE DATABASE IF NOT EXISTS `project_university`
CHARACTER SET utf8
COLLATE utf8_general_ci;


CREATE TABLE `project_university`.`user` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100),
  `dni` VARCHAR(20),
  `role` ENUM('admin', 'user') DEFAULT 'user',
  `email` VARCHAR(100),
  `password` VARCHAR(100), `avatar` VARCHAR(255),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` TIMESTAMP NULL
);

CREATE TABLE `project_university`.`user_session` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `user` INT,
  `startDate` TIMESTAMP,
  `endDate` TIMESTAMP,
  `is_active` BOOLEAN DEFAULT TRUE,
  FOREIGN KEY (`user`) REFERENCES `user` (`id`)
);

CREATE TABLE `project_university`.`address` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100) UNIQUE,
  `city` VARCHAR(100),
  `country` VARCHAR(100),
  `state` VARCHAR(100),
  `street` VARCHAR(100),
  `postal_code` VARCHAR(100),
  `location` VARCHAR(100),
  `department` VARCHAR(100),
  `main_address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` TIMESTAMP NULL,
  `created_by` INT,
  `updated_by` INT,
  FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`updated_by`) REFERENCES `user` (`id`)
);

CREATE TABLE `project_university`.`client_office` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100) UNIQUE,
  `email` VARCHAR(100) UNIQUE,
  `phone` VARCHAR(40),
  `address` INT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` TIMESTAMP NULL,
  `created_by` INT,
  `updated_by` INT,
  FOREIGN KEY (`address`) REFERENCES `address` (`id`),
  FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`updated_by`) REFERENCES `user` (`id`)
);

CREATE TABLE `project_university`.`client` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100) UNIQUE,
  `dni` VARCHAR(20) UNIQUE,
  `email` VARCHAR(100) UNIQUE,
  `phone` VARCHAR(40),
  `type` ENUM('person', 'company', 'government') DEFAULT 'person',
  `address` INT,
  `client_office` INT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` TIMESTAMP NULL,
  `created_by` INT,
  `updated_by` INT,
  FOREIGN KEY (`address`) REFERENCES `address` (`id`),
  FOREIGN KEY (`client_office`) REFERENCES `client_office` (`id`),
  FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`updated_by`) REFERENCES `user` (`id`)
);

CREATE TABLE `project_university`.`branch` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100),
  `rif` VARCHAR(20) UNIQUE,
  `email` VARCHAR(100) UNIQUE,
  `phone` VARCHAR(40),
  `address` INT,
  `client` INT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` TIMESTAMP NULL,
  `created_by` INT,
  `updated_by` INT,
  FOREIGN KEY (`address`) REFERENCES `address` (`id`),
  FOREIGN KEY (`client`) REFERENCES `client` (`id`),
  FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`updated_by`) REFERENCES `user` (`id`)
);

CREATE TABLE `project_university`.`employee` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `firstname` VARCHAR(100),
  `lastname` VARCHAR(100),
  `fullname` VARCHAR(100) UNIQUE,
  `dni` VARCHAR(20) UNIQUE,
  `email` VARCHAR(100) UNIQUE,
  `phone` VARCHAR(40),
  `created_by` INT,
  `updated_by` INT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` TIMESTAMP NULL,
  FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`updated_by`) REFERENCES `user` (`id`)
);

CREATE TABLE `project_university`.`project` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100) UNIQUE,
  `description` VARCHAR(255),
  `foreman` INT,
  `client` INT,
  `address` INT,
  `start_date` DATE,
  `end_date` DATE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` TIMESTAMP NULL,
  `created_by` INT,
  `updated_by` INT,
  FOREIGN KEY (`foreman`) REFERENCES `employee` (`id`),
  FOREIGN KEY (`client`) REFERENCES `client` (`id`),
  FOREIGN KEY (`address`) REFERENCES `address` (`id`),
  FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`updated_by`) REFERENCES `user` (`id`)
);

CREATE TABLE `project_university`.`task` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100),
  `description` TEXT,
  `start_date` DATETIME,
  `end_date` DATETIME,
  `project` INT,
  `employee` INT,
  `status` INT DEFAULT 1,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` TIMESTAMP NULL,
  `created_by` INT,
  `updated_by` INT,
  FOREIGN KEY (`project`) REFERENCES `project` (`id`),
  FOREIGN KEY (`employee`) REFERENCES `employee` (`id`),
  FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`updated_by`) REFERENCES `user` (`id`)
);

CREATE TABLE `project_university`.`report` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100),
  `path` VARCHAR(255),
  `project` INT,
  `report_type` INT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` TIMESTAMP NULL,
  `created_by` INT,
  `updated_by` INT,
  FOREIGN KEY (`project`) REFERENCES `project` (`id`),
  FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`updated_by`) REFERENCES `user` (`id`)
);

INSERT INTO `project_university`.`user` (name, dni, role, email, password, avatar)
VALUES ('Admin', '0011223344', 'admin', 'admin@gmail.com', '$2y$10$2iHXFO1BcJT9si.1laGbRObBaryVVrCza7sJsXLQaUT4.7aT5ewKS', NULL);
