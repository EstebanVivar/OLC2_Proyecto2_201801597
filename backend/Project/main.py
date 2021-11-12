


from TablaSimbolos.Generator import Generator
from TablaSimbolos.TablaSimbolos import TablaSimbolos
from Optimizacion.Optimizador_Sintactico import parse2 as Optimizar
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from grammar import parserX
app = Flask(__name__)
CORS(app,resources={r'/*':{"origins":"*"}})

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/Bienvenida")
def welcome():
    return render_template('index.html')
C3D=''
@app.route("/Editor", methods=["POST","GET"])
def compilar():
    if request.method == "POST":    
        try:
            inpt = request.json['input']

            genAux = Generator()
            genAux.cleanAll()
            generator = genAux.getInstance()
            

            newEnv = TablaSimbolos(None)
            ast = parserX(inpt)
            DEBUGGER=None
            for instr in ast:
                DEBUGGER=instr
                instr.compilar(newEnv)
                
            C3D=generator.CodigoC3D()
            # res=Optimizar(C3D)
            # res.Mirilla()
            # a=res.getCode()
            # b=res.getReporte()
            # print(b)

            return  jsonify(generator.CodigoC3D())
        except Exception:
            print("**********")
            print(str(DEBUGGER))
            print("**********")
            return jsonify("Error")
    else:        
        return render_template('index.html')

@app.route('/Reportes')
def REPORTS():                
        return render_template('index.html')

@app.route('/AST', methods=["POST","GET"])
def AST():            
    if request.method == "POST":    
        return jsonify(auxGlobal[1])
    else:        
        return render_template('index.html')

@app.route('/TablaSimbolos', methods=["POST","GET"])
def Symbols():            
    if request.method == "POST":    
        return jsonify(auxGlobal[2])
    else:        
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)