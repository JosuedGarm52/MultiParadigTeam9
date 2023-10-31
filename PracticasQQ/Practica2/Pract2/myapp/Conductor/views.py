from django.shortcuts import render,redirect, get_object_or_404
from Conductor.models import Conductor
from Conductor.forms import ConductorForm

# Create your views here.
def nuevoConductor(request):
    if request.method=='POST':
        formaConductor = ConductorForm(request.POST)
        if formaConductor.is_valid():
            formaConductor.save()
            return redirect("ListadoConductor")

    else:
        formaConductor=ConductorForm()
    return render(request,"nuevoConductor.html",{'formaConductor':formaConductor})

def editarConductor(request,id):
    conductor = get_object_or_404(Conductor,pk=id)
    if request.method == "POST":
        formaConductor = ConductorForm(request.POST,instance=conductor)
        if formaConductor.is_valid():
            formaConductor.save()
            return redirect('ListadoConductor')
    else:
        formaConductor = ConductorForm(instance=conductor)
    return render(request,"editarConductor.html",{"formaConductor":formaConductor})

def eliminarConductor(request,id):
    objeto = get_object_or_404(Conductor,pk=id)
    if objeto:
        objeto.delete()
    return redirect("ListadoConductor")

def detalleConductor(request,id):
    conductor = get_object_or_404(Conductor,pk=id)
    return render(request,"detalleConductor.html",{"conductor":conductor})