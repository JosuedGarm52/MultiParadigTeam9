from flask import Flask, render_template, Blueprint

app = Flask(__name__)

appuser = Blueprint('user', __name__, template_folder='templates', static_folder='static', static_url_path='/main/static')

@appuser.route('/')
def index():
    return render_template('indexPerfil.html')#cambiar al adaptado

@appuser.route('/registro')
def regis_perfil():
    return render_template('regisUser.html')#cambiar al adaptado

@appuser.route('/parejas')
def parejas():
    return render_template('SearchPareja.html')#cambiar al adaptado