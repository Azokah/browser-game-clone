# Generated by Django 2.0.4 on 2018-05-06 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_edificio'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificio',
            name='aldea',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='celdas', to='game.Aldea'),
            preserve_default=False,
        ),
    ]
