from flask import Flask, render_template, Blueprint, redirect, url_for,request, jsonify
from models import Cuenta,Perfil,Mod,Chat,Mensaje
from auth import tokenCheck,verificar
from app import db,bcrypt
from sqlalchemy import exc 
from sqlalchemy.orm.exc import NoResultFound
from utils import decode_auth_token, encode_auth_token, verificarID, sanitize_local_link
from auth import obtenerInfo
import os

app = Flask(__name__)

appmod = Blueprint('mod', __name__, template_folder='templates', static_folder='static', static_url_path='/main/static')

@appmod.route('/')
def index():
    return render_template('mod.html')

  
@appmod.route('/obtener_chat',methods=["POST"])
def obtener_chat():
    token = request.json['cuenta_id']
    try:
        cuenta_id = verificarID(token)
    except Exception as e:
        # Aquí puedes manejar la excepción como desees.
        # Puedes imprimir un mensaje de depuración, registrar el error, etc.
        print(f"Error al verificar ID: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Error al verificar ID'}) ,412

    usercuenta = Cuenta.query.filter_by(id_cuenta=cuenta_id).first()
    if usercuenta:
        usermod = Mod.query.filter_by(cuenta_id = usercuenta.id_cuenta ).first()
        link = usermod.linkcsv
        if usermod:
            lista_chats = obtener_chats_unicos(usermod)
            nombres = [
                usercuenta.primer_nombre,
                usercuenta.otros_nombres,
                usercuenta.primer_apellido,
                usercuenta.segundo_apellido
            ]
            # Filtra los nombres que no son None
            nombres_no_nulos = [nombre for nombre in nombres if nombre is not None]
            # Combina los nombres con un espacio como separador
            nombre_completo = ' '.join(nombres_no_nulos)
            datos_usuario = {
                "Nombre": nombre_completo,
                "lista":lista_chats,
                "link": link,
            }
            # Devolver los datos como respuesta JSON
            return jsonify(datos_usuario)
        else:
            responseObject = {
            'status' : 'fail',
            'message': 'mod no encontrado'
            }
            return jsonify(responseObject), 505
        
    else:
        responseObject = {
                'status' : 'fail',
                'message': 'Cuenta no encontrada'
            }
        return jsonify(responseObject), 503
    
def obtener_chats_unicos(usermod):
    lista_chats = Chat.query.filter_by(mod_id=usermod.id_mod).all()

    datos_chats = []
    combinaciones_unicas = set()

    for chat in lista_chats:
        mensaje = Mensaje.query.filter_by(id_mensaje=chat.mensaje_id).first()

        # Asegúrate de que haya un mensaje asociado al chat
        if mensaje:
            remitente = mensaje.usuario_rem
            destinatario = mensaje.usuario_dest

            # Ordena los participantes alfabéticamente antes de agregar al conjunto
            combinacion_ordenada = tuple(sorted([remitente, destinatario]))

            # Asegúrate de que las combinaciones no se repitan
            if combinacion_ordenada not in combinaciones_unicas:
                datos_chat = {
                    'remitente': remitente,
                    'destinatario': destinatario
                }

                datos_chats.append(datos_chat)

                # Agrega la combinación al conjunto de combinaciones únicas
                combinaciones_unicas.add(combinacion_ordenada)

    return datos_chats


@appmod.route('/guardar_enlace', methods=['POST'])
def guardar_enlace():
    # Obtiene el enlace del cuerpo de la solicitud
    data = request.get_json()
    enlace = data.get('enlace')
    _id = data.get('cuenta_id')
    try:
        cuenta_id = verificarID(_id)
    except Exception as e:
        # Aquí puedes manejar la excepción como desees.
        # Puedes imprimir un mensaje de depuración, registrar el error, etc.
        print(f"Error al verificar ID: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Error al verificar ID'}),412
    
    cuenta = Cuenta.query.filter_by(id_cuenta = cuenta_id).first()
    mod = Mod.query.filter_by(cuenta_id = cuenta.id_cuenta).first()

    if cuenta:
        # Verifica si la cuenta tiene un moderador asociado
        if mod:
            enlace_saneado = sanitize_local_link(enlace)
            # Verifica si el enlace tiene la extensión .csv
            if enlace_saneado.lower().endswith('.csv'):
                # Actualiza el campo linkcsv del moderador
                mod.linkcsv = enlace_saneado

                # Confirma los cambios en la base de datos
                db.session.commit()

                # Retorna una respuesta (puedes ajustar el contenido según tus necesidades)
                return jsonify({'mensaje': 'Enlace guardado exitosamente'})
            else:
                return jsonify({'mensaje': 'La extensión del archivo debe ser .csv'})
        else:
            return jsonify({'mensaje': 'No se encontró un moderador asociado a la cuenta'})
    else:
        return jsonify({'mensaje': 'No se encontró la cuenta'})


@appmod.route('/borrar_enlace', methods=['POST'])
def borrar_enlace():
    # Obtiene el ID de la cuenta y el enlace del cuerpo de la solicitud
    data = request.get_json()
    _id = data.get('cuenta_id')
    try:
        cuenta_id = verificarID(_id)
    except Exception as e:
        # Aquí puedes manejar la excepción como desees.
        # Puedes imprimir un mensaje de depuración, registrar el error, etc.
        print(f"Error al verificar ID: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Error al verificar ID'}),412
    
    # Busca la cuenta y el moderador asociado
    cuenta = Cuenta.query.get(cuenta_id)
    mod = Mod.query.filter_by(cuenta_id=cuenta.id_cuenta).first()

    if cuenta:
        # Verifica si la cuenta tiene un moderador asociado
        if mod:
            # Establece el campo linkcsv del moderador como nulo
            mod.linkcsv = None

            # Confirma los cambios en la base de datos
            db.session.commit()

            # Retorna una respuesta (puedes ajustar el contenido según tus necesidades)
            return jsonify({'mensaje': 'Enlace eliminado exitosamente'})
        else:
            return jsonify({'mensaje': 'No se encontró un moderador asociado a la cuenta'})
    else:
        return jsonify({'mensaje': 'No se encontró la cuenta'})

@appmod.route('/obtener_perfiles', methods=['POST'])
def obtener_perfiles():
    try:
        perfiles = Perfil.query.all()

        # Convierte la lista de perfiles a un formato JSON
        lista_perfiles = [
            {
                
                "id": perfil.cuenta.id_cuenta,
                "nombre": perfil.cuenta.primer_nombre,
                "apellido": perfil.cuenta.primer_apellido,
                "usuario": perfil.usuario,
            }
            for perfil in perfiles
        ]

        # Devuelve la lista de perfiles como respuesta JSON
        return jsonify({"perfiles": lista_perfiles})

    except Exception as e:
        return jsonify({'error': str(e)}), 503