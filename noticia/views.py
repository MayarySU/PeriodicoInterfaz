
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View

from noticia.forms import ReporteroForm
from noticia.models import Reportero
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import Noticia, Reportero
from .forms import NoticiaForm, ReporteroForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic import View
from .models import Noticia




class NoticiaView(ListView):
    model = Noticia
    template_name = 'noticia/listar_noticias.html'  # Plantilla para mostrar la lista de noticias
    context_object_name = 'noticias'  # Nombre del objeto de contexto que contiene las noticias


def listar_noticias(request):
    noticias = Noticia.objects.all()  # Obtener todas las noticias de la base de datos
    return render(request, 'noticia/listar_noticias.html', {'noticias': noticias})
def agregar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la página de lista de noticias después de agregar una noticia
            return redirect('noticias')
    else:
        form = NoticiaForm()
    return render(request, 'noticia/agregar_noticia.html', {'form': form})
# views.py



def editar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)

    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()

    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'noticia/editar_noticia.html', {'form': form, 'noticia': noticia})


def eliminar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    if request.method == 'POST':
        noticia.delete()
        return redirect('noticias')  # Redireccionar a la página de noticias después de eliminar
    return render(request, 'noticia/eliminar.html', {'noticia': noticia})


class Home(View):
    def get(self, request):
        noticias = Noticia.objects.all()  # Obtener todas las noticias
        context = {
            'titulo': 'Inicio',
            'encabezado': "Periodico el mitotero",
            'hay_agregar': False,
            'noticias': noticias  # Pasar las noticias al contexto
        }
        return render(request, 'home/index.html', context)
class ReporteroView(View):
    def get(self, request):
        context = {
            'titulo': 'Reporteros',
            'reporteros': Reportero.objects.all(),
            'encabezado': "Reporteros",
            'hay_agregar': True,
            'link_agregar': "/reportero_alta",
            'filtro': "nombre"
        }
        return render(request, 'reportero/listar.html', context)

    def post(self, request):
        if 'filtro_checkbox' not in request.POST:
            nombre = request.POST['filtro']
            reporteros = Reportero.objects.filter(nombre__icontains=nombre).all()
        else:
            reporteros = Reportero.objects.all()
        context = {
            'titulo': 'Reporteros',
            'reporteros': reporteros,
            'encabezado': "Reporteros",
            'hay_agregar': True,
            'link_agregar': "/reportero_alta",
            'filtro': "nombre"
        }
        return render(request, 'reportero/listar.html', context)

class ReporteroAlta(View):
    def get(self, request):
        form = ReporteroForm()
        context = {
            'titulo': 'Alta Reporteros',
            'form': form,
            'btn_submit_texto': "Guardar",
            'encabezado': "Alta Reporteros",
            'color_fondo': 'w3-green'
        }
        return render(request, 'reportero/abc.html', context)

    def post(self, request):
        form = ReporteroForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            form.save()
            user = Reportero.objects.filter(username=username).first()
            user.set_password(password)
            user.save()
            return redirect('reporteros')
        context = {
            'titulo': 'Error en Alta Reporteros',
            'form': form,
            'encabezado': "Alta Reporteros",
            'btn_submit_texto': "Guardar",
            'color_fondo': 'w3-green'
        }
        return render(request, 'reportero/abc.html', context)

class ReporteroBaja(View):
    def get(self, request, id):
        reportero = Reportero.objects.filter(id=id).first()
        form = ReporteroForm(instance=reportero)
        context = {
            'titulo': 'Eliminar Reportero',
            'form': form,
            'btn_submit_texto': "Eliminar",
            'encabezado': "Baja Reporteros",
            'color_fondo': 'w3-red'
        }
        return render(request, 'reportero/abc.html', context)

    def post(self, request, id):
        Reportero.objects.filter(id=id).delete()
        return redirect("reporteros")

class ReporteroEditar(View):
    def get(self, request, id):
        reportero = Reportero.objects.filter(id=id).first()
        form = ReporteroForm(instance=reportero)
        context = {
            'titulo': 'Editar Reportero',
            'form': form,
            'btn_submit_texto': "Guardar Cambios",
            'encabezado': "Editar Reporteros",
            'color_fondo': 'w3-yellow'
        }
        return render(request, 'reportero/abc.html', context)

    def post(self, request, id):
        reportero = Reportero.objects.filter(id=id).first()
        form = ReporteroForm(request.POST, request.FILES, instance=reportero)
        if form.is_valid():
            form.save()
            reportero.set_password(form.cleaned_data["password"])
            reportero.save()
            return redirect('reporteros')
        context = {
            'titulo': 'Error en Editar Reportero',
            'form': form,
            'btn_submit_texto': "Guardar Cambios",
            'encabezado': "Editar Reporteros",
            'color_fondo': 'w3-yellow'
        }
        return render(request, 'reportero/abc.html', context)
