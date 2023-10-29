from django.forms import ModelForm
from ServicioMantenimiento.models import ServicioMantenimiento

class ServicioMantenimientoForm(ModelForm):
    class Meta:
        model = ServicioMantenimiento
        fields = "__all__"