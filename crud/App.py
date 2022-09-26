from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

# Conexión DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'agendap'
mysql = MySQL(app)

# Configuraciones
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    return render_template('crear.html')

@app.route('/crear', methods = ['POST'])
def crear():
    if request.method == 'POST':
        materia = request.form['materia']
        dias = request.form['dias']
        hora_inicio = request.form['hora_inicio']
        hora_fin = request.form['hora_fin']
        instituto = request.form['instituto']
        salon = request.form['salon']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO clases (materia, dias, hora_inicio, hora_fin, instituto, salon) VALUES (%s, %s, %s, %s, %s, %s)', (materia, dias, hora_inicio, hora_fin, instituto, salon))
        mysql.connection.commit()
        flash('Clase programada satisfactoriamente')
        return redirect(url_for('Index'))

#Listar
@app.route('/listar')
def listar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM clases')
    datos = cur.fetchall()
    return render_template('leer.html', informacion = datos)

@app.route('/editar/<id>')
def obtener_informacion(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM clases WHERE id = %s',(id))
    datos = cur.fetchall()
    return render_template('editar-clase.html', registros = datos[0])

@app.route('/actualizar/<id>', methods = ['POST'])
def actualizar_clase(id):
    if request.method == 'POST':
        materia = request.form['materia']
        dias = request.form['dias']
        hora_inicio = request.form['hora_inicio']
        hora_fin = request.form['hora_fin']
        instituto = request.form['instituto']
        salon = request.form['salon']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE clases SET materia = %s, dias = %s, hora_inicio = %s, hora_fin = %s, instituto = %s, salon = %s WHERE id = %s', (materia, dias, hora_inicio, hora_fin, instituto, salon))
        mysql.connection.commit()
        flash('Clase actualizada satisfactoriamente')
        return redirect(url_for('listar.html'))

@app.route('/eliminar/<string:id>')
def eliminar_clase(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM clases WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Clase eliminada satisfactoriamente')
    return redirect(url_for('listar'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)