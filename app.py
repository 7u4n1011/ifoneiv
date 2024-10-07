from flask import *

app = Flask(__name__)

#página principal
@app.route('/')
def index():
  return render_template('index.html')


#menu pedidos
@app.route('/pedidos')
def pedidos():
  pass

#menu clientes
@app.route('/clientes')
def clientes():
  pass

#menu productos
@app.route('/productos')
def productos():
  pass

if __name__ == '__main__':
  app.run(debug=True)


from flask import *

import mysql.connector

conexion = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root",
 database=""
)
cursor = conexion.cursor()

app = Flask(__name__)
 