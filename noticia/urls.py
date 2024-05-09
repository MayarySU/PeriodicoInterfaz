from django.urls import path
from noticia.views import Home, ReporteroView, ReporteroAlta, ReporteroBaja, ReporteroEditar
from django.urls import path
# En tu archivo urls.py

# En tu archivo urls.py
from django.urls import path
from noticia.views import Home, ReporteroView, ReporteroAlta, ReporteroBaja, ReporteroEditar
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('reporteros/', ReporteroView.as_view(), name='reporteros'),
    path('reportero_alta/', ReporteroAlta.as_view(), name='reportero_alta'),
    path('reportero_baja/<int:id>/', ReporteroBaja.as_view(), name='reportero_baja'),
    path('reportero_editar/<int:id>/', ReporteroEditar.as_view(), name='reportero_editar'),
    path('noticias/', views.listar_noticias, name='noticias'),
    path('agregar_noticia/', views.agregar_noticia, name='agregar_noticia'),
    # La URL para editar noticia
    path('editar_noticia/<int:id>/', views.editar_noticia, name='editar_noticia'),
    path('eliminar_noticia/<int:id>/', views.eliminar_noticia, name='eliminar_noticia'),
]
