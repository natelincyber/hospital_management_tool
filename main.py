from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import redirect
from datetime import timedelta

SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
db = SQLAlchemy(app)

class PatientInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(20), default=False)
    gender = db.Column(db.String(20), nullable=False)
    medID = db.Column(db.Integer, nullable=False)
    cureTime = db.Column(db.Integer, nullable=False)
    doctorID = db.Column(db.Integer, nullable=False)
    field = db.Column(db.String(25), nullable=False)
    date_admitted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __str__(self):
        return 'PatientID:' + str(self.id)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/see_patients", methods=['GET', 'POST'])
def see_patients():
    if request.method == 'POST':
        patient_first = request.form['firstName']
        patient_last = request.form['lastName']
        patient_age = request.form['age']
        patient_state = request.form['state']
        patient_gender = request.form['gender']
        patient_medID = request.form['medID']
        patient_cureTime = request.form['cureTime']
        patient_doctorID = request.form['doctorID']
        patient_field = request.form['field']
        new_patient = PatientInfo(firstName=patient_first, lastName=patient_last, age=patient_age, state=patient_state, gender=patient_gender, medID=patient_medID, cureTime=patient_cureTime, doctorID=patient_doctorID, field=patient_field)        
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
        patient.firstName = request.form['firstName']
        patient.lastName = request.form['lastName']
        patient.age = request.form['age']
        patient.state = request.form['state']
        patient.gender = request.form['gender']
        patient.medID = request.form['medID']
        patient.cureTime = request.form['cureTime']
        patient.doctorID = request.form['doctorID']
        patient.field = request.form['field']
        new_patient = PatientInfo(firstName=patient_first, lastName=patient_last, age=patient_age, state=patient_state, gender=patient_gender, medID=patient_medID, cureTime=patient_cureTime, doctorID=patient_doctorID, field=patient_field)
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
        patient.firstName = request.form['firstName']
        patient.LastName = request.form['lastName']
        patient.age = request.form['age']
        patient.state = request.form['state']
        patient.gender = request.form['gender']
        patient.medID = request.form['medID'] 
        patient.cureTime = request.form['cureTime']
        patient.doctorID = request.form['doctorID']
        patient.field = request.form['field']      
        db.session.commit()
        return redirect('/see_patients') 
    else:
        return render_template('edit.html', patient=patient)  


@app.route('/about_hospitalhero')
def about():
    return render_template('about_hospitalhero.html')

@app.route('/new_patient_error/<int:id>', methods=['GET', 'POST'])
def new_patient_error(id):
    patient = PatientInfo.query.get_or_404(id)
    if request.method == 'POST':
        patient = PatientInfo.query.get_or_404(id)
        patient.firstName = request.form['firstName']
        patient.LastName = request.form['lastName']
        patient.age = request.form['age']
        patient.state = request.form['state']
        patient.gender = request.form['gender']
        patient.medID = request.form['medID'] 
        patient.cureTime = request.form['cureTime']
        patient.doctorID = request.form['doctorID']
        patient.field = request.form['field']      
        db.session.commit()
        return redirect('/see_patients') 
    else:
        return render_template('new_patient_error.html', patient=patient) 

if __name__ == '__main__': 
    app.run(debug=True)