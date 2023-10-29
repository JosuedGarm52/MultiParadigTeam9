from django.forms import ModelForm
from MarcaCoche.models import MarcaCoche

class MarcaCocheForm(ModelForm):
    class Meta:
        model = MarcaCoche
        fields = "__all__"