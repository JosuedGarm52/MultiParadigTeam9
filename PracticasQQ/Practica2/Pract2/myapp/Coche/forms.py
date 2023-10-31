from django.forms import ModelForm
from Coche.models import Coche

class CocheForm(ModelForm):
    class Meta:
        model = Coche
        fields = "__all__"