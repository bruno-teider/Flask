from flask import Blueprint, request, render_template, redirect, url_for

sensor = Blueprint("sensors", __name__, template_folder="templates")

sensores = {
    'Umidade':'80', 
    'Temperatura':'25', 
    'Luminosidade':'100'
}

@sensor.route('/sensors')
def sensors():
    global sensores
    return render_template("sensors.html", sensores=sensores)

@sensor.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@sensor.route('/add_sensor', methods=['GET','POST'])
def add_sensors():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
        valor = request.form['valor']
    else:
        sensor = request.args.get('sensor', None)
        valor = request.args.get('valor', None)
    sensores[sensor] = valor
    return render_template("sensors.html", sensores=sensores)

@sensor.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", sensores=sensores)

@sensor.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensores.pop(sensor)
    return render_template("sensors.html", sensores=sensores)