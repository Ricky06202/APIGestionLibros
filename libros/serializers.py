from rest_framework import serializers
from .models import *

class AutorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Autores
        fields = ('__all__')

class TemaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Temas
        fields = ('__all__')

class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(many=True)
    nombreTema = TemaSerializer(many=True)

    class Meta:
        model = Libro
        fields = ('__all__')

    def create(self, validated_data):
        autor_data = validated_data.pop('autor')
        tema_data = validated_data.pop('nombreTema')
        libro = Libro.objects.create(**validated_data)
        for a in autor_data:
            autor = Autores.objects.get(**a)
            print(autor)
            libro.autor.add(autor)
        for t in tema_data:
            tema = Temas.objects.get(**t)
            print(tema)
            libro.nombreTema.add(tema)
        return libro