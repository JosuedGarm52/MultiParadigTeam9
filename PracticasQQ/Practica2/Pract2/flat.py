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

#Habia olvidado configurar la bd xd
    # ve a settings.py 
    # cambia database
    # Host y port

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

# agruegue el templeates de conductor y tambien puse en url con el path
# templeates puse el indexConductor y layout html

#quise agregar a admin.py para que salieran en cada carpeta corresponidente
# segun no es necesario ponerlo todo en pract2

# movi layout a pract2/templates
# modifique myapp/settings.py el templates[ dir: [] ] y agregue from os
# agregue los demas a en el html pract2/templates/bienvenido.html

# copie y modifique los templates en las demas carpetas

# me esta dando problemas las referencas a los templates del carro
# el error era esto
    #<td><a href="editarCoche">Editar</a></td>
    #<td><a href="editarCoche/{{coche.id}}">Editar</a></td> faltaba el coche id
#y
    #<a href="nuevoCoche.html">Agregar</a>
    #<a href="nuevoCoche">Agregar</a>

#Por ultimo, solo deje 3 views y llene 3 datos a cada tabla