# Generated by Django 5.1 on 2024-09-22 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libros", "0009_remove_libro_año_publicacion_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="libro",
            name="año_publicacion",
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="libro",
            name="link_portada",
            field=models.URLField(
                blank=True, default="https://www.example.com", max_length=300
            ),
        ),
    ]
