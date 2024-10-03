from rest_framework import serializers
from .models import *

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = ('__all__')
class AutorIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Autores
        fields = ['id']
class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temas
        fields = ('__all__')
class TemaIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Temas
        fields = ['id']
class LibroSerializer(serializers.ModelSerializer):
    autor = AutorIdSerializer(many=True)
    nombreTema = TemaIdSerializer(many=True)

    class Meta:
        model = Libro
        fields = ('__all__')

    def create(self, validated_data):
        autor_data = validated_data.pop('autor')
        tema_data = validated_data.pop('nombreTema')
        libro = Libro.objects.create(**validated_data)
        for a in autor_data:
            autor = Autores.objects.get(id=a['id'])
            libro.autor.add(autor)
        for t in tema_data:
            tema = Temas.objects.get(id=t['id'])
            libro.nombreTema.add(tema)
        return libro