# Generated by Django 4.2.4 on 2023-08-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librosApp', '0002_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=models.TextField(max_length=1000),
        ),
    ]
