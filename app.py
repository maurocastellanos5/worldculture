from flask import Flask, render_template, abort, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from modelo.models import db, Usuario, Producto, Pedido, Cliente, Administrador, Direccion, Tarjeta, Paqueterias, Envio, Venta

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
    p= Producto()
    p=p.consultaGeneral()
    return render_template('/Ropa/RopaDama.html', Productos=p)

@app.route('/RopaCaballero')
def RopaCaballero():
    p= Producto()
    p=p.consultaGeneral()
    return render_template('/Ropa/RopaCaballero.html', Productos=p)

@app.route('/RopaNino')
def RopaNino():
    p= Producto()
    p=p.consultaGeneral()
    return render_template('/Ropa/RopaNino.html', Productos=p)

@app.route('/RopaNina')
def RopaNina():
    p= Producto()
    p=p.consultaGeneral()
    return render_template('/Ropa/RopaNina.html', Productos=p)
#Fin Rutas Departamento Ropa


#Inicio Rutas Departamento Accesorios
@app.route('/AccesoriosDama')
def AccesoriosDama():
    p= Producto()
    p=p.consultaGeneral()
    return render_template('/Accesorios/AccesoriosDama.html', Productos=p)

@app.route('/AccesoriosCaballero')
def AccesoriosCaballero():
    p= Producto()
    p=p.consultaGeneral()
    return render_template('/Accesorios/AccesoriosCaballero.html', Productos=p)

@app.route('/AccesoriosNino')
def AccesoriosNino():
    p= Producto()
    p=p.consultaGeneral()
    return render_template('/Accesorios/AccesoriosNino.html', Productos=p)

@app.route('/AccesoriosNina')
def AccesoriosNina():
    p= Producto()
    p=p.consultaGeneral()
    return render_template('/Accesorios/AccesoriosNina.html', Productos=p)
#Fin Rutas Departamento Ropa

#Inicio Rutas Departamento Calzado
@app.route('/CalzadoDama')
def CalzadoDama():
    p= Producto()
    p=p.consultaGeneral()
    return render_template('/Calzado/CalzadoDama.html', Productos=p)

@app.route('/CalzadoCaballero')
def CalzadoCaballero():
    p= Producto()
    p=p.consultaGeneral()
    return render_template('/Calzado/CalzadoCaballero.html', Productos=p)

@app.route('/CalzadoNino')
def CalzadoNino():
    p= Producto()
    p=p.consultaGeneral()
    return render_template('/Calzado/CalzadoNino.html', Productos=p)

@app.route('/CalzadoNina')
def CalzadoNina():
    p= Producto()
    p=p.consultaGeneral()
    return render_template('/Calzado/CalzadoNina.html', Productos=p)

#Fin Rutas Departamento Calzado

#Inicio Crud Productos
@app.route('/Productos')
@login_required
def consultaProductos():
    p = Producto()
    p=p.consultaGeneral()
    return render_template('/Productos/AdministrarProductos.html',Productos=p)

@app.route('/AddProductos',methods=['POST'])
@login_required
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
@login_required
def consultarProducto(id):
    p = Producto()
    p.IdProducto = id
    p = p.consultaIndividual()
    return render_template('Productos/EditProductos.html', Producto=p)

@app.route('/Productos/modificar', methods=['POST'])
@login_required
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
@login_required
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
@login_required
def consultarUsuario(id):
    u = Usuario()
    u.IdUsuario = id
    u = u.consultaIndividual()
    return render_template('Usuarios/EditAdministradores.html', Usuario=u)

@app.route('/Usuarios/modificar', methods=['POST'])
@login_required
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
@login_required
def eliminarUsuario(id):
    u = Usuario()
    u.IdUsuario = id
    u.eliminar()
    return redirect(url_for('consultaUsuarios'))
        
#Fin Crud Usuarios

#Inicio Crud Pedidos
@app.route('/Pedidos')
@login_required
def consultaPedidos():
    p = Pedido()
    p=p.consultaGeneral()
    return render_template('/Pedidos/AdministrarPedidos.html',Pedidos=p)

