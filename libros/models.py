from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    contenido = models.TextField()
    esta_disponible = models.BooleanField(default=False)
    def __str__(self):
        return self.name
