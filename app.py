from flask import Flask, render_template, abort, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from modelo.models import db, Usuario

app = Flask(__name__)
app.secret_key = 'W0rldCultur3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:hola.123@localhost/WorldCulture'
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
        return 'Datos No Válidos'

@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for("inicio"))
    else:
        return render_template('login.html')

#Fin de Configuración para el manejo de la sesion


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
