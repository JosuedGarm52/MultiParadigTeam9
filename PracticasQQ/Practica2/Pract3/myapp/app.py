from flask import Flask
from database import db
from config import BasicConf
from flask_migrate import Migrate
import logging

app = Flask(__name__)
app.config.from_object(BasicConf)
db.init_app(app)
migrate =Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="logs.log")