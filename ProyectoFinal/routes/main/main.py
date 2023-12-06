from flask import Flask, Blueprint,request,jsonify,render_template,redirect
from auth import tokenCheck,verificar
from app import db,bcrypt
from models import Perfil, Cuenta,Mod,Admin, Noticia
from sqlalchemy import exc 
from utils import encode_auth_token, decode_auth_token

app = Flask(__name__)

appmain = Blueprint('main', __name__, template_folder='templates', static_folder='static', static_url_path='/main/static')

@appmain.route('/', methods=['GET','POST'])
def index():
    if request.method == "GET":
        image_urls = [
            "https://media.istockphoto.com/id/514472018/es/foto/hermosa-boda-par-abrazar-cerca-de-columnas.jpg?s=612x612&w=0&k=20&c=uNaI5B3WpsnZVff6l6jvyhZMXd-DIkQl7ZCjO2W92K0=",
            "https://media.istockphoto.com/id/498477061/es/foto/siente-el-d%C3%ADa-de-su-boda-bliss.jpg?s=612x612&w=0&k=20&c=kYex3_JmNNEz6CdYfclcwKjxj2GGln-NU9QyXKdlb5Y=",
            "https://media.istockphoto.com/id/530188882/es/foto/retrato-de-una-joven-pareja-de-novios.jpg?s=612x612&w=0&k=20&c=SeUr9mYN6ZJ1phUPg05577uSMtO8-u4bSgcda-DfAus="
        ]
        noticias = Noticia.query.all()
        info_list = [
            {
                'image_url': noticia.url if noticia.url 
                else 'https://upload.wikimedia.org/wikipedia/commons/a/a3/Image-not-found.png',
                'text1': noticia.text1,
                'text2': noticia.text2
            }
            for noticia in noticias
        ]
        
        return render_template('main.html', image_urls=image_urls, info_list=info_list)
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

        except ValueError as e:
            return jsonify({'status': 'error', 'message': f'Error al desencriptar el token: {str(e)}'})

        if cuenta_id:
            # Consultar admin
            admin = Admin.query.filter_by(cuenta_id=cuenta_id).first()
            cuentax = Cuenta.query.filter_by(id_cuenta = cuenta_id).first()
            if admin:
                return jsonify({
                    'status': 'success',
                    'rol': 'administrador',
                    'email': cuentax.email  # Obtén el email desde la cuenta asociada al admin
                })

            # Consultar mod
            mod = Mod.query.filter_by(cuenta_id=cuenta_id).first()
            if mod:
                return jsonify({
                    'status': 'success',
                    'rol': 'moderador',
                    'email': mod.cuenta.email  # Obtén el email desde la cuenta asociada al mod
                })
            
            # Consultar el perfil
            cuenta = Cuenta.query.filter_by(id_cuenta = cuenta_id).first()
            if cuenta:
                perfil = Perfil.query.filter_by(cuenta_id = cuenta.id_cuenta).first()
                
                if perfil:
                    return jsonify({
                        'status': 'success',
                        'rol': 'casanova',
                        'email': perfil.usuario
                    })
            cuenta = Cuenta.query.filter_by(id_cuenta = cuenta_id).first()
            if cuenta:
                    nombre_componentes = [
                        cuenta.primer_nombre,
                        cuenta.otros_nombres,
                        cuenta.primer_apellido,
                        cuenta.segundo_apellido,
                    ]

                    # Filtrar los componentes que no son None
                    nombre_no_none = [componente for componente in nombre_componentes if componente is not None]

                    # Unir los componentes con un espacio en blanco
                    nombre_completo = " ".join(nombre_no_none)
                    return jsonify({
                        'status': 'success',
                        'rol': 'pendiente',
                        'email': nombre_completo
                    })
        return jsonify({'status': 'error', 'message': 'No se encontro el rol'})


def verificar_credenciales(principal, contra):
    # Buscar el usuario por correo electrónico en la tabla Cuenta
    cuenta = Cuenta.query.filter_by(email=principal.lower().strip()).first()

    if cuenta and bcrypt.check_password_hash(cuenta.password, contra):
        return True, cuenta
    else:
        # Si no se encontró en la tabla Cuenta, buscar en la tabla Perfil por usuario
        perfil = Perfil.query.filter_by(usuario=principal).first()

        if perfil and perfil.cuenta_id is not None:
            # Si se encuentra el perfil y tiene un cuenta_id válido, obtener la cuenta
            cuenta = Cuenta.query.filter_by(id_cuenta=perfil.cuenta_id).first()
            if cuenta and bcrypt.check_password_hash(cuenta.password, contra):
                return True, cuenta

    return False, None



@appmain.route('/login',methods=["GET","POST"])
def login_post():
    if(request.method=="GET"):
        token = request.args.get('cuenta_id')
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
                responseObject = {
                    'status' : 'fail',
                    'message': 'Credenciales incompletas'
                }
                return jsonify(responseObject), 403

            success, cuenta = verificar_credenciales(principal, contra)

            if success:
                _id = cuenta.id_cuenta
                auth_token = cuenta.encode_auth_token(user_id=_id)
                responseObject = {
                    'status': 'success',
                    'login': 'Inicio de sesión exitoso',
                    'auth_token': auth_token
                }
                return jsonify(responseObject), 203
            else:
                # Usuario no encontrado o contraseña incorrecta
                responseObject = {
                    'status' : 'fail',
                    'message': 'Credenciales incorrectas'
                }
                return jsonify(responseObject), 403
        except Exception as e:
            return jsonify({'message': str(e)}), 503

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
        email=request.json['correo'].lower().strip()
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
                'message':'usuario existente con ese correo'
            }
        return jsonify(responseObject)
    
@appmain.route('/terminos-y-condiciones',methods=["GET","POST"])
def terminos():
     return render_template('terminos-y-condiciones.html')

@appmain.route('/procedimientos',methods=["GET","POST"])
def proceso():
     return render_template('procedimientos.html')