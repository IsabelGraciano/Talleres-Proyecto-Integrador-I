from rest_framework import viewsets
from .models import Measure, cultivo
from .serializers import MeasureSerializer, cultivoSerializer

class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measure.objects.all().order_by('-created')
    serializer_class = MeasureSerializer


class cultivoViewSet(viewsets.ModelViewSet):
    queryset = cultivo.objects.all().order_by('-created')
    serializer_class = cultivoSerializer