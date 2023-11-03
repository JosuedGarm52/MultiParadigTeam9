from flask import Blueprint,request,redirect,render_template,url_for
from models import Agencia
from forms import AgenciaForm
from app import db

appAgencia = Blueprint('appagencia', __name__, template_folder="templates")
APP_BASE = 'agencia'

@appAgencia.route(f'/')
@appAgencia.route(f'/index{APP_BASE}')
def inicial():
    agencias = Agencia.query.all()
    return render_template(f'index{APP_BASE}.html',agencias=agencias)

@appAgencia.route(f'/agregar',methods = ["GET","POST"])
def agregar():
    agencia = Agencia()
    agenciaForm = AgenciaForm(obj=agencia)
    if request.method == "POST":
        if agenciaForm.validate_on_submit():
            agenciaForm.populate_obj(agencia)
            db.session.add(agencia)
            db.session.commit()
            return redirect(url_for(f'app{APP_BASE}.inicial'))
    return render_template(f'agregar{APP_BASE}.html',forma=agenciaForm)

@appAgencia.route(f"/editar/<int:id>",methods=["GET","POST"])
def editar(id):
    agencia = Agencia.query.get_or_404(id)
    agenciaForm = AgenciaForm(obj=agencia)
    if request.method == "POST":
        if agenciaForm.validate_on_submit():
            agenciaForm.populate_obj(agencia)
            db.session.commit()
            return redirect(url_for(f'app{APP_BASE}.inicial'))
    return render_template(f'editar{APP_BASE}.html',forma=agenciaForm)

@appAgencia.route(f"/eliminar/<int:id>")
def eliminar(id):
    agencia = Agencia.query.get_or_404(id)
    db.session.delete(agencia)
    db.session.commit()
    return redirect(url_for(f'app{APP_BASE}.inicial'))
