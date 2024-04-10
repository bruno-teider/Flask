from flask import Blueprint, request, render_template, redirect, url_for

actuators = Blueprint("actuators", __name__, template_folder="templates")

atuadores = {
    'Lampada':'Ligado'
}

@actuators.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@actuators.route('/add_actuator', methods=['GET','POST'])
def add_actuator():
    global atuadores
    if request.method == 'POST':
        actuator = request.form['actuator']
        valor = request.form['valor']
    else:
        actuator = request.args.get('actuator', None)
        valor = request.args.get('valor', None)
    atuadores[actuator] = valor
    return render_template("actuator.html", atuadores=atuadores)

@actuators.route('/actuators')
def actuator_list():
    global atuadores
    return render_template("actuator.html", atuadores=atuadores)

@actuators.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", atuadores=atuadores)

@actuators.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global atuadores
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    atuadores.pop(actuator)
    return render_template("actuator.html", atuadores=atuadores)