-- Create Database if not exists
CREATE DATABASE IF NOT EXISTS hospital_db;
USE hospital_db;

-- 1. Users Table (Admin)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Insert Default Admin (Username: admin, Password: admin123)
INSERT INTO users (id, username, password) 
VALUES (1, 'admin', 'admin123')
ON DUPLICATE KEY UPDATE username=username;

-- 2. Patients Table
CREATE TABLE IF NOT EXISTS patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    emergency_contact VARCHAR(100) NOT NULL, -- Added Emergency Contact
    disease VARCHAR(150) NOT NULL
);

-- Insert Sample Patients
INSERT INTO patients (name, age, gender, phone, emergency_contact, disease) VALUES
('Ramesh Kumar', 45, 'Male', '9876543210', 'Suresh (Brother) - 9123456789', 'Malaria'),
('Anita Sharma', 32, 'Female', '8765432109', 'Vijay (Husband) - 8123456789', 'Viral Fever');

-- 3. Doctors Table
CREATE TABLE IF NOT EXISTS doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

-- Insert Sample Doctors
INSERT INTO doctors (name, specialization, phone) VALUES
('Amit Shah', 'Cardiologist', '9988776655'),
('Neha Verma', 'Pediatrician', '8877665544');

-- 4. Appointments Table
CREATE TABLE IF NOT EXISTS appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100) NOT NULL,
    doctor_name VARCHAR(100) NOT NULL,
    app_date DATETIME NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending'
);

-- Insert Sample Appointments
INSERT INTO appointments (patient_name, doctor_name, app_date, status) VALUES
('Ramesh Kumar', 'Amit Shah', '2026-07-05 10:30:00', 'Confirmed');

-- 5. Settings Table (For Hospital Name)
CREATE TABLE IF NOT EXISTS settings (
    id INT PRIMARY KEY,
    hospital_name VARCHAR(100) NOT NULL
);

INSERT INTO settings (id, hospital_name) 
VALUES (1, 'City Hospital')
ON DUPLICATE KEY UPDATE id=id;