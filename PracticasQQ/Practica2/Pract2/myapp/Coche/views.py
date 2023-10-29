from django.shortcuts import render,redirect, get_object_or_404
from Coche.models import Coche
from Coche.forms import CocheForm

# Create your views here.
def nuevoCoche(request):
    if request.method=='POST':
        formaCoche = CocheForm(request.POST)
        if formaCoche.is_valid():
            formaCoche.save()
            return redirect("ListadoCoche")

    else:
        formaCoche=CocheForm()
    return render(request,"nuevoCoche.html",{'formaCoche':formaCoche}) 

def editarCoche(request,id):
    coche = get_object_or_404(Coche,pk=id)
    if request.method == "POST":
        formaCoche = CocheForm(request.POST,instance=coche)
        if formaCoche.is_valid():
            formaCoche.save()
            return redirect('ListadoCoche')
    else:
        formaCoche = CocheForm(instance=coche)
    return render(request,"editarCoche.html",{"formaCoche":formaCoche})

def eliminarCoche(request,id):
    objeto = get_object_or_404(Coche,pk=id)
    if objeto:
        objeto.delete()
    return redirect("ListadoCoche")

def detalleCoche(request,id):
    coche = get_object_or_404(Coche,pk=id)
    return render(request,"detalleCoche.html",{"coche":coche})