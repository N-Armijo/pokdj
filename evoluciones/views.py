from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Evolucion
from .forms import EvolucionForm

# Create your views here.

# @login_required
# def listar_evolucion(request):
#     evoluciones = Evolucion.objects.select_related('pokemon').all()
#     return render(request, 'listar_evolucion.html', {'evoluciones': evoluciones})
@login_required
def listar_evolucion(request):
    evoluciones = Evolucion.objects.all()  # Puedes simplificar esto si no necesitas `select_related`
    return render(request, 'listar_evolucion.html', {'evoluciones': evoluciones})



# @login_required
# def crear_evolucion(request):
#     if request.method == 'POST':
#         form = EvolucionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_evolucion')
#     else:
#         form = EvolucionForm()
#     return render(request, 'crear_evolucion.html', {'form': form})
@login_required
def crear_evolucion(request):
    if request.method == 'POST':
        form = EvolucionForm(request.POST)
        if form.is_valid():
            form.save()
            print("Evolución guardada con éxito")  # Verifica que se guarde correctamente
            return redirect('listar_evolucion')
        else:
            print("Formulario no válido:", form.errors)  # Muestra errores si los hay
    else:
        form = EvolucionForm()
    return render(request, 'crear_evolucion.html', {'form': form})


@login_required
def eliminar_evolucion(request, evolucion_id):
    evolucion = get_object_or_404(Evolucion, id=evolucion_id)
    if request.method == 'POST':
        evolucion.delete()
        return redirect('listar_evolucion')
    return render(request, 'eliminar_evolucion.html', {'evolucion': evolucion})

@login_required
def editar_evolucion(request, evolucion_id):
    evolucion = get_object_or_404(Evolucion, id=evolucion_id)
    if request.method == 'POST':
        form = EvolucionForm(request.POST, instance=evolucion)
        if form.is_valid():
            form.save()
            return redirect('listar_evolucion')
    else:
        form = EvolucionForm(instance=evolucion)
    return render(request, 'editar_evolucion.html', {'form': form})
