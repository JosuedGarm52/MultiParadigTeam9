import jwt
import datetime
from config import BaseConf
from flask import jsonify

def encode_auth_token(user_id):
        try:
            payload={
                'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=5),
                'iat':datetime.datetime.utcnow(),
                'sub':user_id 
            }

            return jwt.encode(
                payload,
                BaseConf.SECRET_KEY,
                algorithm = 'HS256'
            )
        except Exception as e:
            return e    
        
@staticmethod
def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token,BaseConf.SECRET_KEY, algorithms = ['HS256'])#algorithms es plural y diferente al encode
            return payload
        except jwt.ExpiredSignatureError as e:
            return 'Signature Expired please log in again'
        
        except jwt.InvalidTokenError as e:
            return 'Invalid Token'      
        
def verificarID(valor):
    try:
        token = valor
        # Decodificar el token para obtener la información
        decoded_token = decode_auth_token(token)
        # Acceder al valor del campo "sub"
        if 'sub' in decoded_token:
            sub_value = decoded_token['sub']
            cuenta_id = int(sub_value)
            return cuenta_id
        else:
            raise ValueError('El campo "sub" no está presente en el token')
    except jwt.ExpiredSignatureError as e:
        return jsonify({'status': 'error', 'message': f'Error de token: {str(e)}'})
    except jwt.InvalidTokenError as e:
        return jsonify({'status': 'error', 'message': f'Error de token: {str(e)}'})
    except ValueError as e:
        return jsonify({'status': 'error', 'message': f'El formato de cuenta_id no es válido: {str(e)}'})
    
def sanitize_local_link(enlace):
    # Elimina caracteres no permitidos para enlaces locales
    caracteres_prohibidos = r'*"<>|'
    enlace_saneado = ''.join(c for c in enlace if c not in caracteres_prohibidos)

    # Asegúrate de que no tenga el prefijo "file:///"
    if enlace_saneado.lower().startswith('file:///'):
        enlace_saneado = enlace_saneado[len('file:///'):]

    return enlace_saneado


