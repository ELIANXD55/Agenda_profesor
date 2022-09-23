from distutils.log import info
import telnetlib
from flask import Flask, request, render_template, redirect, url_for , flash, jsonify
from flask_mysqldb import MySQL,MySQLdb
from os import path #pip install notify-py
from notifypy import Notify
import requests



app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ELIANXD55'
app.config['MYSQL_DB'] = 'agendaprofesor' 
mysql = MySQL(app )

app.secret_key = 'contraseñasecreta'

@app.route('/')
def casa():
    return render_template('login.html')

@app.route('/home<id><nombre><telefono><correo><contrasena>')
def home(id,nombre, telefono , correo , contrasena):
    #return "welcome {0}{1}{2}{3}{4} ".format(id,nombre,telefono,correo,contrasena)
    datos = "welcome {0}{1}".format(id,nombre)
    return render_template("index.html", informacion = datos)

@app.route('/login', methods= ["POST",'GET'])
def login():
    bandera = 0
    datos = 0
    comprobar = 0
    if request.method == 'POST': 
        lista = []
        json = {}
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        response = requests.get('http://127.0.0.1:300/informacion')
        data = response.json()
        result = data['INFORMACION']
        for i in result:
            id = i['id']
            nombre = i['nombre']
            telefono = i['telefono']
            core = i['correo']
            contra = i['contrasena']
            if core == correo and contra == contrasena:
                lista.append(id)
                lista.append(nombre)
                lista.append(telefono)
                lista.append(core)
                lista.append(contra)
                json['id'] = id
                json['nombre'] = nombre
                json['telefono'] = telefono
                json['correo'] = core
                json['contrasena'] = contra
                print("------------------------------------------------------------------------")

                print(id)
                print(nombre)
                print(telefono)
                print(core)
                print(contra)
                print("ENCONTRADOOOOOOOOOOO")
                print("------------------------------------------------------------------------")
                comprobar = 1
                datos =jsonify({'INFORMACION':json, 'MENSAJE':'ACA SE ACABA LA LISTA'})
                return redirect(url_for('home',id = id, nombre = nombre, telefono = telefono  , correo = core , contrasena = contra))
        if comprobar == 0:
            flash('CORREO O CONTRASEÑA INVALIDOS')
            return render_template('login.html')
    else:
        return redirect(url_for('home',id = id, nombre = nombre, telefono = telefono  , correo = core , contrasena = contra))


@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/register', methods =['POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        json ={
            "NOMBRE": nombre,
            "TELEFONO": telefono,
            "CORREO": correo,
            "CONTRASENA": contrasena
        }
        response = requests.post('http://127.0.0.1:300/informacion',json=json)
        print(dir(response))
        flash('USURUARIO REGISTRADO CORREOTAMENTE')
    return redirect(url_for('login'))

#-------------------------------API-----------------------------------------------------------------------------
#------------------------------CONVIERTE LA INFO DE LA BD A API------------------------------------------------
@app.route('/informacion')
def informacion():
    cur = mysql.connection.cursor()
    cur.execute('SELECT id , nombre , telefono , correo , contrasena FROM profesores')
    datos = cur.fetchall()
    informacion = []
    for fila in datos:
        informacio ={'id':fila[0],'nombre':fila[1],'telefono':fila[2],'correo':fila[3],'contrasena':fila[4]}
        informacion.append(informacio)
    return jsonify({'INFORMACION':informacion, 'MENSAJE':'ACA SE ACABA LA LISTA'})
#-----------------------------------------------------------------------------------------------------------------
#------------------------------TRAE LA INFO DE LA API Y ME MUESTRA LO QUE NECEDITO------------------------------------------------
@app.route('/informacion/<correo>', methods= ['GET'])
def leer(correo):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id , nombre , telefono , correo , contrasena FROM profesores WHERE correo = '{0}' ".format(correo))
    datos = cur.fetchone()
    if datos != None:
        informacion ={'id':datos[0], 'nombre':datos[1], 'telefono':datos[2], 'correo':datos[3], 'contrasena':datos[4]}
        a = jsonify({'INFORMACION':informacion, 'MENSAJE':'GOOOOOOOOOOOOOOOOD'})
        return a
#-----------------------------------------------------------------------------------------------------------------
#------------------------------AGREGO------------------------------------------------
@app.route('/informacion', methods=['POST'])
def registro_api():
    cur = mysql.connection.cursor()
    cur.execute("""INSERT INTO profesores (nombre,telefono,correo,contrasena) VALUES ('{0}','{1}','{2}','{3}')
                """.format(request.json['NOMBRE'],request.json['TELEFONO'],request.json['CORREO'],request.json['CONTRASENA'],))
    mysql.connection.commit()
    return jsonify({"MENSAJE": "AGREGADO" })

if __name__ == '__main__':
    app.run(port = 300, debug = True)