# Generated by Django 5.0.2 on 2024-04-18 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0002_alter_reportero_options_alter_reportero_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportero',
            name='fecha_nacimiento',
            field=models.DateField(default='1900-01-01'),
        ),
    ]
