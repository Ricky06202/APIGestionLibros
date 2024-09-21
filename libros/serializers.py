from rest_framework import serializers
from .models import *

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('__all__')

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = ('__all__')

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temas
        fields = ('__all__')