# Generated by Django 4.2.4 on 2023-08-27 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librosApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=500)),
                ('imagen', models.URLField()),
                ('autor', models.CharField(max_length=50)),
            ],
        ),
    ]
