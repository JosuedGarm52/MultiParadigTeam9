from flask import Flask, render_template, Blueprint, redirect, url_for,request, jsonify
from models import Cuenta,Perfil
from auth import tokenCheck,verificar
from app import db,bcrypt
from sqlalchemy import exc 
from sqlalchemy.orm.exc import NoResultFound
from utils import decode_auth_token, encode_auth_token
from auth import obtenerInfo

app = Flask(__name__)

appuser = Blueprint('user', __name__, template_folder='templates', static_folder='static', static_url_path='/user/static')

@appuser.route('/')
def index():
    return render_template('indexPerfilServer.html')#cambiar al adaptado

@appuser.route('/obtener_datos', methods = ["POST"])
def obtener_datos():
    # Obtener datos de la solicitud JSON
    datos_solicitud = request.json
    cuenta_idtoken = datos_solicitud.get('cuenta_id')
    cuenta_id = verificarID(cuenta_idtoken)

    usercuenta = obtenerInfo(token=cuenta_idtoken)
    userperfil = Perfil.query.filter_by(cuenta_id=cuenta_id).first()
    
    datos_usuario = {
        "primer_nombre": usercuenta['data']['pnombre'],
        "otros_nombres": usercuenta['data']['snombre'],
        "primer_apellido": usercuenta['data']['papellido'],
        "segundo_apellido": usercuenta['data']['sapellido'],
        "fecha_nacimiento": usercuenta['data']['fnacimiento'].strftime('%Y-%m-%d'),
        "telefono": usercuenta['data']['Telef'],
        "correo_electronico": usercuenta['data']['correo'],
        "usuario": userperfil.usuario,
        "pais":userperfil.pais_origen,
        "genero":userperfil.genero,
        "busqueda":userperfil.busqueda,
    }

    # Devolver los datos como respuesta JSON
    return jsonify(datos_usuario)

def verificarID(valor):
    try:
        token = valor
        # Decodificar el token para obtener la información
        decoded_token = decode_auth_token(token)
        # Acceder al valor del campo "sub"
        if 'sub' in decoded_token:
            sub_value = decoded_token['sub']
            cuenta_id = int(sub_value)
            return cuenta_id
        else:
            raise ValueError('El campo "sub" no está presente en el token')
    except ValueError:
        return jsonify({'status': 'error', 'message': 'El formato de cuenta_id no es válido'})

@appuser.route('/registro',methods=["GET","POST"])
def regis_perfil():
    if request.method == "GET":
        return render_template('regisUser.html')  # cambiar al adaptado
    else:
        try:
            token = request.json['cuenta_id']

            # Decodificar el token para obtener la información
            decoded_token = decode_auth_token(token)

            # Acceder al valor del campo "sub"
            if 'sub' in decoded_token:
                sub_value = decoded_token['sub']
                cuenta_id = int(sub_value)
            else:
                raise ValueError('El campo "sub" no está presente en el token')
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