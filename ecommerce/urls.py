from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from produtos.views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base, name="base"),
    path('index/', index, name="index"),
    path('listagem/', listagem, name="listagem"),
    path('detalhes/<int:id>', detalhes, name="detalhes"),
    path('quemsomos/', quem_somos, name="quemsomos"),
    path('forms/', cadastro_usuario, name="cadastro_usuario"),
    path('login/', login, name="login"),
    path ( 'accounts/login/',LoginView.as_view(template_name = 'login.html' ), name = 'login' ),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)