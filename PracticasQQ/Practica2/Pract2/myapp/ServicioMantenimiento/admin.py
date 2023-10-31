from django.contrib import admin
from ServicioMantenimiento.models import ServicioMantenimiento

# Register your models here.
@admin.register(ServicioMantenimiento)
class ServicioMantenimientoAdmin(admin.ModelAdmin):
    list_display = ('get_tipo_servicio_display', 'fecha_servicio', 'costo_servicio', 'vehiculo')
    list_filter = ('tipo_servicio', 'fecha_servicio', 'costo_servicio')
    search_fields = ('vehiculo__modelo', 'vehiculo__numeroplaca')
    list_per_page = 10
    ordering = ('fecha_servicio',)