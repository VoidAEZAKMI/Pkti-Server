from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

from .models import Sensor
from .serializers import SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #     if not pk:
    #         return Sensor.objects.all().order_by('-id')[:1]
    #
    #     return Sensor.objects.filter(pk=pk)
    #
    # @action(methods=['get'], detail=True)
    # def category(self, request, pk=None):
    #     cats = Sensor.objects.get(pk=pk)
    #     return Response({'sens': cats.name})
