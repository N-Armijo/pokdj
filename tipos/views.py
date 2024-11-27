from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Tipo
from .forms import TipoForm

# Create your views here.
@login_required
def listar_tipo(request):
    tipos = Tipo.objects.all()
    return render(request, 'listar_tipo.html', {'tipos': tipos})

@login_required
def crear_tipo(request):
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tipo')
    else:
        form = TipoForm()
    return render(request, 'crear_tipo.html', {'form': form})

@login_required
def editar_tipo(request, tipo_id):
    tipo = get_object_or_404(Tipo, id=tipo_id)
    if request.method == 'POST':
        form = TipoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('listar_tipo')
    else:
        form = TipoForm(instance=tipo)
    return render(request, 'editar_tipo.html', {'form': form})

@login_required
def eliminar_tipo(request, tipo_id):
    tipo = get_object_or_404(Tipo, id=tipo_id)
    if request.method == 'POST':
        tipo.delete()
        return redirect('listar_tipo')
    return render(request, 'eliminar_tipo.html', {'tipo': tipo})