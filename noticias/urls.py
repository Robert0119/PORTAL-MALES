from django.urls import path
from .views import lista_noticias
from .views import CustomLoginView
from .views import CustomLoginView, home
from .views import home, lista_noticias, CustomLoginView, detalle_noticia
from .views import home, lista_noticias, CustomLoginView, detalle_noticia, admin_noticias
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

class CustomLoginView(LoginView):
    template_name = 'noticias/login.html'
    redirect_authenticated_user = True  # si el usuario ya está logueado, lo redirige

    def get_success_url(self):
        # Retorna la URL (o name) de la ruta que definimos en urls.py
        return reverse_lazy('admin_noticias')
urlpatterns = [
    path('', home, name='home'),  # Página principal
    path('noticias/', lista_noticias, name='lista_noticias'),  # Vista de noticias
    path('noticia/<int:noticia_id>/', detalle_noticia, name='detalle_noticia'),
    path('login/', CustomLoginView.as_view(), name='login'),  # Página de login
    # Ruta del panel de administración personalizado
    path('admin_noticias/', admin_noticias, name='admin_noticias'),
    path('registrarDatos/', views.registrarDatos, name='registrarDatos'),
    path('eliminarDatos/<int:noticia_id>/', views.eliminarDatos, name='eliminarDatos'),
    path('editarDatos/<int:noticia_id>/', views.editarDatos, name='editarDatos'),
    path('salir/', views.salir, name='salir'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Para servir archivos multimedia