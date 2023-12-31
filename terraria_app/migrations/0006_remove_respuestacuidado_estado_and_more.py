# Generated by Django 5.0 on 2023-12-07 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("terraria_app", "0005_alter_respuestacuidado_respuesta"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="respuestacuidado",
            name="estado",
        ),
        migrations.RemoveField(
            model_name="respuestacuidado",
            name="orden",
        ),
        migrations.RemoveField(
            model_name="respuestacuidado",
            name="pregunta",
        ),
        migrations.RemoveField(
            model_name="respuestacuidado",
            name="registro_cuidado",
        ),
        migrations.CreateModel(
            name="PreguntaCuidado",
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
                ("orden", models.IntegerField()),
                (
                    "pregunta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="terraria_app.pregunta",
                    ),
                ),
                (
                    "registro_cuidado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="terraria_app.registrocuidado",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="respuestacuidado",
            name="pregunta_cuidado",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="terraria_app.preguntacuidado",
            ),
        ),
    ]
