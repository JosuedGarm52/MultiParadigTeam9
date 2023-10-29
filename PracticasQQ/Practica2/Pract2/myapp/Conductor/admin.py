from django.contrib import admin
from Conductor.models import Conductor

# Register your models here.
@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'clave_licencia', 'edad', 'direccion')
    list_filter = ('edad',)
    search_fields = ('nombre', 'clave_licencia', 'direccion')
    list_per_page = 10
    ordering = ('nombre',)
