from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
	path('web/modulos/', views.modulo_list, name='modulo_list'),
	path('web/contacto/', views.contacto, name='contacto'),
	path('web/acerca/', views.acerca, name='acerca'),
]
