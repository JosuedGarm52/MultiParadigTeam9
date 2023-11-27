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
from pyngrok import ngrok
import os


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

# Agrega el siguiente código para exponer tu aplicación a través de Ngrok
def create_ngrok_tunnel():
    # Obtén el puerto en el que se ejecutará tu aplicación Flask localmente
    # Esto debe coincidir con el puerto configurado en tu aplicación Flask
    port = int(os.environ.get("PORT", 5000))

    # Configura el túnel Ngrok en el puerto especificado
    public_url = ngrok.connect(port)
    print(' * ngrok tunnel "{}" -> "http://127.0.0.1:{}/"'.format(public_url, port))


# Ejecuta la función para crear el túnel Ngrok cuando la aplicación se inicia en modo de desarrollo
if __name__ == '__main__':
    # Llama a la función para crear el túnel Ngrok
    create_ngrok_tunnel()

    # Inicia tu aplicación Flask normalmente
    app.run(debug=True)