from flask import Blueprint,jsonify,request
from models import Mascota
from app import db

appmascota = Blueprint("appmascota",__name__)
@appmascota.route('/mascota/agregar',methods=["POST"]) #Cuidado con el nombre de las rutas, no puede haber dos rutas con nombre 'agregar' en el mismo proyecto
def agregarMascota(): #Método para agregar producto
    try:
        json = request.get_json() #Lo convierte en un diccionario
        mascota = Mascota() #Crear un producto nuevo
        mascota.nombremascota = json['nombremascota']
        mascota.razamascota = json['razamascota']
        mascota.colormascota = json['colormascota']
        mascota.edadmascota = json['edadmascota']
        db.session.add(mascota)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Mascota agregada exitósamente"}) #Respuesta valida
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex}) #XML Moderno, EDI - Electronic Data Interchange

@appmascota.route('/mascota/editar',methods=["POST"]) #Cuidado con el nombre de las rutas, no puede haber dos rutas con nombre 'agregar' en el mismo proyecto
def editarMascota(): #Método para agregar producto
    try:
        json = request.get_json() #Lo convierte en un diccionario
        mascota = Mascota.query.get_or_404(json["id"])
        mascota.nombremascota = json['nombremascota']
        mascota.razamascota = json['razamascota']
        mascota.colormascota = json['colormascota']
        mascota.edadmascota = json['edadmascota']
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Mascota modificada exitósamente"}) #Respuesta valida
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex}) #XML Moderno, EDI - Electronic Data Interchange

@appmascota.route('/mascota/eliminar',methods=["POST"]) #Cuidado con el nombre de las rutas, no puede haber dos rutas con nombre 'agregar' en el mismo proyecto
def eliminarMascota(): #Método para agregar producto
    try:
        json = request.get_json()
        mascota = Mascota.query.get_or_404(json["id"])
        db.session.delete(mascota)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Mascota eliminada exitósamente"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex}) #XML Moderno, EDI - Electronic Data Interchange

@appmascota.route('/mascota/obtener')
def obtenerMascotas():
    mascotas = Mascota.query.all()
    listaMascotas = []
    for p in mascotas:
        mascota = {} #Diccionario vacio
        mascota["nombremascota"] = p.nombremascota
        mascota["razamascota"] = p.razamascota
        mascota["colormascota"] = p.colormascota
        mascota["edadmascota"] = p.edadmascota
        listaMascotas.append(mascota)
    return jsonify({'Mascotas':listaMascotas})
