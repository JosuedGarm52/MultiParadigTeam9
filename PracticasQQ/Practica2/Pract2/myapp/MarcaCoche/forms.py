from django.forms import ModelForm
from MarcaCoche.models import MarcaCoche

class CocheForm(ModelForm):
    class Meta:
        model = MarcaCoche
        fields = "__all__"