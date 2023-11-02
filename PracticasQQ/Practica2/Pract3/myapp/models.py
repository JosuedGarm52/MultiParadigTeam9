from app import db

#formulario
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    direccion = db.Column(db.String(250))
    edad = db.Column(db.Integer)

class Vendedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    num_iden_ven = db.Column(db.String(250))
    fecha_inicio = db.Column(db.DateTime)
    num_telefono = db.Column(db.String(250))

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(250))
    valor = db.Column(db.Float)  
    categoria = db.Column(db.String(100))
    fecha = db.Column(db.DateTime)
    cantidad = db.Column(db.Integer)
    
