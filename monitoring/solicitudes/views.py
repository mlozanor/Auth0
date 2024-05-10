from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import SolicitudForm
from .logic.solicitudesLogic import create_solicitud, get_solicitudes
from django.contrib.auth.decorators import login_required
# Descomentar cuando se cree el archivo monitoring/auth0backend.py
#from monitoring.auth0backend import getRole

@login_required
def solicitud_list(request):
    role = getRole(request)
    if role == 'admin':
       solicitudes = get_solicitudes()
       context = {
           'solicitudes_list': solicitudes
       }
       return render(request, 'solicitudes/solicitudes.html', context)
    else:
        return HttpResponse('No tienes permisos para ver esta página')
    

@login_required
def single_solicitud(request, id=0):
    solicitud = get_solicitudes(id)
    context = {
        'solicitud': solicitud
    }
    return render(request, 'solicitudes/solicitud.html', context)


@login_required
def solicitud_create(request):
    role = getRole(request)
    if role == 'admin':
        if request.method == 'POST':
            form = SolicitudForm(request.POST)
            if form.is_valid():
                create_solicitud(form)
                messages.add_message(request, 'Solicitud creada correctamente')
                return HttpResponseRedirect(reverse('solicitudCreate'))
            else:
                messages.error(request, 'Error al crear la solicitud')
        else:
            form = SolicitudForm()
        context = {
            'form': form
        }
        return render(request, 'solicitudes/solicitud_create.html', context)
    else:
        return HttpResponse('No tienes permisos para ver esta página')
   