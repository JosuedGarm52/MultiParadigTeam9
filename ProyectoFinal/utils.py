import jwt
import datetime
from config import BaseConf

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