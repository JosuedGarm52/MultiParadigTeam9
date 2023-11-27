from flask import Flask, Blueprint,request,jsonify,render_template,redirect
from auth import tokenCheck,verificar
from app import db,bcrypt
from models import Perfil, Cuenta,Mod,Admin
from sqlalchemy import exc 
from utils import encode_auth_token, decode_auth_token


app = Flask(__name__)

appadmin = Blueprint('admin', __name__, template_folder='templates', static_folder='static', static_url_path='/main/static')

@appadmin.route('/')
def index():
    return render_template('admin.html')#cambiar al adaptado

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
                (Cuenta.primer_apellido.ilike(f'%{texto_busqueda}%'))
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
            ]
        else:
            # Obtén todas las cuentas
            todas_las_cuentas = Cuenta.query.all()

            for cuenta in todas_las_cuentas:
                cuenta_id = cuenta.id_cuenta

                # Verifica si existe una relación con el perfil
                perfil = Perfil.query.filter_by(cuenta_id=cuenta_id).first()

                # Verifica si existe una relación con el administrador
                admin = Admin.query.filter_by(cuenta_id=cuenta_id).first()

                # Verifica si existe una relación con el moderador
                mod = Mod.query.filter_by(cuenta_id=cuenta_id).first()

                # Si no tiene ninguna relación, agrega la información a la lista
                if perfil is None and admin is None and mod is None:
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
        # Maneja cualquier error que pueda ocurrir durante la búsqueda
        print(f"Error al buscar cuentas: {str(e)}")
        return jsonify({'error': 'Error al buscar cuentas'}), 500

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