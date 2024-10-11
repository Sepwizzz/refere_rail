from rest_framework import viewsets
from .models import Arbitros, Organizador,Evento
from .serializers import ArbitrosSerializer, OrganizadorSerializer,EventoSerializer

class ArbitrosViewSet(viewsets.ModelViewSet):
    queryset = Arbitros.objects.all()
    serializer_class = ArbitrosSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        tipo_arbitro = self.request.query_params.get('tipoArbitro', None)
        disciplina = self.request.query_params.get('disciplina', None)
        ciudad = self.request.query_params.get('ciudad', None)
        localidad = self.request.query_params.get('localidad', None)

        if tipo_arbitro is not None:
            queryset = queryset.filter(tipoArbitro=tipo_arbitro)
        if disciplina is not None:
            queryset = queryset.filter(disciplina=disciplina)
        if ciudad is not None:
            queryset = queryset.filter(ciudad=ciudad)
        if localidad is not None:
            queryset = queryset.filter(localidad=localidad)

        return queryset
        
class OrganizadorViewSet(viewsets.ModelViewSet):
    queryset = Organizador.objects.all()
    serializer_class = OrganizadorSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def get_queryset(self):
        queryset = Evento.objects.all()
        estado = self.request.query_params.get('estado', None)
        arbitros = self.request.query_params.get('arbitros', None)
        organizador = self.request.query_params.get('organizador', None)

        if estado is not None:
            queryset = queryset.filter(estado=estado)
        if arbitros is not None:
            queryset = queryset.filter(arbitros=arbitros)
        if organizador is not None:
            queryset = queryset.filter(organizador=organizador)

        return queryset