# Generated by Django 3.2.12 on 2024-06-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('blood_pressure_systolic', models.IntegerField(blank=True, null=True)),
                ('blood_pressure_diastolic', models.IntegerField(blank=True, null=True)),
                ('body_temperature', models.FloatField(blank=True, null=True)),
                ('heart_rate', models.IntegerField(blank=True, null=True)),
                ('respiratory_rate', models.IntegerField(blank=True, null=True)),
                ('blood_glucose_levels', models.FloatField(blank=True, null=True)),
                ('cholesterol_total', models.FloatField(blank=True, null=True)),
                ('cholesterol_hdl', models.FloatField(blank=True, null=True)),
                ('cholesterol_ldl', models.FloatField(blank=True, null=True)),
                ('cholesterol_triglycerides', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]