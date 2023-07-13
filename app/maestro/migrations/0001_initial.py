# Generated by Django 4.2.3 on 2023-07-09 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Institucion",
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
                ("nombre", models.CharField(max_length=255)),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("clinica", "Clínica"),
                            ("centro_medico", "Centro Médico"),
                            ("hospital_clinico", "Hospital Clínico"),
                            ("hospital", "Hospital"),
                            ("ces", "Centro de Salud"),
                            ("cesfam", "Centro de Salud Familiar"),
                            ("cecosf", "Centro Comunitario de Salud Familiar"),
                            ("psr", "Postas Salud Rural"),
                            ("sapu", "Servicio de Atención Primaria de Urgencia"),
                            (
                                "sar",
                                "Servicio de Atención Primaria de Urgencia de Alta Resolutividad",
                            ),
                            ("bodega", "Bodega"),
                            ("farmacia", "Farmacia"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "titularidad",
                    models.CharField(
                        choices=[("publico", "Público"), ("privado", "Privado")],
                        max_length=20,
                    ),
                ),
                (
                    "num_camas_uti",
                    models.PositiveSmallIntegerField(verbose_name="Número de Camas UTI"),
                ),
                (
                    "num_camas_uci",
                    models.PositiveSmallIntegerField(verbose_name="Número de Camas UCI"),
                ),
                ("factor", models.FloatField(help_text="Factor")),
            ],
            options={
                "verbose_name_plural": "Instituciones",
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                ("nombre", models.CharField(max_length=255)),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("soporte_vital", "Soporte Vital"),
                            ("apoyo_monitorizacion", "Apoyo y Monitorización"),
                        ],
                        max_length=32,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Medicamento",
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
                ("nombre_comercial", models.CharField(max_length=255)),
                (
                    "nombre_generico",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "ingredientes",
                    models.CharField(
                        help_text="Ingredientes químicos o sustancias activas presentes.",
                        max_length=255,
                    ),
                ),
                (
                    "concentracion",
                    models.CharField(
                        help_text="Cantidad de sustancia activa presente en cada unidad.",
                        max_length=255,
                    ),
                ),
                (
                    "forma_presentacion",
                    models.CharField(
                        choices=[
                            ("frasco", "Frasco"),
                            ("blister", "Blister"),
                            ("ampolla", "Ampolla"),
                        ],
                        max_length=16,
                    ),
                ),
                (
                    "forma_farmaceutica",
                    models.CharField(
                        choices=[
                            ("tabletas", "Tabletas"),
                            ("capsulas", "Cápsulas"),
                            ("solucion", "Solucion"),
                            ("crema", "Crema"),
                        ],
                        max_length=16,
                    ),
                ),
                (
                    "via_administracion",
                    models.CharField(
                        choices=[
                            ("oral", "Oral"),
                            ("topica", "Tópica"),
                            ("intravenoso", "Intravenoso"),
                            ("intramuscular", "Intramuscular"),
                        ],
                        max_length=16,
                    ),
                ),
                (
                    "indicaciones_terapeuticas",
                    models.CharField(
                        blank=True,
                        help_text="Condiciones o enfermedades para las cuales se prescribe.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "contraindicaciones",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "efectos_secundarios",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "instrucciones_dosificacion",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("fabricante", models.CharField(max_length=255)),
                (
                    "informacion_almacenamiento",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "interacciones_medicamentosas",
                    models.CharField(
                        blank=True,
                        help_text="Interacciones conocidas con otros medicamentos o sustencias.",
                        max_length=255,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Equipamiento",
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
                ("marca", models.CharField(max_length=255)),
                ("modelo", models.CharField(max_length=255)),
                (
                    "item",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="maestro.item"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Quiebre",
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
                ("cantidad", models.PositiveIntegerField(default=500)),
                (
                    "institucion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="maestro.institucion",
                    ),
                ),
                (
                    "medicamento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="maestro.medicamento",
                    ),
                ),
            ],
            options={
                "unique_together": {("institucion", "medicamento")},
            },
        ),
    ]
