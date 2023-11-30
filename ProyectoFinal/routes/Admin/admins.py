from flask import Flask, Blueprint,request,jsonify,render_template,redirect, send_file
from auth import tokenCheck,verificar
from app import db,bcrypt
from models import Perfil, Cuenta,Mod,Admin, Mensaje, Chat, Noticia
from sqlalchemy import exc, func
from utils import encode_auth_token, decode_auth_token, verificarID
import pandas as pd
from datetime import datetime, timedelta
import io
from collections import defaultdict

app = Flask(__name__)

appadmin = Blueprint('admin', __name__, template_folder='templates', static_folder='static', static_url_path='/main/static')

@appadmin.route('/')
def index():
    return render_template('admin.html')#cambiar al adaptado

@appadmin.route('noticias')
def obtener_noticias():
    # Aquí obtienes las noticias de la base de datos (puedes adaptar según tu modelo)
    noticias = Noticia.query.all()

    # Creas una lista de diccionarios con los datos de cada noticia
    lista_noticias = [
        {
            'id': noticia.id,
            'text1': noticia.text1 if noticia.text1 else '',
            'text2': noticia.text2 if noticia.text2 else '',
            'url': noticia.url if noticia.url 
            else 'https://upload.wikimedia.org/wikipedia/commons/a/a3/Image-not-found.png'
        }
        for noticia in noticias
        # Puedes agregar más condiciones si necesitas verificar otros campos
    ]

    # Devuelves la lista de noticias como respuesta JSON
    return jsonify({'noticias': lista_noticias})

