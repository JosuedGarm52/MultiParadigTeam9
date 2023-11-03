from flask import Blueprint,request,redirect,render_template,url_for
from models import Vendedor
from forms import VendedorForm
from app import db

appVendedor = Blueprint('appvendedor', __name__, template_folder="templates")
APP_BASE = 'vendedor'

@appVendedor.route(f'/{APP_BASE}/')
@appVendedor.route(f'/{APP_BASE}/index{APP_BASE}')
def inicial():
    vendedores = Vendedor.query.all()
    return render_template(f'index{APP_BASE}.html',vendedores=vendedores)

@appVendedor.route(f'/{APP_BASE}/agregar',methods = ["GET","POST"])
def agregar():
    vendedor = Vendedor()
    vendedorForm = VendedorForm(obj=vendedor)
    if request.method == "POST":
        if vendedorForm.validate_on_submit():
            vendedorForm.populate_obj(vendedor)
            db.session.add(vendedor)
            db.session.commit()
            return redirect(url_for(f'app{APP_BASE}.inicial'))
    return render_template(f'agregar{APP_BASE}.html',forma=vendedorForm)

@appVendedor.route(f"/{APP_BASE}/editar/<int:id>",methods=["GET","POST"])
def editar(id):
    vendedor = Vendedor.query.get_or_404(id)
    vendedorForm = VendedorForm(obj=vendedor)
    if request.method == "POST":
        if vendedorForm.validate_on_submit():
            vendedorForm.populate_obj(vendedor)
            db.session.commit()
            return redirect(url_for(f'app{APP_BASE}.inicial'))
    return render_template(f'editar{APP_BASE}.html',forma=vendedorForm)

@appVendedor.route(f"/{APP_BASE}/eliminar/<int:id>")
def eliminar(id):
    vendedor = Vendedor.query.get_or_404(id)
    db.session.delete(vendedor)
    db.session.commit()
    return redirect(url_for(f'app{APP_BASE}.inicial'))
