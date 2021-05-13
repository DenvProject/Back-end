from rest_framework import viewsets
from rest_framework.response import Response

from .json_data_handler import handle_gastos_publicos_json, handle_tuberculose_json

class GastosPublicosViewSet(viewsets.ViewSet):

    def list(self, request):

        gastos_publicos = handle_gastos_publicos_json()
        return Response(gastos_publicos, status=200)


class CasosTuberculoseViewSet(viewsets.ViewSet):

    def list(self, request):
        casos_tuberculose = handle_tuberculose_json()
        return Response(casos_tuberculose, status=200, headers={'Access-Control-Allow-Origin': '*'})