from app import db

#formulario
class Cliente(db.Model):
    #diferencia de django si se declara id
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    direccion = db.Column(db.String(250))
    edad = db.Column(db.Integer)