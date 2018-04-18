# Generated by Django 2.0.4 on 2018-04-17 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20180417_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='civilizacion',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.Civilizacion'),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]