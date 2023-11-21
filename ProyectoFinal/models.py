import jwt 
import datetime
from config import BaseConf
from app import db, bcrypt
from utils import encode_auth_token, decode_auth_token

class Cuenta(db.Model):
    __tablename__="cuenta"
    id_cuenta=db.Column(db.Integer,primary_key = True, autoincrement = True)
    primer_nombre = db.Column(db.String(255), nullable=False)#req
    otros_nombres = db.Column(db.String(255), nullable=True)
    primer_apellido = db.Column(db.String(255), nullable=False)#req
    segundo_apellido = db.Column(db.String(255), nullable=True)
    fecha_nacimiento = db.Column(db.DateTime,nullable=False)#req
    telefono = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255),nullable = False)
    registered_on= db.Column(db.DateTime,nullable=False)

    def __init__(self, primer_nombre, otros_nombres, primer_apellido, segundo_apellido, fecha_nacimiento, telefono, password) -> None:
        self.primer_nombre = primer_nombre
        self.otros_nombres = otros_nombres
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.password = bcrypt.generate_password_hash(
            password, BaseConf.BCRYPT_LOG_ROUNDS
        ).decode()
        self.registered_on = datetime.datetime.now()


    def encode_auth_token(self, user_id):
        return encode_auth_token(user_id)

    @staticmethod
    def decode_auth_token(auth_token):
        return decode_auth_token(auth_token)

class Perfil(db.Models):
    __tablename__="perfil"
    usuario = db.Column(db.String(255),primary_key = True)
    pais_origen = db.Column(db.String(255), nullable=False)#req
    genero = db.Column(db.String(255), nullable=False)#req
    busqueda = db.Column(db.String(255), nullable=False)#req
    activo = db.Column(db.Boolean, nullable=False, default=True)#req
    estado_civil = db.Column(db.String(255), nullable=False, default="soltero")#req
    cuenta_id = db.Column(db.Integer, db.ForeignKey('cuenta.id_cuenta'), nullable=False)
    
    cuenta = db.relationship('Cuenta', backref=db.backref('perfil', lazy=True))

    def __init__(self, usuario, pais_origen, genero, busqueda, activo=True, estado_civil="soltero", cuenta_id=None) -> None:
        self.usuario = usuario
        self.pais_origen = pais_origen
        self.genero = genero
        self.busqueda = busqueda
        self.activo = activo
        self.estado_civil = estado_civil
        self.cuenta_id = cuenta_id
    
class Foto(db.Models):
    id_foto=db.Column(db.Integer,primary_key = True, autoincrement = True)
    link = db.Column(db.String(255), nullable=False)#req

    def __init__(self, id_foto, link) -> None:
        self.id_foto = id_foto
        self.link = link

