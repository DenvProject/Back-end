from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .json_data_handler import handle_gastos_publicos_json

class GastosPublicosViewSet(viewsets.ViewSet):

    def list(self, request):

        gastos_publicos = handle_gastos_publicos_json()
        return Response(gastos_publicos, status=200)