@app.route('/AddPedidos',methods=['POST'])
@login_required
def guardarPedidos():
    p = Pedido()
    p.IdProducto = request.form['IdProducto']
    p.Fecha = request.form['Fecha']
    p.IdCliente = request.form['IdCliente']
    p.insertar()
    return redirect(url_for('consultaPedidos'))

@app.route('/EditPedidos/<int:id>')
@login_required
def consultarPedido(id):
    p = Pedido()
    p.IdPedido = id
    p = p.consultaIndividual()
    return render_template('Pedidos/EditPedidos.html', Pedido=p)

@app.route('/Pedidos/modificar', methods=['POST'])
@login_required
def actualizarPedido():
    p = Pedido()
    p.IdPedido = request.form['IdPedido']
    p.IdProducto = request.form['IdProducto']
    p.Fecha = request.form['Fecha']
    p.IdCliente = request.form['IdCliente']
    p.actualizar()
    return redirect(url_for('consultaPedidos'))

@app.route('/DeletePedidos/<int:id>')
@login_required
def eliminarPedido(id):
    p = Pedido()
    p.IdPedido = id
    p.eliminar()
    return redirect(url_for('consultaPedidos'))
        
#Fin Crud Pedidos

#Inicio Crud Clientes
@app.route('/Clientes')
@login_required
def consultaClientes():
    c = Cliente()
    c=c.consultaGeneral()
    return render_template('/Clientes/AdministrarClientes.html',Clientes=c)

@app.route('/AddClientes',methods=['POST'])
@login_required
def guardarClientes():
    c = Cliente()
    c.IdUsuario = request.form['IdUsuario']
    c.insertar()
    return redirect(url_for('consultaClientes'))

@app.route('/EditClientes/<int:id>')
@login_required
def consultarCliente(id):
    c = Cliente()
    c.IdCliente = id
    c = c.consultaIndividual()
    return render_template('Clientes/EditClientes.html', Cliente=c)

@app.route('/Clientes/modificar', methods=['POST'])
@login_required
def actualizarCliente():
    c = Cliente()
    c.IdCliente = request.form['IdCliente']
    c.IdUsuario = request.form['IdUsuario']
    c.actualizar()
    return redirect(url_for('consultaClientes'))

@app.route('/DeleteClientes/<int:id>')
@login_required
def eliminarCliente(id):
    c = Cliente()
    c.IdCliente = id
    c.eliminar()
    return redirect(url_for('consultaClientes'))
        
#Fin Crud Clientes

#Inicio Crud Administradores
@app.route('/Administradores')
@login_required
def consultaAdministradores():
    a = Administrador()
    a = a.consultaGeneral()
    return render_template('/Administradores/AdministrarAdministrador.html', Administradores=a)

@app.route('/AddAdministradores',methods=['POST'])
@login_required
def guardarAdministradores():
    a = Administrador()
    a.IdUsuario = request.form['IdUsuario']
    a.insertar()
    return redirect(url_for('consultaAdministradores'))

@app.route('/EditAdministradores/<int:id>')
@login_required
def consultarAdministrador(id):
    a = Administrador()
    a.IdAdministrador = id
    a = a.consultaIndividual()
    return render_template('Administradores/EditAdministrador.html', Administrador=a)

@app.route('/Administradores/modificar', methods=['POST'])
@login_required
def actualizarAdministrador():
    a = Administrador()
    a.IdAdministrador = request.form['IdAdministrador']
    a.IdUsuario = request.form['IdUsuario']
    a.actualizar()
    return redirect(url_for('consultaAdministradores'))

@app.route('/DeleteAdministradores/<int:id>')
@login_required
def eliminarAdministrador(id):
    a = Administrador()
    a.IdAdministrador = id
    a.eliminar()
    return redirect(url_for('consultaAdministradores'))       
#Fin Crud Administradores

#Inicio Crud Direcciones
@app.route('/Direcciones')
@login_required
def consultaDirecciones():
    d = Direccion()
    d = d.consultaGeneral()
    return render_template('Direcciones/AdministrarDireccion.html', Direcciones=d)

