from django.contrib import admin
from Coche.models import Coche

# Register your models here.
@admin.register(Coche)
class CocheAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'year_fabricacion', 'numeroplaca', 'color', 'precio', 'conductor')
    list_filter = ('marca', 'year_fabricacion', 'color')
    search_fields = ('modelo', 'numeroplaca', 'conductor__nombre')
    list_per_page = 10
    ordering = ('marca', 'modelo')