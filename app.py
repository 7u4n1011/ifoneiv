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

# Menu clientes
@app.route('/cliente')
def clientes():
  pass

# Menu productos
@app.route('/productos')
def productos():
  pass

if __name__ == '__main__':
  app.run(debug=True)

#-------------------------- Menu Clientes------------------------

@app.route('/cliente')
def productos():
  query = "SELECT * FROM cliente"
  cursor.execute(query)
  cliente = cursor.fetchall()
  return render_template('productos.html',cliente=cliente)

@app.route('agregar_clientes', methods=['POST'])
def agregar_clientes():
  #obtengo los datos del formulario
  nombre = request.form.get('nombre')
  direccion = request.form.get('direccion')
  dni = request.form.get('dni')

  #los agrego a la base de datos
  query = 'INSERT INTO cliente (descripcion, precio) VALUES (%s, %s, %s)'
  cursor.execute(query, (nombre, direccion, dni))
  conexion.commit()
  return redirect(url_for('clientes'))

@app.route('/modificar_clientes', methods=['POST'])
def modificar_clientes():
  #obtengo el id que puso en el formulario
  ID_cliente = request.form.get('ID')

  #obtengo los campos modificados
  nombre = request.form.get('nombre')
  direccion = request.form.get('direccion')
  dni = request.form.get('dni')

  #ejecuto el sql para modificar
  query = 'UPDATE cliente SET nombre = %s, direccion = %s, dni = %s WHERE ID_cliente = %s'
  cursor.execute(query, (nombre, direccion, dni, ID_cliente))
  return redirect(url_for('clientes'))

@app.route('/eliminar_clientes', methods=['POST'])
def eliminar_clientes():
  #obtengo el id que puso en el formulario
  ID_cliente = request.form.get('ID')

  #hago la query en la base de datos para eliminar el producto de ese ID
  query = 'DELETE FROM cliente WHERE '+ID_cliente+' = cliente.ID_cliente'
  cursor.execute(query)
  conexion.commit()
  return redirect(url_for('clientes'))

if __name__ == '__main__':
  app.run(debug=True)