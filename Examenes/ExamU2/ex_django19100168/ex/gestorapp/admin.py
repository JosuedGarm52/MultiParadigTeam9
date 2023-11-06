from django.contrib import admin

# Register your models here.
from gestorapp.models import Estacion,Bombero,Equipo,Camion,PerroBombero

admin.site.register(Equipo)
admin.site.register(Estacion)
# admin.site.register(Equipo,Estacion,Bombero,Camion,PerroBombero)
admin.site.register(Bombero)
admin.site.register(Camion)
admin.site.register(PerroBombero)


