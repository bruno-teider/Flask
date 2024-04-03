from flask import Flask

app= Flask(__name__)
## __name__ is the application name

@app.route('/')
def index():
    return"Hello, web world!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
