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
    email = db.Column(db.String(255), nullable=False)#req
    password = db.Column(db.String(255),nullable = False)#req
    registered_on= db.Column(db.DateTime,nullable=False)

    def __init__(self, primer_nombre, otros_nombres, primer_apellido, segundo_apellido, fecha_nacimiento, telefono, email, password) -> None:
        self.primer_nombre = primer_nombre
        self.otros_nombres = otros_nombres
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, BaseConf.BCRYPT_LOG_ROUNDS
        ).decode()
        self.registered_on = datetime.datetime.now()

    @staticmethod
    def encode_auth_token(user_id):
        return encode_auth_token(user_id)

    @staticmethod
    def decode_auth_token(auth_token):
        return decode_auth_token(auth_token)

class Perfil(db.Model):
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
    
class Foto(db.Model):
    __tablename__="foto"
    id_foto=db.Column(db.Integer,primary_key = True, autoincrement = True)
    link = db.Column(db.String(255), nullable=False)#req

    def __init__(self, id_foto, link) -> None:
        self.id_foto = id_foto
        self.link = link

class Perfil_Foto(db.Model):
    __tablename__= "perfil_foto"
    usuario_name = db.Column(db.String(255), db.ForeignKey('perfil.usuario'), primary_key=True)
    foto_id = db.Column(db.Integer, db.ForeignKey('foto.id_foto'), primary_key=True)
    isperfil = db.Column(db.Boolean, nullable=False, default=True)#req
    
    usuario = db.relationship('Perfil', backref=db.backref('perfil_fotos', lazy=True))
    
    foto = db.relationship('Foto', backref=db.backref('perfil_fotos', lazy=True))

    def __init__(self, usuario_name, foto_id, isperfil=True) -> None:
        self.usuario_name = usuario_name
        self.foto_id = foto_id
        self.isperfil = isperfil

class Admin(db.Model):
    __tablename__= "admin"
    id_admin = db.Column(db.Integer,primary_key = True, autoincrement = True)
    cuenta_id = db.Column(db.Integer, db.ForeignKey('cuenta.id_cuenta'), nullable=False)
    
    def __init__(self, id_admin,cuenta_id):
        self.id_admin = id_admin
        self.cuenta_id = cuenta_id
    
class Mod(db.Model):
    __tablename__= "mod"

    id_mod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cuenta_id = db.Column(db.Integer, db.ForeignKey('cuenta.id_cuenta'), nullable=False)
    cuenta = db.relationship('Cuenta', backref=db.backref('mod', lazy=True))

    def __init__(self, id_cuenta,cuenta) -> None:
        self.cuenta_id = id_cuenta #checar esta parte
        self.cuenta = cuenta

class Mensaje(db.Model):
    __tablename__ = "mensaje"
    id_mensaje = db.Column(db.Integer, primary_key=True)
    usuario_rem = db.Column(db.String(255), db.ForeignKey('perfil.usuario'), nullable=False)
    usuario_dest = db.Column(db.String(255), db.ForeignKey('perfil.usuario'), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    contenido = db.Column(db.String, nullable=False)
    isvisible = db.Column(db.Boolean, nullable=False, default=True)
    isread = db.Column(db.Boolean, nullable=False, default=False)
    
    remitente = db.relationship('Perfil', foreign_keys=[usuario_rem])
    destinatario = db.relationship('Perfil', foreign_keys=[usuario_dest])

    def __init__(self, id_mensaje, usuario_rem, usuario_dest, fecha, contenido, isvisible, isread):
        self.id_mensaje = id_mensaje
        self.usuario_rem = usuario_rem
        self.usuario_dest = usuario_dest
        self.fecha = fecha
        self.contenido = contenido
        self.isvisible = isvisible
        self.isread = isread

class Chat(db.Model):
    __tablename__ = "chat"

    mensaje_id = db.Column(db.Integer, db.ForeignKey('mensaje.id_mensaje'), primary_key=True)
    mod_id = db.Column(db.Integer, db.ForeignKey('mod.id_mod'), primary_key=True)

    mensaje = db.relationship('Mensaje', backref=db.backref('chat', lazy=True))
    mod = db.relationship('Mod', backref=db.backref('chat', lazy=True))

    def __init__(self, id_mensaje, id_mod) -> None:
        self.mensaje_id = id_mensaje
        self.mod_id = id_mod

class Documento(db.Model):
    usuario_name = db.Column(db.String(255), db.ForeignKey('perfil.usuario'), primary_key=True, nullable=False)
    link = db.Column(db.String(255), nullable=False)  # req
    isaprobado = db.Column(db.Boolean, nullable=False, default=False)
    tipo = db.Column(db.String(255), nullable=False)  # req
    mod_id = db.Column(db.Integer, db.ForeignKey('mod.id_mod'), nullable=False)

    mod = db.relationship('Mod', backref=db.backref('documentos', lazy=True))

    def __init__(self, usuario_name, link, isaprobado, tipo, mod_id):
        self.usuario_name = usuario_name
        self.link = link
        self.isaprobado = isaprobado
        self.tipo = tipo
        self.mod_id = mod_id
