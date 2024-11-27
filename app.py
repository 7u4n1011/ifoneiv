from flask import *

import mysql.connector

# Conexion a la base de datos
conexion = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root",
 database="iphone"
)
cursor = conexion.cursor()

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
  return render_template('index.html')


# Menu pedidos
@app.route('/pedido')
def pedidos():
  pass


# Menu productos
@app.route('/productos')
def productos():
  pass

#-------------------------- Menu Clientes------------------------

@app.route('/cliente')
def cliente():
  query = "SELECT * FROM cliente"
  cursor.execute(query)
  cliente = cursor.fetchall()
  return render_template('clientes.html',cliente=cliente)

@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    nombre = request.form.get('nombre')
    direccion = request.form.get('direccion')
    dni = request.form.get('dni')

    query = 'INSERT INTO cliente (nombre, direccion, dni) VALUES (%s, %s, %s)'
    cursor.execute(query, (nombre, direccion, dni))
    conexion.commit()
    return redirect(url_for('cliente'))


@app.route('/modificar_cliente', methods=['POST'])
def modificar_cliente():
    ID_cliente = request.form.get('ID')
    nombre = request.form.get('nombre')
    direccion = request.form.get('direccion')
    dni = request.form.get('dni')

    query = 'UPDATE cliente SET '
    values = []
    if nombre:
        query += 'nombre = %s, '
        values.append(nombre)
    if direccion:
        query += 'direccion = %s, '
        values.append(direccion)
    if dni:
        query += 'dni = %s, '
        values.append(dni)

    # Elimina la última coma y espacio
    query = query.rstrip(', ')
    query += ' WHERE ID_cliente = %s'
    values.append(ID_cliente)

    cursor.execute(query, tuple(values))
    conexion.commit()
    return redirect(url_for('cliente'))

@app.route('/eliminar_cliente', methods=['POST'])
def eliminar_cliente():
    # Obtengo el ID del formulario
    ID_cliente = request.form.get('ID')

    # Hago la query en la base de datos para eliminar el producto de ese ID
    query = 'DELETE FROM cliente WHERE ID_cliente = %s'
    cursor.execute(query, (ID_cliente,))
    conexion.commit()
    return redirect(url_for('cliente'))


if __name__ == '__main__':
  app.run(debug=True)

#hecho por juan elizondo
from flask import *

import mysql.connector
#conecion de base de datos 
conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="iphone"
)
cursor = conexion.cursor()  
app = flask(__name__) 


#menu productos 
@app.route('/productos')
def productos():
  query="SELECT * FROM producto"
  cursor.execute(query)
  productos = cursor.fetvhall()
  return render_template('producto.html',productos=productos)
