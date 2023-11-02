from flask import Blueprint,request,redirect,render_template,url_for
from models import Venta
from forms import VentaForm
from app import db

appVenta = Blueprint('appventa', __name__, template_folder="templates")
APP_BASE = 'venta'

@appVenta.route('/venta/')
@appVenta.route('/venta/index')
def inicial():
    ventas = Venta.query.all()
    return render_template('index.html',ventas=ventas)

@appVenta.route('/venta/agregar',methods = ["GET","POST"])
def agregar():
    venta = Venta()
    ventaForm = VentaForm(obj=venta)
    if request.method == "POST":
        if ventaForm.validate_on_submit():
            ventaForm.populate_obj(venta)
            db.session.add(venta)
            db.session.commit()
            return redirect(url_for(f'app{APP_BASE}.inicial'))
    return render_template('agregar.html',forma=ventaForm)

@appVenta.route("/venta/editar/<int:id>",methods=["GET","POST"])
def editar(id):
    venta = Venta.query.get_or_404(id)
    ventaForm = VentaForm(obj=venta)
    if request.method == "POST":
        if ventaForm.validate_on_submit():
            ventaForm.populate_obj(venta)
            db.session.commit()
            return redirect(url_for(f'app{APP_BASE}.inicial'))
    return render_template('editar.html',forma=ventaForm)

@appVenta.route("/venta/eliminar/<int:id>")
def eliminar(id):
    venta = Venta.query.get_or_404(id)
    db.session.delete(venta)
    db.session.commit()
    return redirect(url_for(f'app{APP_BASE}.inicial'))
