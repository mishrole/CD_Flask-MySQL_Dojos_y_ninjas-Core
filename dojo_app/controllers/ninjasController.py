from flask import Flask, render_template, request, redirect
from dojo_app import app
# from dojo_app.models. import Ninja
from dojo_app.models import dojoModel, ninjaModel

@app.route('/ninjas', methods=['GET'])
def form():
    dojos = dojoModel.Dojo.get_all()
    return render_template('ninja.html', dojos = dojos)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        "dojo": request.form["dojo"],
        "firstname": request.form["firstname"],
        "lastname": request.form["lastname"],
        "age": request.form["age"]
    }

    ninja = ninjaModel.Ninja.save(data)
    print(ninja)

    if ninja:
        return redirect(f'/dojos/{request.form["dojo"]}')
    else:
        return redirect('/dojos')
    