@app.route('/AddDirecciones',methods=['POST'])
@login_required
def guardarDirecciones():
    d = Direccion()
    d.Pais         = request.form['Pais']
    d.Estado       = request.form['Estado']
    d.Ciudad       = request.form['Ciudad']
    d.Colonia      = request.form['Colonia']
    d.Calle        = request.form['Calle']
    d.CodigoPostal = request.form['CodigoPostal']
    d.Descripcion  = request.form['Descripcion']
    d.IdCliente    = request.form['IdCliente']
    d.insertar()
    return redirect(url_for('consultaDirecciones'))

@app.route('/EditDirecciones/<int:id>')
@login_required
def consultarDireccion(id):
    d = Direccion()
    d.IdDireccion = id
    d = d.consultaIndividual()
    return render_template('Direcciones/EditDireccion.html', Direccion=d)

@app.route('/Direcciones/modificar', methods=['POST'])
@login_required
def actualizarDireccion():
    d = Direccion()
    d.IdDireccion  = request.form['IdDireccion']
    d.Pais         = request.form['Pais']
    d.Estado       = request.form['Estado']
    d.Ciudad       = request.form['Ciudad']
    d.Colonia      = request.form['Colonia']
    d.Calle        = request.form['Calle']
    d.CodigoPostal = request.form['CodigoPostal']
    d.Descripcion  = request.form['Descripcion']
    d.IdCliente    = request.form['IdCliente']
    d.actualizar()
    return redirect(url_for('consultaDirecciones'))

@app.route('/DeleteDirecciones/<int:id>')
@login_required
def eliminarDireccion(id):
    d = Direccion()
    d.IdDireccion = id
    d.eliminar()
    return redirect(url_for('consultaDirecciones'))       
#Fin Crud Direcciones

#Inicio Crud Tarjetas
@app.route('/Tarjetas')
@login_required
def consultaTarjetas():
    t = Tarjeta()
    t = t.consultaGeneral()
    return render_template('Tarjetas/AdministrarTarjetas.html', Tarjetas=t)

@app.route('/AddTarjetas',methods=['POST'])
@login_required
def guardarTarjetas():
    t = Tarjeta()
    t.NumeroTarjeta    = request.form['NumeroTarjeta']
    t.FechaVencimiento = request.form['Fecha']
    t.Cvv              = request.form['CVV']
    t.Titular          = request.form['Titular']
    t.IdCliente        = request.form['IdCliente']
    t.insertar()
    return redirect(url_for('consultaTarjetas'))

@app.route('/EditTarjetas/<int:id>')
@login_required
def consultarTarjeta(id):
    t = Tarjeta()
    t.IdTarjeta = id
    t = t.consultaIndividual()
    return render_template('Tarjetas/EditTarjetas.html', Tarjeta=t)

@app.route('/Tarjetas/modificar', methods=['POST'])
@login_required
def actualizarTarjeta():
    t = Tarjeta()
    t.IdTarjeta    = request.form['IdTarjeta']
    t.NumeroTarjeta    = request.form['NumeroTarjeta']
    t.FechaVencimiento = request.form['Fecha']
    t.Cvv              = request.form['CVV']
    t.Titular          = request.form['Titular']
    t.IdCliente        = request.form['IdCliente']
    t.actualizar()
    return redirect(url_for('consultaTarjetas'))

@app.route('/DeleteTarjetas/<int:id>')
@login_required
def eliminarTarjeta(id):
    t = Tarjeta()
    t.IdTarjeta = id
    t.eliminar()
    return redirect(url_for('consultaTarjetas'))       
#Fin Crud Tarjetas

#Inicio Crud Paqueterias
@app.route('/Paqueterias')
@login_required
def consultaPaqueterias():
    p = Paqueterias()
    p = p.consultaGeneral()
    return render_template('Paqueteria/AdministrarPaqueteria.html', Paqueterias=p)

@app.route('/AddPaqueterias',methods=['POST'])
@login_required
def guardarPaqueterias():
    p = Paqueterias()
    p.Nombre = request.form['Nombre']
    p.insertar()
    return redirect(url_for('consultaPaqueterias'))

@app.route('/EditPaqueterias/<int:id>')
@login_required
def consultarPaqueterias(id):
    p = Paqueterias()
    p.IdPaqueteria  = id
    p = p.consultaIndividual()
    return render_template('Paqueteria/EditPaqueteria.html', Paqueteria=p)

