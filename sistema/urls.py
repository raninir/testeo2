from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

from . import views
#Url para ir a las direcciones
urlpatterns = [
    url(r'^$',views.index),
    url(r'^index/$',views.index,name="inicio"),
    url(r'^MascotaLista',views.lista,name="lista"),
    url(r'^Usuarios/$',views.registrarse,name="registrarse"),
    url(r'^formulario/$',views.formulario,name="formulario"),
    url(r'^login/$',views.ingresar,name="login"),
    url(r'^salir/$',views.salir,name="logout"),
    url(r'^admin/$',views.admin,name="admin"),
    url(r'^password/$', views.change_password, name='change_password'),
#URLS para recuperar contraseña
   url(r'^password_reset', PasswordResetView.as_view(), 
        {'template_name':'password_reset_form.html',
        'email_template_name': 'password_reset_email.html'}, 
        name='password_reset'), 
    url(r'^password_reset_done', PasswordResetDoneView.as_view(), 
        {'template_name': 'password_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), 
        {'template_name': 'password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', PasswordResetCompleteView.as_view(), {'template_name': 'password_reset_complete.html'},
        name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
