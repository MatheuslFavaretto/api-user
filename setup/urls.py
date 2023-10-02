from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from user_api.views import UserViewSet
from email_model.views import EmailViewSet
from cpf_model.views import CpfViewSet
from endereco_model.views import EnderecoViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'emails', EmailViewSet)
router.register(r'cpf', CpfViewSet)
router.register(r'enderecos', EnderecoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/v1/api/', include(router.urls)),  
]
