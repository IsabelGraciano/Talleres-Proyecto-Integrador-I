from rest_framework import serializers
from .models import Measure, cultivo

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ('id', 'type', 'value')
        #fields = ('id', 'codigo', 'latitud', 'longitud', 'area', 'producto')

class cultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = cultivo
        #fields = ('id', 'type', 'value')
        fields = ('codigo', 'latitud', 'longitud', 'area', 'producto')