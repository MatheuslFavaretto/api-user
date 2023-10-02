from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

#from user_api.views.cpf import CpfViewSet
#from user_api.views.email import EmailViewSet
#from user_api.views.endereco import EnderecoViewSet
from user_api.views.user import UserViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet)
#router.register(r'emails', EmailViewSet)
#router.register(r'cpf', CpfViewSet)
#router.register(r'enderecos', EnderecoViewSet)

urlpatterns = [
#    path('admin/', admin.site.urls),
    path('v1/api/', include(router.urls)),  
]
