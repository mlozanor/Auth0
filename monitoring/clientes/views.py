from django.shortcuts import render
from .forms import ClienteForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.clientesLogic import create_cliente, get_clientes
from django.contrib.auth.decorators import login_required

@login_required
def cliente_list(request):
    clientes = get_clientes()
    context = {
        'clientes_list': clientes
    }
    return render(request, 'cliente/clientes.html', context)

def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            create_cliente(form)
            messages.success(request, 'Cliente creado correctamente')
            return HttpResponseRedirect(reverse('client_create'))
    else:
        form = ClienteForm()

    context = {
            'form': form
    }
    
    return render(request, 'cliente/clienteCreate.html', context)