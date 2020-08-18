from flask import Flask, render_template

app = Flask(__name__)

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