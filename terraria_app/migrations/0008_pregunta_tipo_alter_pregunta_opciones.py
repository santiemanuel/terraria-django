# Generated by Django 5.0 on 2023-12-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("terraria_app", "0007_sesioncuidado_respuestacuidado_sesion_cuidado"),
    ]

    operations = [
        migrations.AddField(
            model_name="pregunta",
            name="tipo",
            field=models.CharField(
                choices=[("opciones", "Opciones"), ("numerica", "Numérica")],
                default="opciones",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="pregunta",
            name="opciones",
            field=models.TextField(blank=True),
        ),
    ]
