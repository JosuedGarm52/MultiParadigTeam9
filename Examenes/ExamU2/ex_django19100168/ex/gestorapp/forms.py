from django.forms import ModelForm
from gestorapp.models import *

class BomberoForm(ModelForm):
    class Meta:
        model = Bombero
        fields = "__all__"
class EstacionForm(ModelForm):
    class Meta:
        model = Estacion
        fields = "__all__"
class CamionForm(ModelForm):
    class Meta:
        model = Camion
        fields = "__all__"
class PerroForm(ModelForm):
    class Meta:
        model = PerroBombero
        fields = "__all__"
        
class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = "__all__"