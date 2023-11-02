from flask import Flask
from database import db
from config import BasicConf
from flask_migrate import Migrate
from rutas.cliente.clientes import appCliente
from rutas.vendedor.vendedores import appVendedor
from rutas.venta.ventas import appVenta
import logging

app = Flask(__name__)
app.register_blueprint(appCliente)
app.register_blueprint(appVendedor)
app.register_blueprint(appVenta)
app.config.from_object(BasicConf)
db.init_app(app)
migrate = Migrate(app, db)
logging.basicConfig(level=logging.DEBUG,filename="logs.log")