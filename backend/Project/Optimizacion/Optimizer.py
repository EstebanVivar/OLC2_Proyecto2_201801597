from Optimizador_Sintactico import parse2 as Optimizar
from flask import Flask, request
from flask.helpers import url_for
from werkzeug.utils import redirect
import json
from flask_cors import CORS
import sys

sys.setrecursionlimit(10000000)

app = Flask(__name__)
CORS(app)

@app.route('/saludo', methods = ["GET"])
def saludo():
    return "Hola estamos en Optimizador"

@app.route('/optimizar', methods = ["POST", "GET"])
def optimizar():
    if request.method == "POST":
        entrada = request.data.decode("utf-8")
        entrada = json.loads(entrada)
        global tmp_val_opt
        tmp_val_opt = entrada["codigo"]
        return redirect(url_for("mirilla"))

@app.route('/mirilla')
def mirilla():
    try:
        global tmp_val_opt
        res = Optimizar(tmp_val_opt)
        res.Mirilla()
        consola = res.getCode()
        global reporte 
        reporte = res.getReporte()
        return json.dumps(consola)
    except:
        consola = "Se  ha ejecutado un problema de compilacion :c"
        return json.dumps(consola)

@app.route('/reporte', methods = ['GET'])
def reporte():
    try:
        global reporte
        return {'valores': reporte}
    except:
        consola = "Se  ha ejecutado un problema de compilacion :c"
        return json.dumps(consola)


if __name__ == '__main__':
    app.run(debug = True, port=5300)