from flask import Flask, render_template, request
import random
import qrcode
import os

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

    patient_id = "P" + str(random.randint(1000, 9999))
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

if __name__ == '__main__':
    app.run(debug=True)