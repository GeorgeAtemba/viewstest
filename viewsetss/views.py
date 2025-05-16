from django.shortcuts import render

from .models import MixMod
from rest_framework import viewsets
from .serializer import SerViewset

# Create your views here.
class Aclass(viewsets.ModelViewSet):
    queryset = MixMod.objects.all()
    serializer_class = SerViewset
