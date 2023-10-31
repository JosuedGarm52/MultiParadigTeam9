from django.shortcuts import render,redirect, get_object_or_404
from MarcaCoche.models import MarcaCoche
from MarcaCoche.forms import MarcaCocheForm

# Create your views here.
def nuevoMarcaCoche(request):
    if request.method=='POST':
        formaCoche = MarcaCocheForm(request.POST)
        if formaCoche.is_valid():
            formaCoche.save()
            return redirect("ListadoMarcaCoche")

    else:
        formaCoche=MarcaCocheForm()
    return render(request,"nuevoMarcaCoche.html",{'formaMarcaCoche':formaCoche}) 

def editarMarcaCoche(request,id):
    marcacoche = get_object_or_404(MarcaCoche,pk=id)
    if request.method == "POST":
        formaMarcaCoche = MarcaCocheForm(request.POST,instance=marcacoche)
        if formaMarcaCoche.is_valid():
            formaMarcaCoche.save()
            return redirect('ListadoMarcaCoche')
    else:
        formaMarcaCoche = MarcaCocheForm(instance=marcacoche)
    return render(request,"editarMarcaCoche.html",{"formaMarcaCoche":formaMarcaCoche})

def eliminarMarcaCoche(request,id):
    objeto = get_object_or_404(MarcaCoche,pk=id)
    if objeto:
        objeto.delete()
    return redirect("ListadoMarcaCoche")

def detalleMarcaCoche(request,id):
    coche = get_object_or_404(MarcaCoche,pk=id)
    return render(request,"detalleMarcaCoche.html",{"marcacoche":coche})