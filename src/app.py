from flask import Flask

PORT = 8000

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/par-impar')
def par_impar():
    numero = 10  # puedes cambiar este valor o pasarlo como parámetro
    if numero % 2 == 0:
        return f"{numero} es par"
    else:
        return f"{numero} es impar"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
