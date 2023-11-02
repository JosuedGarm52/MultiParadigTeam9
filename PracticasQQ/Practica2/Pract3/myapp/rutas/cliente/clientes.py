from flask import Blueprint,request,redirect,render_template,url_for
from models import Cliente
from forms import ClienteForm
from app import db

appCliente = Blueprint('appcliente', __name__, template_folder="templates")
APP_BASE = 'cliente'

@appCliente.route('/')
@appCliente.route('/index')
def inicial():
    clientes = Cliente.query.all()
    return render_template('index.html',clientes=clientes)

@appCliente.route('/agregar',methods = ["GET","POST"])
def agregar():
    cliente = Cliente()
    clienteForm = ClienteForm(obj=cliente)
    if request.method == "POST":
        if clienteForm.validate_on_submit():
            clienteForm.populate_obj(cliente)
            db.session.add(cliente)
            db.session.commit()
            return redirect(url_for(f'app{APP_BASE}.inicial'))
    return render_template('agregar.html',forma=clienteForm)

@appCliente.route("/editar/<int:id>",methods=["GET","POST"])
def editar(id):
    persona = Cliente.query.get_or_404(id)
    personaForm = ClienteForm(obj=persona)
    if request.method == "POST":
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            db.session.commit()
            return redirect(url_for(f'app{APP_BASE}.inicial'))
    return render_template('editar.html',forma=personaForm)

@appCliente.route("/eliminar/<int:id>")
def eliminar(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for(f'app{APP_BASE}.inicial'))
