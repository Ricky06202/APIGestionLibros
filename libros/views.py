from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LibroSerializer
from .models import Libro

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer