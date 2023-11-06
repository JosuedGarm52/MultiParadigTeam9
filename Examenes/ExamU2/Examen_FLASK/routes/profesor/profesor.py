from flask import Blueprint,jsonify,request
from models import Profesor
from app import db

approfesor = Blueprint("approfesor",__name__)
@approfesor.route('/profesor/agregar',methods=["POST"]) #Cuidado con el nombre de las rutas, no puede haber dos rutas con nombre 'agregar' en el mismo proyecto
def agregarProfesor(): #Método para agregar producto
    try:
        json = request.get_json() #Lo convierte en un diccionario
        profesor = Profesor() #Crear un producto nuevo
        profesor.nombreprofesor = json['nombreprofesor']
        profesor.apellidosprofesor = json['apellidosprofesor']
        profesor.materiaprofesor = json['materiaprofesor']
        profesor.correoprofesor = json['correoprofesor']
        db.session.add(profesor)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Profesor agregado exitósamente"}) #Respuesta valida
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex}) #XML Moderno, EDI - Electronic Data Interchange

@approfesor.route('/profesor/editar',methods=["POST"]) #Cuidado con el nombre de las rutas, no puede haber dos rutas con nombre 'agregar' en el mismo proyecto
def editarProfesor(): #Método para agregar producto
    try:
        json = request.get_json() #Lo convierte en un diccionario
        profesor = Profesor.query.get_or_404(json["id"])
        profesor.nombreprofesor = json['nombreprofesor']
        profesor.apellidosprofesor = json['apellidosprofesor']
        profesor.materiaprofesor = json['materiaprofesor']
        profesor.correoprofesor = json['correoprofesor']
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Profesor modificado exitósamente"}) #Respuesta valida
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex}) #XML Moderno, EDI - Electronic Data Interchange

@approfesor.route('/profesor/eliminar',methods=["POST"]) #Cuidado con el nombre de las rutas, no puede haber dos rutas con nombre 'agregar' en el mismo proyecto
def eliminarProfesor(): #Método para agregar producto
    try:
        json = request.get_json()
        profesor = Profesor.query.get_or_404(json["id"])
        db.session.delete(profesor)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Profesor eliminado exitósamente"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex}) #XML Moderno, EDI - Electronic Data Interchange

@approfesor.route('/profesor/obtener')
def obtenerProfesores():
    profesores = Profesor.query.all()
    listaProfesores = []
    for p in profesores:
        profesor = {} #Diccionario vacio
        profesor["nombreprofesor"] = p.nombreprofesor
        profesor["apellidosprofesor"] = p.apellidosprofesor
        profesor["materiaprofesor"] = p.materiaprofesor
        profesor["correoprofesor"] = p.correoprofesor
        listaProfesores.append(profesor)
    return jsonify({'Profesores':listaProfesores})
