CREATE TABLE patients (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  age INTEGER,
  blood_group TEXT,
  contact TEXT,
  pin TEXT
);

CREATE TABLE qr_codes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  patient_id INTEGER,
  qr_token TEXT UNIQUE
);

CREATE TABLE access_requests (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  patient_id INTEGER,
  doctor_id INTEGER,
  status TEXT
);

CREATE TABLE doctors (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  hospital TEXT
);

CREATE TABLE medical_records (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  patient_id INTEGER,
  doctor_id INTEGER,
  diagnosis TEXT,
  prescription TEXT,
  notes TEXT
);