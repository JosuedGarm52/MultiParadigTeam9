from django.contrib import admin
from MarcaCoche.models import MarcaCoche
# Register your models here.
@admin.register(MarcaCoche)
class MarcaCocheAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'paisorigen', 'year_fundacion')
    list_filter = ('paisorigen', 'year_fundacion')
    search_fields = ('nombre', 'paisorigen')
    list_per_page = 10
    ordering = ('nombre',)