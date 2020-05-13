from rest_framework import viewsets
from .models import Measure
from .serializers import MeasureSerializer

class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measure.objects.all().order_by('-created')
    serializer_class = MeasureSerializer