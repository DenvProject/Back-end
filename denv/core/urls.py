from django.urls import path, include


from rest_framework import routers
from .viewsets import *


app_name = 'core'

router = routers.SimpleRouter()
router.register(r'gastos_publicos', GastosPublicosViewSet, basename='gastos_publicos')

urlpatterns = [
    path('', include((router.urls, 'core'), namespace='data'))
]