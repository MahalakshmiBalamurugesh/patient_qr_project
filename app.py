from flask import Flask, render_template, request
import random

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
     

    return f"""
    <h2>Registration Successful</h2>
    <p>Name: {name}</p>
    <p>Patient ID: {patient_id}</p>
    <p>PIN: {pin}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)