#PAGINA WEB

# Importar
from flask import Flask, render_template, request


app = Flask(__name__)

# La primera página
@app.route('/')
def index():
    return render_template('index.html')
# Segunda página
@app.route('/<defs>')
def definicion(defs):
    return render_template(
                            'definicion.html', 
                            defs = defs
    )

# La tercera página
@app.route('/<defs>/<caus>')
def causas(defs,caus):
    return render_template(
                            'causas.html',                           
                            caus = caus,
                            defs = defs
                           )

@app.route('/<defs>/<caus>/<sols>')
def soluciones(defs,caus,sols):
    return render_template(
                            'soluciones.html', 
                            defs = defs,
                            caus = caus,
                            sols = sols
                           )

if __name__ == '__main__':
    app.run(debug=True)
