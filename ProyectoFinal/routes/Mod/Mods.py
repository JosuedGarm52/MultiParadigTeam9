from flask import Flask, render_template, Blueprint

app = Flask(__name__)

appmod = Blueprint('mod', __name__, template_folder='templates', static_folder='static', static_url_path='/main/static')

@appmod.route('/')
def index():
    return render_template('mod.html')#cambiar al adaptado