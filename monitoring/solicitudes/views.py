from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import SolicitudForm
from .logic.solicitudesLogic import create_solicitud, get_solicitudes
from django.contrib.auth.decorators import login_required
# Descomentar cuando se cree el archivo monitoring/auth0backend.py
from monitoring.auth0backend import getRole

@login_required
def solicitud_list(request):
    role,email= getRole(request)
    solicitudes = get_solicitudes()
    solicitudes_aux=[]
    for solicitud in solicitudes:
        solicitudes_aux.append(solicitud)  
    solicitudes= solicitudes_aux

    context={'solicitudesList':solicitudes}    
    return render(request, 'solicitudes/solicitudes.html',context)
    

@login_required
def solicitud_update(request,solicitud_id):
   solicitud= get_solicitud(solicitud_id)
   role,email= getRole(request)
    
   if role == "admin":
    if request.method == 'POST':
        form= SolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            create_solicitud(form,email) 
            return HttpResponseRedirect(reverse("solicitudesList"))
        else:
            print(form.errors) 
    else: 

        form= SolicitudForm(instance=solicitud)
    context={
            'form': form,
    }    
    return render(request,'solicitudes/update_solicitud.html',context)
   else:
     return HttpResponse("Unauthorized User")   


def solicitud_create(request):
    role, email = getRole(request)
    
    if role in ["admin", "user"]:  # Se corrigió la condición para verificar si el rol es admin o user
        if request.method == 'POST':
            form = SolicitudForm(request.POST)
            if form.is_valid():
                create_solicitud(form, email)
                messages.success(request, 'Solicitud created successfully')  # Se corrigió el mensaje de éxito
                return HttpResponseRedirect(reverse('solicitudesCreate'))
            else:
                print(form.errors)
        else:
            form = SolicitudForm()

        context = {
            'form': form,
        }
        return render(request, 'solicitudes/create_solicitud.html', context)
    else:
        return HttpResponse("Unauthorized User")
