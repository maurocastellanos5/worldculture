from flask import Flask, render_template, abort, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from modelo.models import db, Usuario

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

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
