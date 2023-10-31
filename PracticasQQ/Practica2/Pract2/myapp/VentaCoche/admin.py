from django.contrib import admin
from VentaCoche.models import VentaCoche

# Register your models here.
@admin.register(VentaCoche)
class VentaCocheAdmin(admin.ModelAdmin):
    list_display = ('coche_vendido', 'vendedor', 'fecha_venta', 'precio_venta')
    list_filter = ('vendedor', 'fecha_venta')
    search_fields = ('coche_vendido__modelo', 'vendedor__nombre')
    list_per_page = 10
    ordering = ('fecha_venta',)