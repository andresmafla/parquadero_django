from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('carros', views.carros, name='carros'),
    path('carros/crear', views.crear, name='crear'),
    path('borrar/<int:id>', views.borrar, name='borrar'),
    path('carros/formulario', views.formulario, name='formulario'),
    path('cobro/<int:id>', views.cobro, name='cobro'),
]