from django.forms import ModelForm
from Conductor.models import Conductor

class ConductorForm(ModelForm):
    class Meta:
        model = Conductor
        fields = "__all__"