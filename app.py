from flask import Flask, render_template, request
import random
import qrcode
import os
import sqlite3

conn = sqlite3.connect('patients.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    blood_group TEXT,
    contact TEXT,
    pin TEXT
)
''')

conn.commit()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    age = request.form['age']
    blood_group = request.form['blood_group']
    contact = request.form['contact']
    pin = request.form['pin']

    patient_id = cursor.lastrowid

    query = "INSERT INTO patients (name, age, blood_group, contact, pin) VALUES (?, ?, ?, ?, ?)"
    values = (name, age, blood_group, contact, pin)
    cursor.execute(query, values)
    conn.commit()
    patient_id = cursor.lastrowid

    # Generate QR
    qr_data = f"Patient ID: {patient_id}"
    qr = qrcode.make(qr_data)
    # # Save QR image
    qr_path = f"static/{patient_id}.png"
    qr.save(qr_path)
    
    return render_template("success.html",
                       name=name,
                       patient_id=patient_id,
                       pin=pin,
                       qr_image=qr_path)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        pin = request.form['pin']

        query = "SELECT * FROM patients WHERE id=? AND pin=?"
        cursor.execute(query, (patient_id, pin))
        result = cursor.fetchone()

        if result:
            return "Login successful ✅"
        else:
            return "Invalid ID or PIN ❌"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)