@appadmin.route('/agregar_noticia', methods=['POST'])
def agregar_noticia():
    try:
        data = request.get_json()
        text1 = request.json['text1']
        text2 = data.get('text2')
        url = data.get('url')

        # Crea una instancia de Noticia permitiendo valores nulos
        noticia = Noticia(text1=text1, text2=text2, url=url)

        # Aquí puedes agregar la lógica para guardar la noticia en la base de datos
        db.session.add(noticia)
        db.session.commit()

        # Retorna una respuesta (puedes ajustar el contenido según tus necesidades)
        return jsonify({'mensaje': 'Noticia agregada exitosamente'})
    except Exception as e:
        print(f"Error al agregar noticia: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al procesar la solicitud'}), 500

@appadmin.route('/borrar_noticia/<int:noticia_id>', methods=['DELETE'])
def borrar_noticia(noticia_id):
    try:
        # Busca la noticia por su ID
        noticia = Noticia.query.get(noticia_id)

        if not noticia:
            return jsonify({'error': 'Noticia no encontrada'}), 404

        # Elimina la noticia de la base de datos
        db.session.delete(noticia)
        db.session.commit()

        return jsonify({'message': 'Noticia borrada correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@appadmin.route('/obtener_mod')
def obtener_mod():
    try:
        # Obtener la lista de moderadores desde la base de datos
        moderadores = Mod.query.all()

        # Crear una lista de diccionarios con los datos de cada moderador
        lista_moderadores = []
        for moderador in moderadores:
            # Acceder a los datos de la cuenta asociada al moderador
            cuenta = moderador.cuenta
            info_moderador = {
                'cuenta_id': cuenta.id_cuenta,
                'primer_nombre': cuenta.primer_nombre,
                'primer_apellido': cuenta.primer_apellido,
                'correo': cuenta.email,
                # Agrega más campos según sea necesario
            }
            lista_moderadores.append(info_moderador)

        # Devolver la lista de moderadores como respuesta JSON
        return jsonify(lista_moderadores)

    except Exception as e:
        # Manejar cualquier error que pueda ocurrir durante la obtención de moderadores
        print(f"Error al obtener moderadores: {str(e)}")
        return jsonify({'error': 'Error al obtener moderadores'}), 500
    
@appadmin.route('/buscar_cuentas')
def buscar_cuentas():
    try:
        # Obtén el texto de búsqueda de la solicitud
        texto_busqueda = request.args.get('texto', '').strip()

        # Lista para almacenar información de las cuentas sin relaciones
        cuentas_sin_relacion = []

        if texto_busqueda:
            # Realiza la búsqueda de cuentas en la base de datos según el texto
            cuentas_encontradas = Cuenta.query.filter(
                (Cuenta.primer_nombre.ilike(f'%{texto_busqueda}%')) |
                (Cuenta.primer_apellido.ilike(f'%{texto_busqueda}%'))|
                (Cuenta.email.ilike(f'%{texto_busqueda}%'))
            ).all()

            # Crea una lista de diccionarios con la información de las cuentas encontradas
            lista_cuentas = [
                {
                    'cuenta_id': cuenta.id_cuenta,
                    'primer_nombre': cuenta.primer_nombre,
                    'primer_apellido': cuenta.primer_apellido,
                    'correo': cuenta.email,
                }
                for cuenta in cuentas_encontradas
                # Verifica si la cuenta tiene relación con Perfil, Admin o Mod
                if not tiene_relacion(cuenta)
            ]
        else:
            # Obtén todas las cuentas
            todas_las_cuentas = Cuenta.query.all()

            for cuenta in todas_las_cuentas:
                cuenta_id = cuenta.id_cuenta

                # Verifica si la cuenta tiene relación con Perfil, Admin o Mod
                if not tiene_relacion(cuenta):
                    cuentas_sin_relacion.append({
                        'cuenta_id': cuenta.id_cuenta,
                        'primer_nombre': cuenta.primer_nombre,
                        'primer_apellido': cuenta.primer_apellido,
                        'correo': cuenta.email,
                        # Agrega más campos según sea necesario
                    })

        # Devuelve la lista de cuentas como respuesta JSON
        return jsonify({'cuentas': lista_cuentas if texto_busqueda else cuentas_sin_relacion})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def tiene_relacion(cuenta):
    # Verifica si la cuenta tiene relación con Perfil, Admin o Mod
    perfil = Perfil.query.filter_by(cuenta_id=cuenta.id_cuenta).first()
    admin = Admin.query.filter_by(cuenta_id=cuenta.id_cuenta).first()
    mod = Mod.query.filter_by(cuenta_id=cuenta.id_cuenta).first()

    return perfil is not None or admin is not None or mod is not None


@appadmin.route('/asignar_cuenta/<_id>', methods = ["POST"])
def asignar_cuenta(_id):
    cuentaMod = Cuenta.query.filter_by(id_cuenta = _id).first()
    mod = Mod(id_cuenta=cuentaMod.id_cuenta, cuenta=cuentaMod)
    modExist = Mod.query.filter_by(id_mod = mod.id_mod)
    if modExist:
        try:
            db.session.add(mod)
            db.session.commit()
            responseObject={
                'status':'success',
                'message':"El ascenso a mod existoso"
            }
        except exc.SQLAlchemyError as e:
            responseObject={
                'status':'error',
                'message':e
            }
    else:
        responseObject={
            'status':'error',
            'message':'el ascenso a mod fallo'
        }
    return jsonify(responseObject)


@appadmin.route('/quitar_mod/<_id>', methods = ["POST"])
def quitar_mod(_id):
    cuentaMod = Cuenta.query.filter_by(id_cuenta = _id).first()
    modExist = Mod.query.filter_by(cuenta_id = cuentaMod.id_cuenta).first()
    if modExist:
        try:
            db.session.delete(modExist)
            db.session.commit()
            responseObject={
                'status':'success',
                'message':"El ascenso a cliente exitoso"
            }
        except exc.SQLAlchemyError as e:
            responseObject={
                'status':'error',
                'message':e
            }
    else:
        responseObject={
            'status':'error',
            'message':'No se pudo quitar el permiso de mod'
        }
    return jsonify(responseObject)

@appadmin.route('/csv_mod/<_id>')
def generar_csv_mod(_id):
    mod = Mod.query.filter_by(cuenta_id=_id).first()

    if mod:
        # Obtén los IDs de los chats moderados por el Mod
        ids_chats_moderados = [chat.id_mensaje for chat in mod.chat]

        # Realiza la consulta con SQLAlchemy
        resultados = (
            db.session.query(
                func.least(Mensaje.usuario_rem, Mensaje.usuario_dest).label('persona_1'),
                func.greatest(Mensaje.usuario_rem, Mensaje.usuario_dest).label('persona_2'),
                func.count().label('cantidad_mensajes')
            )
            .filter(Mensaje.id_mensaje.in_(ids_chats_moderados))
            .group_by('persona_1', 'persona_2')
            .order_by('cantidad_mensajes', 'persona_1', 'persona_2')  # Ordena por cantidad de mensajes
            .all()
        )

        # Crea un DataFrame con los resultados
        df_chats_moderados = pd.DataFrame(resultados)

        # Crea el archivo CSV y envíalo como respuesta
        nombre_archivo = f'reporte_chats_mod_{_id}.csv'
        df_chats_moderados.to_csv(nombre_archivo, index=False)

        return send_file(nombre_archivo, as_attachment=True)

    else:
        return None
    
@appadmin.route('/descargar_csv/<mod_id>')
def descargar_csv(mod_id):
    mod = Mod.query.filter_by(cuenta_id=mod_id).first()

    if mod and mod.linkcsv:
        # Puedes establecer el mimetype según el tipo de archivo que estás descargando
        mimetype = 'text/csv'
        # Utiliza send_file para enviar el archivo al cliente
        return send_file(mod.linkcsv, mimetype=mimetype, as_attachment=True)
    else:
        # Retorna una respuesta adecuada si el mod o el enlace no existen
        return jsonify({'mensaje': 'No se encontró el moderador o el enlace CSV'})
    

#generar csv general
@appadmin.route('/generar_csv')
def generar_csv():
    # Obtén los datos de la base de datos
    datos_cuentas = obtener_cuentas_por_dia()
    datos_cuentas_semana = obtener_cuentas_por_semana()
    datos_moderador = obtener_cantidad_moderadores()
    datos_cantidad_mensaje_semana = obtener_cantidad_mensajes_semana()
    datos_cantidad_mensaje_mes = obtener_cantidad_mensajes_mes()
    
    # Crea un DataFrame para cada conjunto de datos
    df_cuentas = pd.DataFrame(datos_cuentas)
    df_cuentas_semana = pd.DataFrame(datos_cuentas_semana)
    df_moderador = pd.DataFrame(datos_moderador)
    df_cantidad_mensaje_semana = pd.DataFrame(datos_cantidad_mensaje_semana)
    df_cantidad_mensaje_mes = pd.DataFrame(datos_cantidad_mensaje_mes)

    # Convierte los DataFrames a archivos CSV en memoria
    csv_cuentas = df_cuentas.to_csv(index=False)
    csv_cuentas_semana = df_cuentas_semana.to_csv(index=False)
    csv_moderador = df_moderador.to_csv(index=False)
    csv_cantidad_mensaje_semana = df_cantidad_mensaje_semana.to_csv(index=False)
    csv_cantidad_mensaje_mes = df_cantidad_mensaje_mes.to_csv(index=False)

    # Combina los archivos CSV en uno solo
    csv_combinado = (
        f'Cuentas al dia:\n{csv_cuentas}\n\n'
        f'Cuentas a la semana:\n{csv_cuentas_semana}\n\n'
        f'Cantidad de Chats moderados:\n{csv_moderador}\n\n'
        f'Cantidad de Mensajes (Semana):\n{csv_cantidad_mensaje_semana}\n\n'
        f'Cantidad de Mensajes (Mes):\n{csv_cantidad_mensaje_mes}'
    )

    # Crea un objeto BytesIO para almacenar el CSV en memoria
    csv_bytes = io.BytesIO(csv_combinado.encode('utf-8'))

    # Devuelve el archivo CSV al navegador para su descarga
    return send_file(
        csv_bytes,
        as_attachment=True,
        download_name='reporte_csv.csv',
        mimetype='text/csv'
    )

def obtener_cuentas_por_dia():
    # Obtén las cuentas de la base de datos
    cuentas = Cuenta.query.all()

    # Crea un diccionario para almacenar la cantidad de cuentas por día
    cuentas_por_dia = {}

    # Itera sobre las cuentas y cuenta la cantidad por día
    for cuenta in cuentas:
        fecha_registro = cuenta.registered_on.date()  # Obtén solo la fecha sin la hora
        cuentas_por_dia[fecha_registro] = cuentas_por_dia.get(fecha_registro, 0) + 1

    # Convierte el diccionario a una lista de diccionarios
    datos = [{'Fecha': fecha, 'Cantidad_Cuentas': cantidad} for fecha, cantidad in cuentas_por_dia.items()]

    return datos

def obtener_cuentas_por_semana():
    # Obtén la fecha actual
    fecha_actual = datetime.now()

    # Resta 7 días a la fecha actual para obtener la fecha de inicio de la semana
    fecha_inicio_semana = fecha_actual - timedelta(days=7)

    # Consulta la base de datos para obtener la cantidad de cuentas por semana
    datos_cuentas = (
        Cuenta.query
        .with_entities(
            func.date_trunc('week', Cuenta.registered_on).label('semana'),
            func.count().label('cantidad_cuentas')
        )
        .filter(Cuenta.registered_on >= fecha_inicio_semana)
        .group_by('semana')
        .all()
    )

    # Convierte los resultados en un formato adecuado para el DataFrame
    datos_formateados = [{'Semana': str(fila.semana), 'Cantidad Cuentas': fila.cantidad_cuentas} for fila in datos_cuentas]

    return datos_formateados

def obtener_cantidad_moderadores():
    moderadores = Mod.query.all()

    # Diccionario para almacenar la cantidad de chats por moderador
    cantidad_chats_por_moderador = defaultdict(int)

    for mod in moderadores:
        # Obtiene la cantidad de chats en los que el moderador está involucrado
        cantidad_chats = Chat.query.filter_by(mod_id=mod.id_mod).count()

        # Agrega la información al diccionario
        cantidad_chats_por_moderador[mod.cuenta.email] = cantidad_chats

    # Convierte el diccionario a una lista de diccionarios para el formato deseado
    moderadores_info = [
        {
            'Correo': correo,
            'Numero de mensajes': cantidad_chats
        }
        for correo, cantidad_chats in cantidad_chats_por_moderador.items()
    ]

    return moderadores_info




def obtener_cantidad_mensajes_semana():
    # Usa la función func.date_trunc para truncar las fechas al comienzo de la semana
    mensajes_semana = db.session.query(
        func.date_trunc('week', Mensaje.fecha).label('semana'),
        Mensaje.usuario_rem,
        Mensaje.usuario_dest,
        func.count().label('cantidad')
    ).group_by('semana', Mensaje.usuario_rem, Mensaje.usuario_dest).all()

    # Diccionario para almacenar la cantidad total de mensajes entre cada par de usuarios
    cantidad_mensajes_por_usuario = defaultdict(int)

    for mensaje in mensajes_semana:
        # Crea una clave única para identificar la pareja de usuarios
        clave_usuarios = frozenset([mensaje.usuario_rem, mensaje.usuario_dest])

        # Agrega la cantidad de mensajes al total acumulado
        cantidad_mensajes_por_usuario[clave_usuarios] += mensaje.cantidad

    # Convierte el diccionario a una lista de diccionarios para el formato deseado
    mensajes_info = [
        {
            'Cantidad de Mensajes': cantidad,
            'Usuarios': ', '.join(usuarios)
        }
        for usuarios, cantidad in cantidad_mensajes_por_usuario.items()
    ]

    return mensajes_info


def obtener_cantidad_mensajes_mes():
    # Usa la función func.date_trunc para truncar las fechas al comienzo del mes
    mensajes_mes = db.session.query(
        func.date_trunc('month', Mensaje.fecha).label('mes'),
        Mensaje.usuario_rem,
        Mensaje.usuario_dest,
        func.count().label('cantidad')
    ).group_by('mes', Mensaje.usuario_rem, Mensaje.usuario_dest).all()

    # Diccionario para almacenar la cantidad total de mensajes entre cada par de usuarios
    cantidad_mensajes_por_usuario = defaultdict(int)

    for mensaje in mensajes_mes:
        # Crea una clave única para identificar la pareja de usuarios
        clave_usuarios = frozenset([mensaje.usuario_rem, mensaje.usuario_dest])

        # Agrega la cantidad de mensajes al total acumulado
        cantidad_mensajes_por_usuario[clave_usuarios] += mensaje.cantidad

    # Convierte el diccionario a una lista de diccionarios para el formato deseado
    mensajes_info = [
        {
            'Cantidad de Mensajes': cantidad,
            'Usuarios': ', '.join(usuarios)
        }
        for usuarios, cantidad in cantidad_mensajes_por_usuario.items()
    ]

    return mensajes_info