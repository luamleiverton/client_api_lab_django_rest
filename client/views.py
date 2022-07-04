from rest_framework import viewsets
from client.serializers import ClientSerializer
from client.models import Client

class ClientViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

