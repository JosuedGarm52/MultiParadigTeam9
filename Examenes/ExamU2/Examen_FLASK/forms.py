from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired

class JugueteForm(FlaskForm): #Clase para el formulario
    nombrejuguete = StringField('Nombre del Juguete',validators=[DataRequired()]) #Declararemos 4 atributos, los campos del formulario
    nombreproveedor = StringField('Proveedor',validators=[DataRequired()])
    precioventa = IntegerField("Precio de Venta",validators=[DataRequired()])
    cantprodvendidos = IntegerField("Cantidad de Unidades Vendidas",validators=[DataRequired()])
    enviar = SubmitField("Enviar")
    