from django.forms import ModelForm
from VentaCoche.models import VentaCoche

class VentaCocheForm(ModelForm):
    class Meta:
        model = VentaCoche
        fields = "__all__"