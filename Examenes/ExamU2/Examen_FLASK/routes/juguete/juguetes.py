from flask import Blueprint,request,redirect,render_template,url_for,send_from_directory
from models import Juguete
from forms import JugueteForm
from app import db
import os

appjuguete = Blueprint('appjuguete',__name__,template_folder="templates",static_folder='static') #Se registra una nueva subaplicación o Blueprint
#Se maneja como si fuera una aplicación normal
@appjuguete.route('/')
@appjuguete.route('/index') #READ
def inicio(): #Cualquier de esas dos rutas hará referencia a este método de inicio
    juguetes = Juguete.query.all() #Traernos todas las personas, todos los objetos de una base de datos
    return render_template('index.html',juguetes=juguetes)

@appjuguete.route('/agregar',methods=["GET","POST"]) #CREATE
def agregar():
    juguete = juguete() #Instanciar un objeto de la clase persona
    jugueteForm = JugueteForm(obj=juguete)
    if request.method == "POST":
        if jugueteForm.validate_on_submit():
            jugueteForm.populate_obj(juguete)
            db.session.add(juguete)
            db.session.commit()
            return redirect(url_for('appjuguete.inicio'))
    return render_template('agregar.html',forma=jugueteForm)

@appjuguete.route("/editar/<int:id>",methods=["GET","POST"]) #UPDATE
def editar(id):
    juguete = Juguete.query.get_or_404(id)
    jugueteForm = JugueteForm(obj=juguete)
    if request.method == "POST":
        if jugueteForm.validate_on_submit():
            jugueteForm.populate_obj(juguete)
            db.session.commit()
            return redirect(url_for('appjuguete.inicio'))
    return render_template('editar.html',forma=jugueteForm)

@appjuguete.route('/eliminar/<int:id>') #DELETE
def eliminar(id):
    juguete = Juguete.query.get_or_404(id)
    db.session.delete(juguete)
    db.session.commit()
    return redirect(url_for('appjuguete.inicio'))