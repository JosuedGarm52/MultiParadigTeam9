from flask import Blueprint,request,redirect,render_template,url_for
from models import Venta
from forms import VentaForm
from app import db

appVenta = Blueprint('appventa', __name__, template_folder="templates")
APP_BASE = 'venta'

@appVenta.route(f'/')
@appVenta.route(f'/index{APP_BASE}')
def inicial():
    ventas = Venta.query.all()
    return render_template(f'index{APP_BASE}.html',ventas=ventas)

@appVenta.route(f'/agregar',methods = ["GET","POST"])
def agregar():
    venta = Venta()
    ventaForm = VentaForm(obj=venta)
    if request.method == "POST":
        if ventaForm.validate_on_submit():
            ventaForm.populate_obj(venta)
            db.session.add(venta)
            db.session.commit()
            return redirect(url_for(f'app{APP_BASE}.inicial'))
    return render_template(f'agregar{APP_BASE}.html',forma=ventaForm)

@appVenta.route(f"/editar/<int:id>",methods=["GET","POST"])
def editar(id):
    venta = Venta.query.get_or_404(id)
    ventaForm = VentaForm(obj=venta)
    if request.method == "POST":
        if ventaForm.validate_on_submit():
            ventaForm.populate_obj(venta)
            db.session.commit()
            return redirect(url_for(f'app{APP_BASE}.inicial'))
    return render_template(f'editar{APP_BASE}.html',forma=ventaForm)

@appVenta.route(f"/eliminar/<int:id>")
def eliminar(id):
    venta = Venta.query.get_or_404(id)
    db.session.delete(venta)
    db.session.commit()
    return redirect(url_for(f'app{APP_BASE}.inicial'))
