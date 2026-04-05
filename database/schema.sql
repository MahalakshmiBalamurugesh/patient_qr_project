CREATE TABLE patients (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  age INT,
  blood_group VARCHAR(5),
  contact VARCHAR(15),
  pin VARCHAR(10),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE qr_codes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  patient_id INT,
  qr_token VARCHAR(255) UNIQUE
);

CREATE TABLE access_requests (
  id INT PRIMARY KEY AUTO_INCREMENT,
  patient_id INT,
  doctor_id INT,
  status VARCHAR(20)
);

CREATE TABLE doctors (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  hospital VARCHAR(100)
);