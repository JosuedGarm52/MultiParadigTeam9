from flask import Flask, Blueprint,request,jsonify,render_template,redirect
from auth import tokenCheck,verificar
from app import db,bcrypt
from models import Perfil, Cuenta
from sqlalchemy import exc 

app = Flask(__name__)

appmain = Blueprint('main', __name__, template_folder='templates', static_folder='static', static_url_path='/main/static')

@appmain.route('/')
def index():
    image_urls = [
        "https://media.istockphoto.com/id/514472018/es/foto/hermosa-boda-par-abrazar-cerca-de-columnas.jpg?s=612x612&w=0&k=20&c=uNaI5B3WpsnZVff6l6jvyhZMXd-DIkQl7ZCjO2W92K0=",
        "https://media.istockphoto.com/id/498477061/es/foto/siente-el-d%C3%ADa-de-su-boda-bliss.jpg?s=612x612&w=0&k=20&c=kYex3_JmNNEz6CdYfclcwKjxj2GGln-NU9QyXKdlb5Y=",
        "https://media.istockphoto.com/id/530188882/es/foto/retrato-de-una-joven-pareja-de-novios.jpg?s=612x612&w=0&k=20&c=SeUr9mYN6ZJ1phUPg05577uSMtO8-u4bSgcda-DfAus="
    ]
    info_list = [
        {
            'image_url': 'https://media.istockphoto.com/id/1303804576/es/foto/nuestro-primer-baile.jpg?s=612x612&w=0&k=20&c=imONv7gNEBiPlOw-s_odejgfIaZ9QEI7eoBqmT0gVmM=',
            'text1': 'El amor es el idioma que todos entendemos.',
            'text2': 'El amor, esa fuerza mágica que impulsa a la humanidad, es un viaje intrincado de emociones, experiencias y compromisos. Va más allá de las palabras, manifestándose en pequeños gestos cotidianos y en los momentos extraordinarios que compartimos.'
        },
    ]
    return render_template('main.html', image_urls=image_urls, info_list=info_list)


def verificar_credenciales(principal, contra):
    # Buscar el usuario por nombre de usuario o correo electrónico
    searchUser = Perfil.query.join(Perfil.cuenta).filter(
        (Perfil.usuario == principal) | (Cuenta.email == principal)
    ).first()

    if searchUser and bcrypt.check_password_hash(searchUser.cuenta.password, contra):
        return True, searchUser
    else:
        return False, None

@appmain.route('/login',methods=["GET","POST"])
def login_post():
    if(request.method=="GET"):
        token = request.args.get('token')
        if token:
            info = verificar(token)
            if(info['status']!="fail"):
                responseObject={
                    'status':"success",
                    'message':'valid token',
                    'info':info
                }
                return jsonify(responseObject)
        return render_template('login.html')
    else:
        try:
            principal = request.json.get('principal')
            contra = request.json.get('contra')

            if not principal or not contra:
                return jsonify({'message': 'Credenciales incompletas'}), 400

            success, user = verificar_credenciales(principal, contra)

            if success:
                auth_token = user.cuenta.encode_auth_token(user_id=user.id)
                responseObject = {
                    'status': 'success',
                    'login': 'Inicio de sesión exitoso',
                    'auth_token': auth_token.decode()  # Decodificar el token si es necesario
                }
                return jsonify(responseObject), 200
            else:
                # Usuario no encontrado o contraseña incorrecta
                return jsonify({'message': 'Credenciales incorrectas'}), 401
        except Exception as e:
            return jsonify({'message': str(e)}), 500

@appmain.route('/register')
def registro():
    return render_template('registro.html')

@appmain.route('/cuenta',methods=["GET","POST"])
def registro_post():
    if request.method=="GET":
        return render_template('register.html')
    else:
        primer_nombre = request.json['pnombre']
        otro_nombre = request.json['snombre'] #opcional
        primer_apellido = request.json['papellido']
        segundo_apellido = request.json['sapellido'] #opcional
        fecha = request.json['fnacimiento']
        email=request.json['correo']
        telefono = request.json['Telef'] #opcional
        password=request.json['password']
        usuario = Cuenta(primer_nombre=primer_nombre,otros_nombres=otro_nombre, primer_apellido=primer_apellido, segundo_apellido= segundo_apellido, fecha_nacimiento=fecha, telefono= telefono, email=email, password=password)
        userExists = Cuenta.query.filter_by(email=email).first()

        # Verificar si hay valores None y cambiarlos a cadena vacía
        otro_nombre = otro_nombre if otro_nombre is not None else ''
        segundo_apellido = segundo_apellido if segundo_apellido is not None else ''
        telefono = telefono if telefono is not None else ''

        if not userExists:
            try:
                db.session.add(usuario)
                db.session.commit()
                auth_token = usuario.encode_auth_token(user_id=usuario.id_cuenta)
                responseObject={
                    'status':'success',
                    'message':"Registro exitoso",
                    'cuenta_id': auth_token
                }
            except exc.SQLAlchemyError as e:
                responseObject={
                    'status':'error',
                    'message':e
                }
        else:
            responseObject={
                'status':'error',
                'message':'usuario existente'
            }
        return jsonify(responseObject)