from flask import Flask, render_template, Blueprint, redirect, url_for,request, jsonify, send_from_directory, send_file, abort
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

@appuser.route('/descargar_pdf/<tipo>',methods=['GET', 'POST'])
def descargar_pdf(tipo):
    token = request.json['cuenta_id']
    try:
        cuenta_id = verificarID(token)
    except Exception as e:
        # Aquí puedes manejar la excepción como desees.
        # Puedes imprimir un mensaje de depuración, registrar el error, etc.
        print(f"Error al verificar ID: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Error al verificar ID'}),412
    
    perfil = Perfil.query.filter_by(cuenta_id = cuenta_id).first()
    if perfil is None:
        return jsonify({'status': 'error', 'message': 'Perfil no encontrado'}), 404
    documento = Documento.query.filter_by(usuario_name=perfil.usuario, tipo = tipo).first()
    if documento is None:
        nombre_archivo = 'default.pdf'
        ruta_pdf = f'routes/user/static/pdf/{nombre_archivo}'
        return send_file(
            ruta_pdf,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='default.pdf'
        )
    # Construir la ruta completa al archivo PDF local
    ruta_pdf = documento.link

    return send_file(
        ruta_pdf,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'{perfil.usuario}_documento.pdf'
    )

@appuser.route('/obtener_datos', methods = ["POST"])
def obtener_datos():
    # Obtener datos de la solicitud JSON
    datos_solicitud = request.json
    cuenta_idtoken = datos_solicitud.get('cuenta_id')
    try:
        cuenta_id = verificarID(cuenta_idtoken)
    except Exception as e:
        # Aquí puedes manejar la excepción como desees.
        # Puedes imprimir un mensaje de depuración, registrar el error, etc.
        print(f"Error al verificar ID: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Error al verificar ID'}),412
    
    usercuenta = Cuenta.query.filter_by(id_cuenta = cuenta_id).first()
    if usercuenta is None:
            abort(404, description="Usuario no encontrado")

    userperfil = Perfil.query.filter_by(cuenta_id=cuenta_id).first()
    if userperfil is None:
            abort(404, description="Perfil de usuario no encontrado")

    userdocs = Documento.query.filter_by(usuario_name = userperfil.usuario).all()
    email = usercuenta.email

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
        "primer_nombre": usercuenta.primer_nombre,
        "otros_nombres": usercuenta.otros_nombres,
        "primer_apellido": usercuenta.primer_apellido,
        "segundo_apellido": usercuenta.segundo_apellido,
        "fecha_nacimiento": usercuenta.fecha_nacimiento.strftime('%Y-%m-%d'),
        "telefono": usercuenta.telefono,
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
    try:
        cuenta_id = verificarID(_id)
    except Exception as e:
        # Aquí puedes manejar la excepción como desees.
        # Puedes imprimir un mensaje de depuración, registrar el error, etc.
        print(f"Error al verificar ID: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Error al verificar ID'}),412

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