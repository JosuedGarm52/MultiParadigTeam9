from models import Cuenta
from functools import wraps 
from flask import jsonify, request

def obtenerInfo(token):
    if token:
        resp = Cuenta.decode_auth_token(token)
        user = Cuenta.query.filter_by(id=resp).first()
        if user:
            usuario = {
                'status':'success',
                'data':{
                    'id_cuenta':user.id,
                    'email':user.email,
                    'admin':user.admin,
                    'pnombre':user.primer_nombre,
                    'snombre':user.otro_nombre,
                    'papellido':user.primer_apellido,
                    'sapellido':user.segundo_apellido,
                    'fnacimiento':user.fecha_nacimiento,
                    'correo':user.email,
                    'Telef':user.telefono,
                    'password':user.password,
                    'registered_on':user.registered_on
                }
            }
            return usuario
        else:
            error = {
                'status':'fail',
                'message':resp
            }
            return error
        
def tokenCheck(f):
    @wraps(f)
    def verificar(*args,**kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']
        if not token:
            return jsonify({'message':'Token no encontrado'})
        try:
            info = obtenerInfo(token)
            print(info) 
            if info['status'] == 'fail':
                return jsonify({'message':'token invalido'})
        except:
            return jsonify({'message':'error'})
        return f(info['data'],*args,**kwargs)
    return verificar

def verificar(token):
    if not token:
        return jsonify({'message':'Token no encontrado'})
    try:
        info = obtenerInfo(token)
        if info['status'] == 'fail':
            return jsonify({'message':'token invalido'})
    except:
        return jsonify({'message':'error'})
    return info