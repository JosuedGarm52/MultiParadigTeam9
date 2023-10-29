from django.shortcuts import render
from Conductor.models import Conductor

# Create your views here.
def index(request):
    return render(request,'bienvenido.html') 

def indexConductor(request):
    noConductores = Conductor.objects.count()
    conductores = Conductor.objects.order_by('id')
    return render(request, 'indexConductor.html', {"conductores": conductores, "count": noConductores})