#Importacion de libreria
from flask import Flask, redirect, render_template, request, url_for
#Clave de la app
#Ruta donde esta los templates 
app = Flask(__name__, template_folder='Templates')
#Arreglo
registros = []
tienda = []
# Ruta principal
@app.route('/')
def inicio():
    return render_template('login.html')

# Ruta principal
@app.route('/Registros.html')
def principal():
    return render_template('Registros.html', registros=registros)
# Ruta principal
@app.route('/Tienda.html')
def tiendas():
    return render_template('Tienda.html', tienda=tienda)

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

#Ruta enviar 
@app.route('/enviarT', methods=['POST'])
def enviart():
    if request.method == 'POST':
        nombret = request.form['nombret']
        Telefonot = request.form['Telefonot']
        estadot = request.form['estadot']
        gerentet = request.form['gerentet']


        tienda.append({'nombret': nombret, 'Telefonot': Telefonot, 'estadot': estadot, 'gerentet': gerentet })

        return redirect(url_for('tienda'))
            
#Controlador de la ruta para borrar
@app.route('/borrarT', methods=['POST'])
def borrart():  
    if request.method == 'POST':

            tienda.clear()
            return redirect(url_for('tienda'))

#Ejecutar
if __name__ == '__main__':
    app.run(debug=True)