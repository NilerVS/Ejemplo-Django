from django.urls import path
from . import views


app_name = "usuario_app"

urlpatterns = [

    path('', views.PruebaView.as_view(), name= 'inicio'),
    path('listar-usuarios/', views.PruebaListView.as_view(), name= 'listarusuario'),
    path('crear-usuarios/', views.PruebaCreateView.as_view(), name= 'crearusuario'),
    path('actulizar-usuarios/<pk>', views.PruebaUpdateView.as_view(), name= 'actulizarusuario'),
    path('eliminar-usuarios/<pk>', views.PruebaDeleteView.as_view(), name= 'eliminarusuario'),

]
