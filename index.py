# Importar las librerias
from flask import Flask, abort, render_template

# Instanciar la aplicaicon
app = Flask(__name__)

#ruta principal
@app.route('/')
#Llamar a index.html en la ruta principal
def principal():
    return render_template('login.html')


# main del programa
if __name__ == '__main__':
    # debug = True, para reiniciar automatica el servidor
    app.run(debug=True)

