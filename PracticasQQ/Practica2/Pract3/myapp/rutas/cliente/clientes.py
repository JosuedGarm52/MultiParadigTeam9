from flask import Blueprint,request,redirect,render_template,url_for
from models import Cliente
from forms import ClienteForm
from app import db

appCliente = Blueprint('appcliente', __name__, template_folder="templates")
APP_BASE = 'cliente'

@appCliente.route('/')
@appCliente.route('/index')
def bienvenida():
    return render_template('bienvenida.html')

@appCliente.route(f'/{APP_BASE}')
@appCliente.route(f'/{APP_BASE}/index{APP_BASE}')
def inicial():
    clientes = Cliente.query.all()
    return render_template(f'index{APP_BASE}.html',clientes=clientes)

@appCliente.route(f"/{APP_BASE}/editar/<int:id>",methods=["GET","POST"])
def editar(id):
    cliente = Cliente.query.get_or_404(id)
    clienteForm = ClienteForm(obj=cliente)
    if request.method == "POST":
        if clienteForm.validate_on_submit():
            clienteForm.populate_obj(cliente)
            db.session.commit()
            return redirect(url_for(f'app{APP_BASE}.inicial'))
    return render_template(f'editar{APP_BASE}.html',forma=clienteForm)

@appCliente.route(f"/{APP_BASE}/eliminar/<int:id>")
def eliminar(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for(f'app{APP_BASE}.inicial'))