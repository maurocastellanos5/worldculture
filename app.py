from flask import Flask, render_template, abort, request, redirect, url_for
from modelo.models import db,Usuario
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:hola.123@localhost/WorldCulture'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Configuración para el manejo de la sesion de los usuarios
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = "inicio"


@loginManager.user_loader
def load_user(Id):
    return Usuario.query.get(int(Id))

app = Flask(__name__)


@app.route('/')
def inicio():
    if current_user.is_authenticated and current_user.Tipo=="A":
        return render_template('PanelAdministracion.html')
    else:
        return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    try:
        u = Usuario()
        u = u.validar(request.form['inputEmail'], request.form['inputPassword'])
        if u != None:
            login_user(u)
            return redirect(url_for('inicio'))
        else:
            return 'Datos No Válidos'
    except:
        abort(500)
    
@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for("inicio"))
    else:
        abort(404)


if __name__ == '__main__':
    app.run()
