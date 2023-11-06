from flask import Blueprint,jsonify,request
from models import Ciudad
from app import db

appciudad = Blueprint("appciudad",__name__)
@appciudad.route('/ciudad/agregar',methods=["POST"]) #Cuidado con el nombre de las rutas, no puede haber dos rutas con nombre 'agregar' en el mismo proyecto
def agregarCiudad(): #Método para agregar producto
    try:
        json = request.get_json() #Lo convierte en un diccionario
        ciudad = Ciudad() #Crear un producto nuevo
        ciudad.nombreciudad = json['nombreciudad']
        ciudad.estadociudad = json['estadociudad']
        ciudad.paisciudad = json['paisciudad']
        ciudad.poblaciontotal = json['poblaciontotal']
        db.session.add(ciudad)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Ciudad agregada exitósamente"}) #Respuesta valida
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex}) #XML Moderno, EDI - Electronic Data Interchange

@appciudad.route('/ciudad/editar',methods=["POST"]) #Cuidado con el nombre de las rutas, no puede haber dos rutas con nombre 'agregar' en el mismo proyecto
def editarCiudad(): #Método para agregar producto
    try:
        json = request.get_json() #Lo convierte en un diccionario
        ciudad = Ciudad.query.get_or_404(json["id"])        
        ciudad.nombreciudad = json['nombreciudad']
        ciudad.estadociudad = json['estadociudad']
        ciudad.paisciudad = json['paisciudad']
        ciudad.poblaciontotal = json['poblaciontotal']
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Ciudad modificada exitósamente"}) #Respuesta valida
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex}) #XML Moderno, EDI - Electronic Data Interchange

@appciudad.route('/ciudad/eliminar',methods=["POST"]) #Cuidado con el nombre de las rutas, no puede haber dos rutas con nombre 'agregar' en el mismo proyecto
def eliminarCiudad(): #Método para agregar producto
    try:
        json = request.get_json()
        ciudad = Ciudad.query.get_or_404(json["id"])
        db.session.delete(ciudad)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Ciudad eliminada exitósamente"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex}) #XML Moderno, EDI - Electronic Data Interchange

@appciudad.route('/ciudad/obtener')
def obtenerCiudades():
    ciudades = Ciudad.query.all()
    listaCiudades = []
    for p in ciudades:
        ciudad = {} #Diccionario vacio
        ciudad["nombreciudad"] = p.nombreciudad
        ciudad["estadociudad"] = p.estadociudad
        ciudad["paisciudad"] = p.paisciudad
        ciudad["poblaciontotal"] = p.poblaciontotal
        listaCiudades.append(ciudad)
    return jsonify({'Ciudades':listaCiudades})
