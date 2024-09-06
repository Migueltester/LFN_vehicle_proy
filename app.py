from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL




app = Flask(__name__) #aplicacion

#Conexion a bd-mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_DB'] = 'lfn_bd'
mysql = MySQL(app)

#Conexion para guardar sesion 
app.secret_key = 'mysecretkey'



#----------Funcion para BUSCAR COLABORADORES------------
@app.route('/find_colab', methods=['POST'])
def find_colab():
    if request.method == 'POST':
        name = request.form['nombre']
        placa = request.form['placa']
    
    # Crear un cursor para ejecutar la consulta
    cur = mysql.connection.cursor()
    
    # Realizar una consulta con JOIN para obtener el nombre del departamento
    cur.execute('''
        SELECT c.id_colab, c.Nombre, c.Apellido, c.Cargo, c.vehiculo, c.placa, d.dep_nombre AS departamento_nombre
        FROM colaboradores c
        LEFT JOIN departamentos d ON c.id_dep = d.id_dep
        WHERE c.Nombre = %s OR c.placa = %s
    ''', (name, placa))
    
    # Obtener todos los resultados de la consulta
    info = cur.fetchall()
    cur.close()
    if info:
        flash('Se encontraron resultados')
        return render_template('CONSULTA.html', colaboradores=info)
    else:
        flash('No se encontraron resultados')
    return render_template('CONSULTA.html', colaboradores=info)
   
#-----------funcion para ANADIR COLABORADORES----------
@app.route('/add_colab', methods=['POST'])
def add_colab3():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        Apellido = request.form['Apellido']
        Cargo = request.form['Cargo']
        Departamento = request.form['Departamento']
        vehiculo = request.form['vehiculo']
        Placa = request.form['Placa']
        cursor_conexion = mysql.connection.cursor() # para meter en la tablas en mysql en la bd
        cursor_conexion.execute('INSERT INTO colaboradores(Nombre, Apellido, Cargo, vehiculo, placa, id_dep) VALUES(%s, %s, %s, %s, %s, %s)', (nombre, Apellido, Cargo,  vehiculo, Placa,Departamento,))
        mysql.connection.commit()
        flash('contacto anadido')
    return redirect(url_for('registro'))

#----------- funcion para Eliminar colaboradores------------
@app.route('/delete_contacto/<string:id>')
def delete_contacto(id):
    print(id)
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM colaboradores WHERE id_colab = %s', (id,))
    mysql.connection.commit()
    flash('contacto removido')
    return redirect(url_for('consulta'))

#------------ funcion para editar y actualizar colaboradores------
@app.route('/update_colab/<string:id>', methods=['POST'])
def update_colab(id):
    if request.method == 'POST':
        nombre = request.form['Nombre']
        Apellido = request.form['Apellido']
        Cargo = request.form['Cargo']
        Departamento = request.form['Departamento']
        vehiculo = request.form['vehiculo']
        Placa = request.form['Placa']

    cur = mysql.connection.cursor()
    cur.execute("""
    UPDATE colaboradores
                set Nombre = %s,
                Apellido = %s,
                Cargo = %s,
                id_dep = %s,
                vehiculo = %s,
                placa = %s
                WHERE id_colab = %s

        """, (nombre, Apellido, Cargo, Departamento, vehiculo, Placa, id))
    mysql.connection.commit()
    flash('Colaborador actualizado')
    return redirect(url_for('consulta'))


#----------Funcion para validar el inicio de sesion--------------
@app.route('/login_s', methods=['POST'])
def iniciar_sesion():
    user = request.form.get('username')
    password = request.form.get('password')
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM user WHERE usuario = %s AND password = %s', (user, password))
    cuenta = cur.fetchone()
    if cuenta:
        flash('Inicio de sesión exitoso', 'success')
        return redirect(url_for('registro'))
    else:
        flash('Nombre de usuario o contraseña incorrectos, vuelva a intentarlo', 'danger')
        return redirect(url_for('login'))
    

    


#-------------ruta de la pagina login----------
@app.route('/')
def login():
    return render_template('login_log.html')

@app.route('/indexo999999')
def index():
    return render_template('index.html')


#-------------ruta AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA de la pagina login-de prueba en github----------ELIMINAAAAAAAAAAAAAAAAAAAARr
@app.route('/Hola')
def login():
    return render_template('login_logholaaaaa.html')

@app.route('/indexo999999')
def index():
    return render_template('index.html')


#-------------ruta de la pagina Consulta y nuevo en xd github


@app.route('/CONSULTA')
def consulta():
    return render_template('CONSULTA.html')

#-------------ruta de la pagina registro
@app.route('/registro_s')
def registro():
    return render_template('Registro.html')

#--------------ruta para editar info de colaboradores
@app.route('/registro_edit/<string:id>')
def registro_edit(id):
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT c.id_colab, c.Nombre, c.Apellido, c.Cargo, c.vehiculo, c.placa, d.dep_nombre AS departamento_nombre
        FROM colaboradores c
        LEFT JOIN departamentos d ON c.id_dep = d.id_dep
        WHERE c.id_colab = %s 
''', (id,))
    data = cur.fetchall()
    if data and len(data):
        return render_template('registro_edit.html', colaborador = data[0])
    else:
        return redirect(url_for('registro'))




if __name__ == '__main__':
    app.run(port =3000, debug = True)