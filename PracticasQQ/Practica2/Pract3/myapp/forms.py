from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired

class ClienteForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    apellido = StringField('Apellido')
    direccion = StringField('Direccion',validators=[DataRequired()])
    edad = IntegerField('Edad',validators=[DataRequired()])
    enviar = SubmitField("Enviar")