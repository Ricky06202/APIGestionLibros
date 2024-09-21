from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import Libro

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autores.objects.all()
    serializer_class = AutorSerializer

class TemaViewSet(viewsets.ModelViewSet):
    queryset = Temas.objects.all()
    serializer_class = TemaSerializer