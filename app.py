from flask import Flask, render_template, request
import sqlite3
import qrcode
import uuid
import os
conn = sqlite3.connect('patients.db', check_same_thread=False)
cursor = conn.cursor()
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('register.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        blood_group = request.form['blood']
        contact = request.form['contact']
        pin = request.form['pin']
        

    # Save patient
    cursor.execute(
        "INSERT INTO patients (name, age, blood_group, contact, pin) VALUES (?, ?, ?, ?, ?)",
        (name, age, blood_group, contact, pin)
    )
    conn.commit()

    patient_id = cursor.lastrowid

    # Generate QR token
    qr_token = str(uuid.uuid4())

    # Save QR token
    cursor.execute(
        "INSERT INTO qr_codes (patient_id, qr_token) VALUES (?, ?)",
        (patient_id, qr_token)
    )
    conn.commit()

    # Generate QR image
    qr = qrcode.make(qr_token)

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

        cursor.execute(
            "SELECT * FROM patients WHERE id=? AND pin=?",
            (patient_id, pin)
        )
        result = cursor.fetchone()

        if result:
            return render_template("success.html",
                                   name=result[1],
                                   patient_id=result[0],
                                   pin=result[5],
                                   qr_image=f"static/{result[0]}.png")
        else:
            return "Invalid ID or PIN ❌"

    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)