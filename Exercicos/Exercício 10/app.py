from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensors')
def sensors():
    dicionario = {'Umidade':80, 'Temperatura':25, 'Luminosidade':100}
    return render_template("sensors.html", dicionario=dicionario)

@app.route('/actuators')
def actuators():
    dicionario = {'Servo Motor':'Ligado', 'Lampada':'Desligado'}
    return render_template('atuadores.html', dicionario=dicionario)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
