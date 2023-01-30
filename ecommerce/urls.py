from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from produtos.views import *
from django.contrib.auth.views import LoginView
from produtos.views import logout_aplicacao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('listagem/', listagem, name="listagem"),
    path('detalhes/<int:id>', detalhes, name="detalhes"),
    path('quemsomos/', quem_somos, name="quemsomos"),
    path('forms/', cadastro_usuario, name="cadastro_usuario"),
    path('sacola/<int:id>', sacola, name="sacola"),
    path('accounts/login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', logout_aplicacao, name="logout")

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)