from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    comodos = {'/quarto':'Quarto', '/banheiro':'Banheiro'}
    return render_template('index.html', comodos=comodos)

@app.route('/quarto')
def quarto():
    opcoes = {'Sensor de Luminosidade':'/quarto/luminosidade', 'Interruptor':'/quarto/interruptor'}
    return render_template('quarto.html', opcoes=opcoes)

@app.route('/quarto/luminosidade')
def luminosidade():
    dicionario = {'Luminosidade':60}
    return render_template('luminosidade.html', dicionario=dicionario)

@app.route('/quarto/interruptor')
def interruptor():
    dicionario = {'Interruptor':'Desligado'}
    return render_template('interruptor.html', dicionario=dicionario)

@app.route('/banheiro')
def banheiro():
    opcoes = {'Sensor Umidade':'/banheiro/umidade', 'Lampada Inteligente':'/banheiro/lampada'}
    return render_template('banheiro.html', opcoes=opcoes)

@app.route('/banheiro/umidade')
def umidade():
    dicionario = {'Umidade':60}
    return render_template('umidade.html', dicionario=dicionario)

@app.route('/banheiro/lampada')
def lampada():
    dicionario = {'Lampada Inteligente':'Ligado'}
    return render_template('lampada.html', dicionario=dicionario)

if __name__ == "__main__":  
    app.run(host='0.0.0.0', port=8080, debug=True)
