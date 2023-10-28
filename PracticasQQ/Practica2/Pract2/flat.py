# django-admin startproject myapp
# python manage.py startapp pract2 //dentro de la carpeta mi app para el proyecto
# crear carpeta templates
    # cree archivo bienvenido.html
# puse def index en /pract2/views.py
# puse index en el url en myapp/urls.py
    # puse el from que hace referencia a index en el url
# fui a al archivo myapp/settings.py
    # fui ala seccion INSTALLED_APPS
        #coloque pract2
#(JosuePepDJango) C:\Users\jacco\OneDrive\Documentos\Repositorios\MultiParadigTeam9\
#PracticasQQ\Practica2\Pract2\myapp>python manage.py migrate
    # aplique el comando -- python manage.py makemigrations
    # aplique el comando -- python manage.py migrate
# corri el server
    # python manage.py runserver
    ## fui a /admin
    # ejecute el comando python manage.py createsuperuser
    # al crear el super user pide el correo usuario y contraseña admin admin
#cree 6 entidades
    # coche
    # marcacoche
    # conducto
    # ventacoche
    # cliente
    # serviciomantenimiento
# 1. Conductor 2.-> Coche 3.  -> MarcaCoche 
                          #3.1 -> VentaCoche 3.1.2 -> Vendedor
                          #3.2 - > servicioMantenimiento
# comando para las entidades
    # python manage.py startapp Conductor
    # python manage.py startapp Coche
    # python manage.py startapp MarcaCoche
    # python manage.py startapp VentaCoche
    # python manage.py startapp Vendedor
    # python manage.py startapp ServicioMantenimiento
# fui a Conductor/models y cree la clase Conductor models.py
# asi como los demas

# Poner en URLS en INSTALLED_APPS las clases y entidades
    # aplique el comando -- python manage.py makemigrations
    # aplique el comando -- python manage.py migrate

#luego de eso agregue en {carpeta}/forms.py una forma basica
#class CocheForm(forms.ModelForm):
#    class Meta:
#        model = Coche
#        fields = "__all__"

