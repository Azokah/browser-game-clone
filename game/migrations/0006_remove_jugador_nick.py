# Generated by Django 2.0.4 on 2018-04-17 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_jugador_nick'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='nick',
        ),
    ]