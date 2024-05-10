from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('clientes/', views.cliente_list),
    path('clientecreate/', csrf_exempt(views.client_create), name='clientCreate'),
]