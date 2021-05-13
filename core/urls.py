from os.path import basename
from django.urls import path, include


from rest_framework import routers
from .viewsets import *


app_name = 'core'

router = routers.DefaultRouter()
router.register(r'gastos_publicos', GastosPublicosViewSet, basename='gastos_publicos')
router.register(r'casos_tuberculose', CasosTuberculoseViewSet ,basename='casos_tuberculose')

urlpatterns = [
    path('', include((router.urls, 'core'), namespace='data'))
]