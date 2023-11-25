from flask import Flask, render_template, Blueprint, redirect, url_for,request, jsonify
from models import Cuenta,Perfil
from auth import tokenCheck,verificar
from app import db,bcrypt
from sqlalchemy import exc 
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)

appuser = Blueprint('user', __name__, template_folder='templates', static_folder='static', static_url_path='/user/static')

@appuser.route('/')
def index():
    return render_template('indexPerfil.html')#cambiar al adaptado

@appuser.route('/registro',methods=["GET","POST"])
def regis_perfil():
    if request.method == "GET":
        return render_template('regisUser.html')  # cambiar al adaptado
    else:
        try:
            cuenta_id = int(request.json['cuenta_id'])
        except ValueError:
            return jsonify({'status': 'error', 'message': 'El formato de cuenta_id no es válido'})

        # Verificar si la cuenta_id existe en la tabla Cuenta
        try:
            cuenta_existente = Cuenta.query.filter_by(id_cuenta=cuenta_id).one()
        except NoResultFound:
            return jsonify({'status': 'error', 'message': 'La cuenta_id no existe o no es válida'})

        usuario = request.json['username']
        pais_origen = request.json['pais']
        genero = request.json['genero']
        busqueda = request.json['busqueda']
        estado_civil = request.json['estado_civil']

        perfil = Perfil(
            usuario=usuario,
            pais_origen=pais_origen,
            genero=genero,
            busqueda=busqueda,
            estado_civil=estado_civil,
            cuenta_id=cuenta_id
        )

        userExists = Perfil.query.filter_by(usuario=usuario).first()
        if not userExists:
            try:
                db.session.add(perfil)
                db.session.commit()
                responseObject = {
                    'status': 'success',
                    'message': "Registro exitoso",
                    'redirect_url': url_for('user.index')
                }
            except exc.SQLAlchemyError as e:
                responseObject = {
                    'status': 'error',
                    'message': e
                }
        else:
            responseObject = {
                'status': 'error',
                'message': 'perfil existente'
            }

        return jsonify(responseObject)

@appuser.route('/parejas')
def parejas():
    return render_template('SearchPareja.html')#cambiar al adaptado