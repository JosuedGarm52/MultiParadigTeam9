from flask import Flask
from database import db
from config import BasicConfig
from flask_migrate import Migrate
import logging
from routes.juguete.juguetes import appjuguete
from routes.ciudad.ciudad import appciudad
from routes.coche.coche import appcoche
from routes.mascota.mascota import appmascota
from routes.profesor.profesor import approfesor

app = Flask(__name__)
app.register_blueprint(appjuguete) #Traer toda la información del Blueprint que acabamos de crear
app.register_blueprint(appciudad)
app.register_blueprint(appcoche)
app.register_blueprint(appmascota)
app.register_blueprint(approfesor)

app.config.from_object(BasicConfig) #Traer toda la configuración de la aplicación
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="logs.log")
