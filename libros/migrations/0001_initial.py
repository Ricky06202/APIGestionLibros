# Generated by Django 5.1 on 2024-09-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Libro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200)),
                ("autor", models.CharField(max_length=200)),
                ("contenido", models.TextField()),
                ("esta_disponible", models.BooleanField(default=False)),
            ],
        ),
    ]