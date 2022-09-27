import re
from flask import Flask, request, render_template, redirect, url_for , flash, jsonify
from flask_mysqldb import MySQL,MySQLdb
import requests


#-------------------------------CONECION DEL MYSQL----------------------------------------------------------------
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ELIANXD55'
app.config['MYSQL_DB'] = 'agendaprofesor' 
mysql = MySQL(app )

app.secret_key = 'contraseñasecreta'
#-----------------------------------------------------------------------------------------------
#-------------------------------------ACA EN LA RUTA RAIZ VA HA MOSTRAR EL LOGIN CON EL RENDER----------------------------------------------------------
@app.route('/')
def casa():
    return render_template('login.html')
#---------------------------------------ACA VA O VAIR EL CRUD CON LA INFORMACION DEL USUARIO-------------------------------------------------------
@app.route('/home/<id>',methods= ["POST",'GET'])
def home(id):
    ids = id
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute(f'select c.id_clase , p.nombre, c.materia ,c.dias,c.inicio,c.final,c.instituo,c.salon from profesores p left join clases c on p.id = c.id_profe where p.id = {ids};')
        data = cur.fetchall()
        print(data)
        return render_template('index.html') and render_template('index.html', informaciones = data , ids = id) 


@app.route('/atras')
def atras():
    return render_template('login.html')
#-----------------------------------------------------------------------------------------------
#----------------------------------------ACA VA EL LOGIN CON SUS METODOS Y LOS PRINTS SON DEBUGS-------------------------------------------------------
@app.route('/login', methods= ["POST",'GET'])
def login():
    comprobar = 0
    if request.method == 'POST': 
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
                print("------------------------------------------------------------------------")
                print(id)
                print(nombre)
                print(telefono)
                print(core)
                print(contra)
                print("ENCONTRADOOOOOOOOOOO")
                print("------------------------------------------------------------------------")
                id = i['id']
                nombre = i['nombre']
                telefono = i['telefono']
                core = i['correo']
                contra = i['contrasena']
            if core == correo and contra == contrasena:
                comprobar = 1
                return redirect(url_for(f'crear',id = id)) and render_template('index.html', ids = id) and redirect(url_for(f'unir',id = id))  
        if comprobar == 0:
            flash('CORREO O CONTRASEÑA INVALIDOS')
            return render_template('login.html') 
    else:
        return redirect(url_for(f'crear',id = id))  and render_template('index.html', ids = id)


@app.route('/unir/<id>')
def unir(id):
    ids  = id
    return redirect(url_for('home', id = ids))

#-----------------------------------------------------------------------------------------------
#---------------------------------------ACA EN LA RAIZ REGISTRO VA RENDERIZAR EL REGISTRO.HTML---------------------------------------------------
@app.route('/registro')
def registro():
    return render_template('registro.html')
#-----------------------------------------------------------------------------------------------
#------------------------------------------ACA VA TODA LA LOGICA DEL REGISTRO CON SU METODO Y CONEXION DEL LA API----------------------------------------------------
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
    return render_template('login.html')

#-----------------------------------------------------------------------------------------------
@app.route('/crear/<id>' , methods= ["POST",'GET'])
def crear(id):
    ids = id
    if request.method == 'GET':
        ids = id
        return render_template('index.html')  
    
    else:
        materia = request.form['materia']
        dias = request.form['dias']
        inicio= request.form['inicio']
        final = request.form['final']
        instituto = request.form['instituto']
        salon = request.form['salon']
        print("--------------------------------------------------------------------------------")
        print(materia)
        print(dias)
        print(inicio)
        print(final)
        print(instituto)
        print(salon)
        print(ids)
        print("--------------------------------------------------------------------------------")
        cur = mysql.connection.cursor()
        cur.execute(' INSERT clases (materia,dias,inicio,final,instituo,salon,id_profe) VALUES (%s,%s,%s,%s,%s,%s,%s)',
        (materia,dias,inicio,final,instituto,salon,ids))
        mysql.connection.commit()
        flash('SE HA AGREGADO CON EXITO LA CLASE  ')
        return redirect(url_for('home', id = ids))

#------------------------------CRUD--------------------------------------------------------------
@app.route('/actualizar/<id>')
def actualizar(id):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM clases WHERE id_clase= {id}")
    data = cur.fetchall()
    print(data)
    
    return render_template('editar.html', informacion = data[0])

@app.route('/eliminar/<id>')
def eliminar(id):
    cur = mysql.connection.cursor()
    cur.execute(' DELETE FROM clases WHERE id_clase = {0}'.format(id))
    mysql.connection.commit()
    flash('CLASE ELIMINADA CORRECTAMENTE')
    return render_template('index.html')

@app.route('/update/<id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        materia = request.form['materia']
        dias = request.form['dias']
        inicio= request.form['inicio']
        final = request.form['final']
        instituto = request.form['instituto']
        salon = request.form['salon']
        cur = mysql.connection.cursor()
        cur.execute("""
                UPDATE clases 
                SET materia = %s,
                    dias = %s,
                    inicio = %s,
                    final = %s,
                    instituo= %s,
                    salon = %s
                WHERE id_clase = %s
                """, (materia,dias,inicio,final,instituto,salon,id))
        
        mysql.connection.commit()
        flash('CLASE ACTUALIZADO CORRECTAMENTE')
        return render_template("index.html")

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
    return jsonify({'INFORMACION':informacion, 'MENSAJE':'GOOOOOOOOOOOOOOOOD'}) and redirect(url_for('home'))
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