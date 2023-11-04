from flask import Blueprint,request,redirect,render_template,url_for, jsonify
from models import Agencia
from app import db

appAgencia = Blueprint('appagencia', __name__, template_folder="templates")
APP_BASE = 'agencia'

@appAgencia.route(f'/{APP_BASE}/agregar',methods = ["GET","POST"])
def agregar():
    try:
        json = request.get_json()
        agencia = Agencia()
        agencia.nombre = json['nombre']
        agencia.num_telef = json['num_telef']
        db.session.add(agencia)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Agencia"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appAgencia.route(f"/{APP_BASE}/editar",methods=["POST"])
def editar():
    try:
        json = request.get_json()
        agencia = Agencia.query.get_or_404(json["id"])
        agencia.nombre = json['nombre']
        agencia.num_telef = json['num_telef']
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Agencia modificar"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appAgencia.route(f"/{APP_BASE}/eliminar",methods=["POST"])
def eliminar():
    try:
        json = request.get_json()
        agencia = Agencia.query.get_or_404(json["id"])
        db.session.delete(agencia)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Agencia eliminado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appAgencia.route(f'/{APP_BASE}/obtener',methods=["GET"])
def obtenerAgencia():
    try:
        agencias = Agencia.query.all()
        listaAgencias = []
        for p in agencias:
                lagencia = {}
                lagencia["id"] = p.id
                lagencia["nombre"] = p.nombre
                lagencia["num_telef"] = p.num_telef
                listaAgencias.append(lagencia)
        return jsonify({"producto":listaAgencias})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})