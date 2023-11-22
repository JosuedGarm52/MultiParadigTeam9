from flask import Flask, render_template, Blueprint

app = Flask(__name__)

appadmin = Blueprint('admin', __name__, template_folder='templates', static_folder='static', static_url_path='/main/static')

@appadmin.route('/')
def index():
    return render_template('admin.html')#cambiar al adaptado