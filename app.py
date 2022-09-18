from flask import Flask, request, render_template, redirect, url_for , flash, session
from flask_mysqldb import MySQL,MySQLdb
from os import path #pip install notify-py
from notifypy import Notify


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

@app.route('/login', methods= ["GET", "POST"])
def login():

    notificacion = Notify()

    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s",(correo,))
        user = cur.fetchone()
        cur.close()
        if len(user)>0:
            if contrasena == user["contrasena"]:
                session ['nombre'] = user['nombre']
                session['correo'] = user['correo']
            else:
                notificacion.title = "Error de Acceso"
                notificacion.message="Correo o contraseña no valida"
                notificacion.send()
                return render_template("login.html")
        else:
            notificacion.title = "Error de Acceso"
            notificacion.message="No existe el usuario"
            notificacion.send()
            return render_template("login.html")
    else:
        
        return render_template("login.html")



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
        print(nombre, telefono, correo, contrasena)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO profesores (nombre, telefono, correo, contrasena) VALUES (%s, %s, %s, %s)", (nombre, telefono, correo, contrasena))
        mysql.connection.commit()
        flash('USURUARIO REGISTRADO CORREOTAMENTE')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port = 300, debug = True)