from flask import render_template, redirect, session, flash, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos=dojo.Dojo.get_all())

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')


@app.route('/destroy_ninja/<int:id>/<int:dojo_id>')
def destroy_ninja(id,dojo_id):
    data={
        "id": id
    }
    ninja.Ninja.destroyNinja(data)
    return redirect(f'/dojo/{dojo_id}')

@app.route('/edit_ninja/<int:id>')
def edit_ninja(id):
    data ={
        "id": id
    }
    return render_template("edit.html", ninja=ninja.Ninja.getNinja(data))

@app.route('/update_ninja', methods=["POST"])
def update_ninja():
    ninja.Ninja.updateNinja(request.form)
    return redirect('/')