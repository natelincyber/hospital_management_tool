from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import redirect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
db = SQLAlchemy(app)
class PatientInfo(db.Model):
    id = db.Column(db.integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.integer(3), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'PatientID:' + str(self.id)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_patient")
def add_patient():
    return render_template("add_patient.html")

@app.route("/see_patients")
def see_patient():
    return render_template("see_patients.html")

if __name__ == '__main__':
    app.run(debug=True)