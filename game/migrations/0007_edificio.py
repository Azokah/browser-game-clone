# Generated by Django 2.0.4 on 2018-05-06 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_remove_celda_ocupada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]