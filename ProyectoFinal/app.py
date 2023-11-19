from flask import Flask
from flask_cors import CORS
from database import db
from encriptador import bcrypt  
from flask_migrate import Migrate
from config import BaseConf
from routes.main.main import appmain

app=Flask(__name__)
app.register_blueprint(appmain)
app.config.from_object(BaseConf)
CORS(app) 
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)