from django.urls import path
from .views import lista_noticias
from .views import CustomLoginView
from .views import CustomLoginView, home
from .views import home, lista_noticias, CustomLoginView, detalle_noticia

urlpatterns = [
    path('', home, name='home'),  # Página principal
    path('noticias/', lista_noticias, name='lista_noticias'),  # Vista de noticias
    path('noticia/<int:noticia_id>/', detalle_noticia, name='detalle_noticia'),
    path('login/', CustomLoginView.as_view(), name='login'),  # Página de login
    
]