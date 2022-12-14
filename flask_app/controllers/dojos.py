from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect ('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", return_dojos=dojos)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect ('/dojos')

@app.route('/dojo/<int:id>')
def dojo_show(id):
    data={
        "id": id
    }
    return render_template('dojos.html', dojo=Dojo.get_dojo_with_ninjas(data))
    




