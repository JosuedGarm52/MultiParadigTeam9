from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    #nombre = StringField('Nombre',validators=[DataRequired()])
    pass