from flask import Flask, render_template, Blueprint, redirect, url_for,request, jsonify
from models import Cuenta,Perfil,Mod,Chat,Mensaje
from auth import tokenCheck,verificar
from app import db,bcrypt
from sqlalchemy import exc 
from sqlalchemy.orm.exc import NoResultFound
from utils import decode_auth_token, encode_auth_token, verificarID
from auth import obtenerInfo

app = Flask(__name__)

appmod = Blueprint('mod', __name__, template_folder='templates', static_folder='static', static_url_path='/main/static')

@appmod.route('/')
def index():
    return render_template('mod.html')

  
@appmod.route('/obtener_chat',methods=["POST"])
def obtener_chat():
    token = request.json['cuenta_id']
    cuenta_id = verificarID(token)

    usercuenta = Cuenta.query.filter_by(id_cuenta=cuenta_id).first()
    if usercuenta:
        usermod = Mod.query.filter_by(cuenta_id = usercuenta.id_cuenta ).first()
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