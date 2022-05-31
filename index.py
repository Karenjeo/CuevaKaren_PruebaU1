#Importacion de libreria
from flask import Flask, redirect, render_template, request, url_for
#Clave de la app
#Ruta donde esta los templates 
app = Flask(__name__, template_folder='Templates')
#Arreglo
registros = []

# Ruta principal
@app.route('/')
def inicio():
    return render_template('login.html')

# Ruta principal
@app.route('/')
def principal():
    return render_template('Registros.html', registros=registros)

#Ruta enviar 
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        Telefono = request.form['Telefono']
        estado = request.form['estado']

        registros.append({'nombre': nombre, 'Telefono': Telefono, 'estado': estado })

        return redirect(url_for('principal'))
            
#Controlador de la ruta para borrar
@app.route('/borrar', methods=['POST'])
def borrar():  
    if request.method == 'POST':

            registros.clear()
            return redirect(url_for('principal'))

#Ejecutar
if __name__ == '__main__':
    app.run(debug=True)