@app.route('/Paqueterias/modificar', methods=['POST'])
@login_required
def actualizarPaqueteria():
    p = Paqueterias()
    p.IdPaqueteria    = request.form['IdPaqueteria']
    p.Nombre = request.form['Nombre']
    p.actualizar()
    return redirect(url_for('consultaPaqueterias'))

@app.route('/DeletePaqueterias/<int:id>')
@login_required
def eliminarPaqueteria(id):
    p = Paqueterias()
    p.IdPaqueteria    = id
    p.eliminar()
    return redirect(url_for('consultaPaqueterias'))       
#Fin Crud Paqueterias

#Inicio Crud Envios
@app.route('/Envios')
@login_required
def consultaEnvios():
    e = Envio()
    e = e.consultaGeneral()
    return render_template('Envios/AdministrarEnvio.html', Envios=e)

@app.route('/AddEnvios',methods=['POST'])
@login_required
def guardarEnvios():
    e = Envio()
    e.IdPaqueteria = request.form['IdPaqueteria']
    e.FechaSalida  = request.form['FechaSalida']
    e.FechaArribo  = request.form['FechaArribo']
    e.FechaEntrega = request.form['FechaEntrega']
    e.insertar()
    return redirect(url_for('consultaEnvios'))

@app.route('/EditEnvios/<int:id>')
@login_required
def consultarEnvio(id):
    e = Envio()
    e.IdEnvios = id
    e = e.consultaIndividual()
    return render_template('Envios/EditEnvio.html', Envio=e)

@app.route('/Envios/modificar', methods=['POST'])
@login_required
def actualizarEnvio():
    e = Envio()
    e.IdEnvios      = request.form['IdEnvio']
    e.IdPaqueteria = request.form['IdPaqueteria']
    e.FechaSalida  = request.form['FechaSalida']
    e.FechaArribo  = request.form['FechaArribo']
    e.FechaEntrega = request.form['FechaEntrega']
    e.actualizar()
    return redirect(url_for('consultaEnvios'))

@app.route('/DeleteEnvios/<int:id>')
@login_required
def eliminarEnvio(id):
    e = Envio()
    e.IdEnvios = id
    e.eliminar()
    return redirect(url_for('consultaEnvios'))       
#Fin Crud Envios

#Inicio Crud Ventas
@app.route('/Ventas')
@login_required
def consultaVentas():
    v = Venta()
    v = v.consultaGeneral()
    return render_template('Ventas/AdministrarVenta.html', Ventas=v)

@app.route('/AddVentas',methods=['POST'])
@login_required
def guardarVentas():
    v = Venta()
    v.IdPedido  = request.form['IdPedido']
    v.idEnvio  = request.form['IdEnvio']
    v.Fecha = request.form['Fecha']
    v.insertar()
    return redirect(url_for('consultaVentas'))

@app.route('/EditVentas/<int:id>')
@login_required
def consultarVenta(id):
    v = Venta()
    v.IdVentas = id
    v = v.consultaIndividual()
    return render_template('Ventas/EditVenta.html', Venta=v)

@app.route('/Ventas/modificar', methods=['POST'])
@login_required
def actualizarVenta():
    v = Venta()
    v.IdVentas     = request.form['IdVentas']
    v.IdPedido  = request.form['IdPedido']
    v.idEnvio  = request.form['IdEnvio']
    v.Fecha  = request.form['Fecha']
    v.actualizar()
    return redirect(url_for('consultaVentas'))

@app.route('/DeleteVentas/<int:id>')
@login_required 
def eliminarVentas(id):
    v = Venta()
    v.IdVentas = id
    v.eliminar()
    return redirect(url_for('consultaVentas'))       
#Fin Crud Ventas


#Inicio Ruta Contacto
@app.route('/Contacto')
def Contacto():
    return render_template('/Contacto/Contacto.html')
#Fin Ruta Contacto

#Inicio Ruta Carrtio
@app.route('/Carrito')
@login_required
def Carrito():
    return render_template('/Carrito/Carrito.html')
#Fin Ruta Carrito

#Inicio Ruta mis Pedidos
@app.route('/MisPedidos')
@login_required
def MisPedidos():
    return render_template('/Pedidos/MisPedidos.html')
#Fin Ruta mis Pedidos

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
