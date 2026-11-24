from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detalle_contacto, name='detalle_contacto'),
    path('nuevo/', views.nuevo_contacto, name='nuevo_contacto'),
    path('editar/<int:pk>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:pk>/', views.eliminar_contacto, name='eliminar_contacto'),
]