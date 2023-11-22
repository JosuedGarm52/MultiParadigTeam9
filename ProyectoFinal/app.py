from flask import Flask
from flask_cors import CORS
from database import db
from encriptador import bcrypt  
from flask_migrate import Migrate
from config import BaseConf
from routes.main.main import appmain
from routes.User.Users import appuser
from routes.Admin.admins import appadmin
from routes.Mod.Mods import appmod

app=Flask(__name__)
app.register_blueprint(appmain)
app.register_blueprint(appuser, url_prefix='/usuarios')
app.register_blueprint(appadmin, url_prefix='/admin')
app.register_blueprint(appmod, url_prefix='/mod')
app.config.from_object(BaseConf)
CORS(app) 
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)