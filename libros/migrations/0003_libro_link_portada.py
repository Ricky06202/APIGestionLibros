# Generated by Django 5.1 on 2024-09-22 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libros", "0002_remove_libro_fecha_publicacion_libro_año_publicacion"),
    ]

    operations = [
        migrations.AddField(
            model_name="libro",
            name="link_portada",
            field=models.URLField(default=None, max_length=300),
        ),
    ]
