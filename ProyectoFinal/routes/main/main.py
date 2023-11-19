from flask import Flask, render_template, Blueprint

app = Flask(__name__)

appmain = Blueprint('main', __name__, template_folder='routes/main/templates', static_folder='routes/main/static')

@appmain.route('/')
def index():
    return render_template('main.html')

