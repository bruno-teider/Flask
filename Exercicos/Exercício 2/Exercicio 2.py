from flask import Flask

app= Flask(__name__)
## __name__ is the application name

@app.route('/')
def index():
    return """
    <html>
    <head>
        <title>Minha Casa</title>
    </head>
    <body>
        <h2>Minha Casa</h2>
        <h3>Escolha um cômodo:</h3>
        <ul>
            <li><a href="/quarto">Quarto</a></li>
            <li><a href="/banheiro">Banheiro</a></li>
        </ul>
    </body>
    </html>
    """

@app.route('/quarto')
def quarto():
    return """
    <html>
    <head>
        <title>Quarto</title>
    </head>
    <body>
        <h1>Sensores/Atuadores no quarto</h1>
        <ul>
            <li><a href="/quarto/luminosidade">Sensor de Luminosidade</a></li>
            <li><a href="/quarto/interruptor">Interruptor</a></li>
        </ul>
        <p>Voltar para <a href="/">página inicial</a>!</p>
    </body>
    </html>
    """

@app.route('/quarto/luminosidade')
def luminosidade():
    return """
    <html>
    <head>
        <title>Luminosidade</title>
    </head>
    <body>
        <h1>Sensor de luminosidade</h1>
        <h2>Luminosidade: 60%
        <p>Voltar para <a href="/">página inicial</a>!</p>
    </body>
    </html>
    """

@app.route('/quarto/interruptor')
def interruptor():
    return """
    <html>
    <head>
        <title>Interruptor</title>
    </head>
    <body>
        <h1>Interruptor</h1>
        <h2>Estado: desligado
        <p>Voltar para <a href="/">página inicial</a>!</p>
    </body>
    </html>
    """

@app.route('/banheiro')
def banheiro():
    return """
    <html>
    <head>
        <title>Banheiro</title>
    </head>
    <body>
        <h1>Sensores/Atuadores no banheiro</h1>
        <ul>
            <li><a href="/banheiro/umidade">Sensor de Umidade</a></li>
            <li><a href="/banheiro/lampada">Lâmpada Inteligente</a></li>
        </ul>
        <p>Voltar para <a href="/">página inicial</a>!</p>
    </body>
    </html>
    """

@app.route('/banheiro/umidade')
def umidade():
    return """
    <html>
    <head>
        <title>Sensor Umidade</title>
    </head>
    <body>
        <h1>Sensor de Umidade</h1>
        <h2>Umidade: 60%
        <p>Voltar para <a href="/">página inicial</a>!</p>
    </body>
    </html>
    """

@app.route('/banheiro/lampada')
def lampada():
    return """
    <html>
    <head>
        <title>Lampada Inteligente</title>
    </head>
    <body>
        <h1>Lampada Inteligente</h1>
        <h2>Estado: desligado
        <p>Voltar para <a href="/">página inicial</a>!</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
