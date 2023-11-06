from app import db

class Juguete(db.Model): #Declarar una tabla Juguete. ESTA ENTIDAD LA MANEJAREMOS CON FORMULARIOS
    id = db.Column(db.Integer,primary_key=True) #Declarar un ID, la columna principal
    nombrejuguete = db.Column(db.String(250))
    nombreproveedor = db.Column(db.String(250))
    precioventa = db.Column(db.Integer)
    cantprodvendidos = db.Column(db.Integer)

#Agregar otras clases más
class Ciudad(db.Model):
    id = db.Column(db.Integer,primary_key=True) #Declarar un ID, la columna principal
    nombreciudad = db.Column(db.String(250))
    estadociudad = db.Column(db.String(250))
    paisciudad = db.Column(db.String(250))
    poblaciontotal = db.Column(db.Integer)

class Coche(db.Model):
    id = db.Column(db.Integer,primary_key=True) #Declarar un ID, la columna principal
    marcacoche = db.Column(db.String(250))
    modelocoche = db.Column(db.String(250))
    paisorigen = db.Column(db.String(250))
    color = db.Column(db.String(250))

class Mascota(db.Model):
    id = db.Column(db.Integer,primary_key=True) #Declarar un ID, la columna principal
    nombremascota = db.Column(db.String(250))
    razamascota = db.Column(db.String(250))
    colormascota = db.Column(db.String(250))
    edadmascota = db.Column(db.Integer)

class Profesor(db.Model):
    id = db.Column(db.Integer,primary_key=True) #Declarar un ID, la columna principal
    nombreprofesor = db.Column(db.String(250))
    apellidosprofesor = db.Column(db.String(250))
    materiaprofesor = db.Column(db.String(250))
    correoprofesor = db.Column(db.String(250))
