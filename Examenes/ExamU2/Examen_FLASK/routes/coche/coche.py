from flask import Blueprint,jsonify,request
from models import Coche
from app import db

appcoche = Blueprint("appcoche",__name__)
@appcoche.route('/coche/agregar',methods=["POST"]) #Cuidado con el nombre de las rutas, no puede haber dos rutas con nombre 'agregar' en el mismo proyecto
def agregarCoche(): #Método para agregar producto
    try:
        json = request.get_json() #Lo convierte en un diccionario
        coche = Coche() #Crear un producto nuevo
        coche.marcacoche = json['marcacoche']
        coche.modelocoche = json['modelocoche']
        coche.paisorigen = json['paisorigen']
        coche.color = json['color']
        db.session.add(coche)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Coche agregado exitósamente"}) #Respuesta valida
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex}) #XML Moderno, EDI - Electronic Data Interchange

@appcoche.route('/coche/editar',methods=["POST"]) #Cuidado con el nombre de las rutas, no puede haber dos rutas con nombre 'agregar' en el mismo proyecto
def editarCoche(): #Método para agregar producto
    try:
        json = request.get_json() #Lo convierte en un diccionario
        coche = Coche.query.get_or_404(json["id"])
        coche.marcacoche = json['marcacoche']
        coche.modelocoche = json['modelocoche']
        coche.paisorigen = json['paisorigen']
        coche.color = json['color']
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Coche modificado exitósamente"}) #Respuesta valida
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex}) #XML Moderno, EDI - Electronic Data Interchange

@appcoche.route('/coche/eliminar',methods=["POST"]) #Cuidado con el nombre de las rutas, no puede haber dos rutas con nombre 'agregar' en el mismo proyecto
def eliminarCoche(): #Método para agregar producto
    try:
        json = request.get_json()
        coche = Coche.query.get_or_404(json["id"])
        db.session.delete(coche)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Coche eliminado exitósamente"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex}) #XML Moderno, EDI - Electronic Data Interchange

@appcoche.route('/coche/obtener')
def obtenerCoches():
    coches = Coche.query.all()
    listaCoches = []
    for p in coches:
        coche = {} #Diccionario vacio
        coche["marcacoche"] = p.marcacoche
        coche["modelocoche"] = p.modelocoche
        coche["paisorigen"] = p.paisorigen
        coche["color"] = p.color
        listaCoches.append(coche)
    return jsonify({'Coches':listaCoches})
