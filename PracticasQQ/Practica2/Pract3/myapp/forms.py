from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField, FloatField, DateField
from wtforms.validators import DataRequired

class ClienteForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    apellido = StringField('Apellido')
    direccion = StringField('Direccion',validators=[DataRequired()])
    edad = IntegerField('Edad',validators=[DataRequired()])
    enviar = SubmitField("Enviar")

class VendedorForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido')
    num_iden_ven = StringField('Número de Identificación')
    fecha_inicio = DateField('Fecha de Inicio') 
    num_telefono = StringField('Número de Teléfono')
    enviar = SubmitField("Enviar")

class VentaForm(FlaskForm):
    nombre_producto = StringField('Nombre del Producto', validators=[DataRequired()])
    valor = FloatField('Valor', validators=[DataRequired()])
    categoria = StringField('Categoría')
    fecha = DateField('Fecha') 
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    enviar = SubmitField("Enviar")

class AgenciaForm(FlaskForm):
    nombre = StringField('Nombre del Producto', validators=[DataRequired()])
    num_telef = IntegerField('Numero del telefono', validators=[DataRequired()])
    enviar = SubmitField("Enviar")
