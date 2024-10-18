""" from flask import Flask, render_template, request , redirect, url_for

app = Flask(__name__)  #instanciamos la aplicacion

#Ruta principal que muestre el menu de opciones 
@app.route('/',  methods = ['GET', 'POST'])
def index():
    return render_template('index.html')
    


#Ruta para el Formulario de inscripcion en curso
@app.route('/inscrip', methods = ['GET', 'POST'])   #/inscrip ruta
def inscripcion():  #funcion inscripcion
    if request.method =="POST":
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        curso = request.form.get('curso')
        return render_template('inscripciones.html', nombre = nombre, apellido = apellido , curso = curso )
    return render_template('index.html')





if __name__ == '__main__':  ##ejecutamos la aplicacion 
    app.run(debug= True) """

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        data = request.form
        return render_template('confirmacion.html', data=data, formulario='Inscripción en curso')
    return render_template('inscripcion.html')

@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        data = request.form
        return render_template('confirmacion.html', data=data, formulario='Registro de usuarios')
    return render_template('usuarios.html')

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        data = request.form
        return render_template('confirmacion.html', data=data, formulario='Registro de productos')
    return render_template('productos.html')

@app.route('/libros', methods=['GET', 'POST'])
def libros():
    if request.method == 'POST':
        data = request.form
        return render_template('confirmacion.html', data=data, formulario='Registro de libros')
    return render_template('libros.html')

if __name__ == '__main__':
    app.run(debug=True)
