from flask import Flask, render_template, abort, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from modelo.models import db, Usuario, Producto

app = Flask(__name__)
app.secret_key = 'W0rldCultur3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin1:hola.123@localhost/WorldCulture'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuración para el manejo de la sesion de los usuarios
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = "inicio"


@loginManager.user_loader
def load_user(Id):
    return Usuario.query.get(int(Id))

@app.route('/')
def inicio():
    if current_user.is_authenticated and current_user.Tipo=="A":
        return render_template('PanelAdministracion.html')
    if current_user.is_anonymous:
        return render_template('index.html')

@app.route('/iniciar')
def iniciosesion():
    if current_user.is_anonymous:
        return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    u = Usuario()
    u = u.validar(request.form['inputEmail'], request.form['inputPassword'])
    if u != None:
        login_user(u)
        return redirect(url_for('inicio'))
    else:
        return 'Datos incorrectos'

@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for("inicio"))
    else:
        return render_template('login.html')

#Fin de Configuración para el manejo de la sesion


#Inicio Rutas Departamento Ropa
@app.route('/RopaDama')
def RopaDama():
    return render_template('/Ropa/RopaDama.html')

@app.route('/RopaCaballero')
def RopaCaballero():
    return render_template('/Ropa/RopaCaballero.html')

@app.route('/RopaNino')
def RopaNino():
    return render_template('/Ropa/RopaNino.html')

@app.route('/RopaNina')
def RopaNina():
    return render_template('/Ropa/RopaNina.html')
#Fin Rutas Departamento Ropa


#Inicio Rutas Departamento Accesorios
@app.route('/AccesoriosDama')
def AccesoriosDama():
    return render_template('/Accesorios/AccesoriosDama.html')

@app.route('/AccesoriosCaballero')
def AccesoriosCaballero():
    return render_template('/Accesorios/AccesoriosCaballero.html')

@app.route('/AccesoriosNino')
def AccesoriosNino():
    return render_template('/Accesorios/AccesoriosNino.html')

@app.route('/AccesoriosNina')
def AccesoriosNina():
    return render_template('/Accesorios/AccesoriosNina.html')
#Fin Rutas Departamento Ropa

#Inicio Rutas Departamento Calzado
@app.route('/CalzadoDama')
def CalzadoDama():
    return render_template('/Calzado/CalzadoDama.html')

@app.route('/CalzadoCaballero')
def CalzadoCaballero():
    return render_template('/Calzado/CalzadoCaballero.html')

@app.route('/CalzadoNino')
def CalzadoNino():
    return render_template('/Calzado/CalzadoNino.html')

@app.route('/CalzadoNina')
def CalzadoNina():
    return render_template('/Calzado/CalzadoNina.html')

#Fin Rutas Departamento Calzado

#Inicio Crud Productos
@app.route('/Productos')
def consultaProductos():
    p = Producto()
    p=p.consultaGeneral()
    return render_template('/Productos/AdministrarProductos.html',Productos=p)

@app.route('/AddProductos',methods=['POST'])
def guardarProducto():
    p = Producto()
    p.CodigoBarras = request.form['Codigo']
    p.Nombre = request.form['Nombre']
    p.Descripcion = request.form['Descripcion']
    p.Departamento = request.form['Departamento']
    p.Seccion = request.form['Seccion']
    p.Stock = request.form['Stock']
    p.PrecioVenta = request.form['PrecioVenta']
    p.PrecioCompra = request.form['PrecioCompra']
    p.insertar()
    return redirect(url_for('consultaProductos'))

@app.route('/EditProductos/<int:id>')
def consultarProducto(id):
    p = Producto()
    p.IdProducto = id
    p = p.consultaIndividual()
    return render_template('Productos/EditProductos.html', Producto=p)

@app.route('/Productos/modificar', methods=['POST'])
def actualizarProducto():
    p = Producto()
    p.IdProducto = request.form['IdProducto']
    p.CodigoBarras = request.form['Codigo']
    p.Nombre = request.form['Nombre']
    p.Descripcion = request.form['Descripcion']
    p.Departamento = request.form['Departamento']
    p.Seccion = request.form['Seccion']
    p.Stock = request.form['Stock']
    p.PrecioVenta = request.form['PrecioVenta']
    p.PrecioCompra = request.form['PrecioCompra']
    p.actualizar()
    return redirect(url_for('consultaProductos'))

@app.route('/DeleteProductos/<int:id>')
def eliminarProducto(id):
    p = Producto()
    p.IdProducto = id
    p.eliminar()
    return redirect(url_for('consultaProductos'))        
#Fin Crud Productos

#Inicio Crud Usuarios
@app.route('/Usuarios')
def consultaUsuarios():
    u = Usuario()
    u=u.consultaGeneral()
    return render_template('/Usuarios/AdministrarAdmin.html',Usuarios=u)

@app.route('/AddUsuarios',methods=['POST'])
def guardarUsuarios():
    u = Usuario()
    u.Nombre = request.form['Nombre']
    u.Telefono = request.form['Telefono']
    u.Email = request.form['Email']
    u.Contrasenia = request.form['Password']
    u.Sexo = request.form['Sexo']
    u.Tipo = request.form['Tipo']
    u.insertar()
    return redirect(url_for('consultaUsuarios'))

@app.route('/EditUsuarios/<int:id>')
def consultarUsuario(id):
    u = Usuario()
    u.IdUsuario = id
    u = u.consultaIndividual()
    return render_template('Usuarios/EditAdministradores.html', Usuario=u)

@app.route('/Usuarios/modificar', methods=['POST'])
def actualizarUsuario():
    u = Usuario()
    u.IdUsuario = request.form['IdUsuario']
    u.Nombre = request.form['Nombre']
    u.Telefono = request.form['Telefono']
    u.Email = request.form['Email']
    u.Contrasenia = request.form['Password']
    u.Sexo = request.form['Sexo']
    u.Tipo = request.form['Tipo']
    u.actualizar()
    return redirect(url_for('consultaUsuarios'))

@app.route('/DeleteUsuario/<int:id>')
def eliminarUsuario(id):
    u = Usuario()
    u.IdUsuario = id
    u.eliminar()
    return redirect(url_for('consultaUsuarios'))
        
#Fin Crud Usuarios

#Inicio Ruta Contacto
@app.route('/Contacto')
def Contacto():
    return render_template('/Contacto/Contacto.html')
#Fin Ruta Contacto

#Inicio Ruta Carrtio
@app.route('/Carrito')
def Carrito():
    return render_template('/Carrito/Carrito.html')
#Fin Ruta Carrito

#Inicio Ruta mis Pedidos
@app.route('/MisPedidos')
def MisPedidos():
    return render_template('/Pedidos/MisPedidos.html')
#Fin Ruta mis Pedidos

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
