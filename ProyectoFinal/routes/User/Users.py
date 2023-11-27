from flask import Flask, render_template, Blueprint, redirect, url_for,request, jsonify, send_from_directory
from models import Cuenta,Perfil,Documento, Perfil_Foto, Foto
from auth import tokenCheck,verificar
from app import db,bcrypt
from sqlalchemy import exc 
from sqlalchemy.orm.exc import NoResultFound
from utils import decode_auth_token, encode_auth_token, verificarID
from auth import obtenerInfo
import os

app = Flask(__name__)

appuser = Blueprint('user', __name__, template_folder='templates', static_folder='static', static_url_path='/user/static')

@appuser.route('/')
def index():
    return render_template('indexPerfil.html')

@appuser.route('/default')
def obtener_default_pdf():
    # Ruta al directorio de documentos estáticos
    directorio_documentos = 'pdf'  # No es necesario poner 'static/' aquí

    # Devolver el archivo PDF predeterminado usando send_from_directory
    ruta_pdf = url_for('user.static', filename='pdf/default.pdf')
    return send_from_directory(directorio_documentos, 'default.pdf')

@app.route('/ver_pdf/<filename>')
def ver_pdf(filename):
    return send_from_directory('pdf', filename)

@appuser.route('/obtener_datos', methods = ["POST"])
def obtener_datos():
    # Obtener datos de la solicitud JSON
    datos_solicitud = request.json
    cuenta_idtoken = datos_solicitud.get('cuenta_id')
    cuenta_id = verificarID(cuenta_idtoken)

    usercuenta = obtenerInfo(token=cuenta_idtoken)
    userperfil = Perfil.query.filter_by(cuenta_id=cuenta_id).first()
    userdocs = Documento.query.filter_by(usuario_name = userperfil.usuario).all()
    email = usercuenta['data']['correo']

    listacta = []
    listcomprobante = []
    listine = []
    listpasspord = []

    for userdoc in userdocs:
        if userdoc.tipo == "acta":
            listacta.append({
                "link": userdoc.link,
                "isaprobado": userdoc.isaprobado,
                "tipo": userdoc.tipo
            })
        elif userdoc.tipo == "comprobante":
            listcomprobante.append({
                "link": userdoc.link,
                "isaprobado": userdoc.isaprobado,
                "tipo": userdoc.tipo
            })
        elif userdoc.tipo == "ine":
            listine.append({
                "link": userdoc.link,
                "isaprobado": userdoc.isaprobado,
                "tipo": userdoc.tipo
            })
        elif userdoc.tipo == "passpord":
            listpasspord.append({
                "link": userdoc.link,
                "isaprobado": userdoc.isaprobado,
                "tipo": userdoc.tipo
            })
    datos_usuario = {
        "primer_nombre": usercuenta['data']['pnombre'],
        "otros_nombres": usercuenta['data']['snombre'],
        "primer_apellido": usercuenta['data']['papellido'],
        "segundo_apellido": usercuenta['data']['sapellido'],
        "fecha_nacimiento": usercuenta['data']['fnacimiento'].strftime('%Y-%m-%d'),
        "telefono": usercuenta['data']['Telef'],
        "correo_electronico": email.lower().strip(),
        "usuario": userperfil.usuario,
        "pais":userperfil.pais_origen,
        "genero":userperfil.genero,
        "busqueda":userperfil.busqueda,
        "acta":listacta,
        "comprobante": listcomprobante,  
        "ine":listine,
        "passpord": listpasspord,
    }

    # Devolver los datos como respuesta JSON
    return jsonify(datos_usuario)

@appuser.route('/perfil/<_id>', methods=['GET'])
def obtener_perfil(_id):
    cuenta_id = verificarID(_id)

    usercuenta = Cuenta.query.filter_by(id_cuenta=cuenta_id).first()
    userperfil = Perfil.query.filter_by(cuenta_id=usercuenta.id_cuenta).first()

    # Obtener fotos asociadas al perfil
    fotos_perfil = sorted(
        [
            {"link": foto.foto.link, "isperfil": foto.isperfil} for foto in userperfil.perfil_fotos
        ],
        key=lambda x: not x["isperfil"]  # Coloca True primero
    )

    # Crear el objeto con los datos a enviar como respuesta JSON
    datos_perfil = {
        "fotos_perfil": fotos_perfil,
        # Puedes agregar más datos según sea necesario
    }

    return jsonify(datos_perfil)


@appuser.route('/registro',methods=["GET","POST"])
def regis_perfil():
    if request.method == "GET":
        return render_template('regisUser.html')  
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
    return render_template('SearchPareja.html')