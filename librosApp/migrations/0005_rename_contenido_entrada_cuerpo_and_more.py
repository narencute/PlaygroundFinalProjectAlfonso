# Generated by Django 4.2.4 on 2023-09-02 00:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('librosApp', '0004_mensaje_alter_entrada_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrada',
            old_name='contenido',
            new_name='cuerpo',
        ),
        migrations.RenameField(
            model_name='entrada',
            old_name='nombre',
            new_name='subtitulo',
        ),
        migrations.AddField(
            model_name='entrada',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entrada',
            name='titulo',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]