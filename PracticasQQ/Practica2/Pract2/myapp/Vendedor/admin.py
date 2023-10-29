from django.contrib import admin
from Vendedor.models import Vendedor

# Register your models here.
@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'direccion')
    list_filter = ('telefono',)
    search_fields = ('nombre', 'correo', 'direccion')
    list_per_page = 10
    ordering = ('nombre',)