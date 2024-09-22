from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Temas(models.Model):
    nombre_tema = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_tema
    
class Autores(models.Model):
    nombre_autor = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_autor
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    autor = models.ManyToManyField(Autores)
    descripcion = models.TextField()
    link_portada = models.URLField(max_length=300, default='https://www.example.com', null=False, blank=True) 
    año_publicacion = models.PositiveBigIntegerField(default=0)
    editorial = models.CharField(max_length=200)
    paginas = models.PositiveBigIntegerField()
    nombreTema = models.ManyToManyField(Temas) 
    esta_disponible = models.BooleanField(default=False)
    precio = models.DecimalField(decimal_places=2, max_digits=15)
    link_referencia = models.URLField(max_length=300) 
    rating = models.DecimalField(decimal_places=2, max_digits=3, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])

    def __str__(self):
        return self.titulo

