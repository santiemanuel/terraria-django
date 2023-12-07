# Generated by Django 5.0 on 2023-12-07 21:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("terraria_app", "0006_remove_respuestacuidado_estado_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SesionCuidado",
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
                ("fecha_inicio", models.DateTimeField(auto_now_add=True)),
                ("fecha_finalizacion", models.DateTimeField(blank=True, null=True)),
                (
                    "registro_cuidado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="terraria_app.registrocuidado",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="respuestacuidado",
            name="sesion_cuidado",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="terraria_app.sesioncuidado",
            ),
            preserve_default=False,
        ),
    ]
