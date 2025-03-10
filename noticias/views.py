from django.shortcuts import render
from .models import Noticia
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404

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
