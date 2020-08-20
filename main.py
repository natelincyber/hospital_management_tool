from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import redirect

SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
db = SQLAlchemy(app)

class PatientInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Boolean, default=False)
    date_admitted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __str__(self):
        return 'PatientID:' + str(self.id)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_patient")
def add_patient():
    return render_template("add_patient.html")

@app.route("/see_patients", methods=['GET', 'POST'])
def see_patients():
    if request.method == 'POST':
        patient_name = request.form['name']
        patient_age = request.form['age']
        patient_state = request.form['state']
        new_patient = PatientInfo(name=patient_name, age=patient_age, state=patient_state)
        db.session.add(new_patient)
        db.session.commit()
        return redirect('/see_patients')
    else:
        all_patients = PatientInfo.query.order_by(PatientInfo.date_admitted).all()
        return render_template('see_patients.html', see_patients=all_patients)

@app.route("/see_patients/new_patient_form")
def addPatientForm():
    if request.method == 'POST':
        patient = PatientInfo.query.get_or_404(id)
        patient.name = request.form['name']
        patient.age = request.form['age']
        patient.state = request.form['state']
        new_patient = PatientInfo(name=patient_name, age=patient_age, state=patient_state)
        db.session.add(new_patient)
        db.session.commit()
        return redirect('/see_patients') 
    else:
        return render_template('new_patient_form.html')

@app.route('/see_patients/delete/<int:id>')
def delete(id):
    patient = PatientInfo.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect('/see_patients')

@app.route('/see_patients/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    patient = PatientInfo.query.get_or_404(id)
    if request.method == 'POST':
        patient = PatientInfo.query.get_or_404(id)
        patient.name = request.form['name']
        patient.age = request.form['age']
        patient.state = request.form['state']
        db.session.commit()
        return redirect('/see_patients') 
    else:
        return render_template('edit.html', patient=patient)  

@app.route('/about_hospitalhero')
def about():
    return render_template('about_hospitalhero.html')


if __name__ == '__main__': 
    app.run(debug=True)