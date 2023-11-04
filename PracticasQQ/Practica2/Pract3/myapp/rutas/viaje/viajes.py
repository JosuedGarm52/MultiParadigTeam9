from flask import Blueprint,request,redirect,render_template,url_for,jsonify
from models import Viaje
from app import db

appViaje = Blueprint('appviaje', __name__, template_folder="templates")
APP_BASE = 'viaje'


@appViaje.route(f'/{APP_BASE}/agregar',methods = ["GET","POST"])
def agregar():
    try:
        json = request.get_json()
        viaje= Viaje()
        viaje.nombre = json['nombre']
        viaje.destino = json['destino']
        db.session.add(viaje)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Viaje"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appViaje.route(f"/{APP_BASE}/editar",methods=["POST"])
def editar():
    try:
        json = request.get_json()
        viaje = Viaje.query.get_or_404(json["id"])
        viaje.nombre = json['nombre']
        viaje.destino = json['destino']
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Viaje modificar"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appViaje.route(f"/{APP_BASE}/eliminar",methods=["POST"])
def eliminar():
    try:
        json = request.get_json()
        viaje = Viaje.query.get_or_404(json["id"])
        db.session.delete(viaje)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Viaje eliminado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appViaje.route(f'/{APP_BASE}/obtener',methods=["GET"])
def obtenerViaje():
    try:
        viajes = Viaje.query.all()
        listaAgencias = []
        for p in viajes:
                lviaje = {}
                lviaje["id"] = p.id
                lviaje["nombre"] = p.nombre
                lviaje["destino"] = p.destino
                listaAgencias.append(lviaje)
        return jsonify({"producto":listaAgencias})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})