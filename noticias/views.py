from django.shortcuts import render, redirect
from .models import Noticia
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import os

@login_required
def admin_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')  # Ordenar por fecha más reciente
    return render(request, 'noticias/admin_noticias.html', {'noticias': noticias})

def home(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')  # Cargar noticias más recientes
    return render(request, 'noticias/lista_noticias.html', {'noticias': noticias})

def lista_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'noticias/lista_noticias.html', {'noticias': noticias})

class CustomLoginView(LoginView):
    template_name = 'noticias/login.html'  # Usa la plantilla personalizada
    redirect_authenticated_user = True  # Si ya está autenticado, lo redirige

    def get_success_url(self):
        return '/admin/'  # Redirige al panel de administración de Django
    
def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'noticias/detalle_noticia.html', {'noticia': noticia})

def registrarDatos(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        contenido = request.POST['contenido']
        imagen = request.FILES.get('imagen')  # Correctamente obtiene el archivo subido

        # Crea una instancia del modelo
        nueva_noticia = Noticia(
            titulo=titulo,
            contenido=contenido,
            imagen=imagen
        )

        # Guarda en la base de datos
        nueva_noticia.save()

        return redirect('admin_noticias')

    # Si alguien intenta acceder mediante GET, redirigir también:
    return redirect('admin_noticias')

def editarDatos(request, noticia_id):
    # Busca la noticia específica por su ID
    noticia = Noticia.objects.get(id=noticia_id)

    if request.method == 'POST':
        # Captura los datos enviados por POST
        titulo = request.POST['titulo']
        contenido = request.POST['contenido']
        imagen = request.FILES.get('imagen', None)

        # Actualiza los campos del objeto existente
        noticia.titulo = titulo
        noticia.contenido = contenido

        # Si suben una nueva imagen, actualizarla. Sino, conserva la antigua.
        if imagen:
            noticia.imagen = imagen

        # Guarda los cambios
        noticia.save()

        # Redirige tras guardar
        return redirect('admin_noticias')

    # Si la solicitud es GET, carga la plantilla con la noticia existente
    return render(request, 'noticias/editar_noticia.html', {'noticia': noticia})

def eliminarDatos(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)

    # Si la noticia tiene imagen, se elimina el archivo físicamente
    if noticia.imagen:
        if os.path.isfile(noticia.imagen.path):
            os.remove(noticia.imagen.path)

    # Ahora sí se elimina la noticia de la base de datos
    noticia.delete()

    return redirect('admin_noticias')

def salir(request):
    logout(request)  # Esto cierra la sesión actual
    return redirect('lista_noticias')  # Redirige a la página de noticias
