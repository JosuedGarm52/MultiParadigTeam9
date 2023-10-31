from django.forms import ModelForm
from Vendedor.models import Vendedor

class VendedorForm(ModelForm):
    class Meta:
        model = Vendedor
        fields = "__all__"