from django.shortcuts import render
from Conductor.models import Conductor
from Coche.models import Coche
from MarcaCoche.models import MarcaCoche
from ServicioMantenimiento.models import ServicioMantenimiento
from Vendedor.models import Vendedor
from VentaCoche.models import VentaCoche

# Create your views here.
def index(request):
    return render(request,'bienvenido.html') 

def indexConductor(request):
    noConductores = Conductor.objects.count()
    conductores = Conductor.objects.order_by('id')
    return render(request, 'indexConductor.html', {"conductores": conductores, "count": noConductores})

def indexCoche(request):
    coches = Coche.objects.all()
    return render(request, 'indexCoche.html', {'coches': coches})

def indexMarcaCoche(request):
    marcacoches = MarcaCoche.objects.all()
    return render(request, 'indexMarcaCoche.html', {'marcacoches': marcacoches})

def indexServicioMantenimiento(request):
    serviciomantenimientos = ServicioMantenimiento.objects.all()
    return render(request, 'indexServicioMantenimiento.html', {'serviciomantenimientos': serviciomantenimientos})

def indexVendedor(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'indexVendedor.html', {'vendedores': vendedores})

def indexVentaCoche(request):
    ventacoches = VentaCoche.objects.all()
    return render(request, 'indexVentaCoche.html', {'ventacoches': ventacoches})