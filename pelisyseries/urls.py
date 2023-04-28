from django.urls import path, reverse_lazy
from django.contrib.auth.views import *
from . import views
from .forms import UserPasswordResetForm, UserSetPasswordForm, CambiarPasswordForm

app_name = 'pelisyseries'
urlpatterns = [ 
    path('', views.home, name='home' ),
    path('index', views.index, name='index' ),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login' ),
    path('logout/', views.logout_request, name='logout' ),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('series/', views.series, name='series'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/accion/', views.accion, name='accion'),
    path('categorias/animacion/', views.animacion, name='animacion'),
    path('categorias/aventura/', views.aventura, name='aventura'),
    path('categorias/terror/', views.terror, name='terror'),
    path('categorias/ciencia_ficcion/', views.ciencia_ficcion, name='ciencia_ficcion'),
    path('categorias/comedia/', views.comedia, name='comedia'),
    path('categorias/drama/', views.drama, name='drama'),
    path('categorias/familiar/', views.familiar, name='familiar'),
    path('categorias/fantasia/', views.fantasia, name='fantasia'),
    path('categorias/misterio/', views.misterio, name='misterio'),
    path('categorias/musicales/', views.musicales, name='musicales'),
    path('recientes/', views.recientes, name='recientes'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar-perfil/', views.EditarPerfil.as_view(), name='editar-perfil'), 
    path('reproducir/<int:id>', views.Reproduccion, name='reproducir'), 
    path('me_gusta/<int:id>', views.Me_gusta, name='me_gusta'),  
    path('favoritos/<int:id>', views.Favoritos, name='favoritos'),  
    path('favoritos/', views.Favoritos_lista, name='favoritos_lista'),  
    path('busqueda/', views.Busqueda, name='busqueda'),  

    path('change_password/', PasswordChangeView.as_view(template_name='registration/change_password.html', form_class=CambiarPasswordForm, success_url = '/'), name='change_password'),

    path('password_reset/', PasswordResetView.as_view(form_class=UserPasswordResetForm, success_url = reverse_lazy('pelisyseries:password_reset_done')), name='password_reset'),  
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),  
    path('password_reset_confirm/<slug:uidb64>/<slug:token>/', PasswordResetConfirmView.as_view(form_class=UserSetPasswordForm, success_url = reverse_lazy('pelisyseries:password_reset_complete')), name='password_reset_confirm'),  
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),  
]