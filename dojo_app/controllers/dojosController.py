from flask import Flask, render_template, request, redirect
from dojo_app import app
from dojo_app.models import dojoModel

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return render_template('404.html'), 404

@app.route('/', methods=['GET'])
def index():
    return redirect('/dojos')

@app.route('/dojos', methods=['GET'])
def dojos():
    dojos = dojoModel.Dojo.get_all()
    return render_template('dojo.html', dojos = dojos)

@app.route('/dojos/<int:id>', methods=['GET'])
def dojo_ninjas(id):
    data = {
        "dojoId": id
    }

    dojo = dojoModel.Dojo.get_dojos_with_ninjas(data)
    return render_template('show.html', dojo = dojo)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        "name": request.form["name"],
    }

    dojoModel.Dojo.save(data)
    return redirect('/dojos')