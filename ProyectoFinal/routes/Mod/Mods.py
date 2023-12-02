from flask import Flask, render_template, Blueprint, redirect, url_for,request, jsonify, send_file,abort
from models import Cuenta,Perfil,Mod,Chat,Mensaje,Documento
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
    
@appmod.route('/perfil', methods=['POST','GET'])
def abrir_userView():
    perfil_id = request.args.get('id')  # Obtén el ID del perfil de los parámetros de consulta
    return render_template('userView.html', perfil_id=perfil_id)

@appmod.route('/descargar_pdf/<tipo>',methods=['GET', 'POST'])
def descargar_pdf(tipo):
    
    token = request.json['perfil_id']
    
    
    perfil = Perfil.query.filter_by(cuenta_id = token).first()
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

@appmod.route('/obtener_datos', methods = ["POST"])
def obtener_datos():
    # Obtener datos de la solicitud JSON
    datos_solicitud = request.json
    perfil_id = datos_solicitud.get('perfil_id')
    cuenta_idtoken = datos_solicitud.get('mod_id')

    usercuenta = Cuenta.query.filter_by(id_cuenta = perfil_id).first()
    if usercuenta is None:
            abort(404, description="Usuario no encontrado")
    userperfil = Perfil.query.filter_by(cuenta_id=perfil_id).first()
    if userperfil is None:
            abort(404, description="Perfil de usuario no encontrado")

    userdocs = Documento.query.filter_by(usuario_name = userperfil.usuario).all()

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
        "usuario": userperfil.usuario,
        "acta":listacta,
        "comprobante": listcomprobante,  
        "ine":listine,
        "passpord": listpasspord,
    }

    # Devolver los datos como respuesta JSON
    return jsonify(datos_usuario)

@appmod.route('/prueba', methods=['POST'])
def manejar_solicitud_de_prueba():
    try:
        # Ejemplo de respuesta (reemplaza con la respuesta adecuada para tu caso)
        respuesta = {'mensaje': 'Solicitud de prueba recibida exitosamente'}

        return jsonify(respuesta)

    except Exception as e:
        # Manejar cualquier error que pueda ocurrir durante el procesamiento
        print(f"Error al manejar la solicitud de prueba: {str(e)}")
        return jsonify({'error': 'Error interno del servidor'}), 500