from flask import Flask, render_template, request
from login import login

app= Flask(__name__)

sensores = {'Umidade':80, 'Temperatura':25, 'Luminosidade':100}

@app.route('/sensors')
def sensors():
    return render_template("sensors.html", sensores1=sensores)

app.register_blueprint(login, url_prefix='/')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
