# Generated by Django 2.0.4 on 2018-04-19 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aldea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('poblation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Celda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupada', models.BooleanField(default=False)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Civilizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, unique=True)),
                ('civilizacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.Civilizacion')),
            ],
        ),
        migrations.CreateModel(
            name='Mapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Patagonia', max_length=50)),
                ('width', models.IntegerField(default=20)),
                ('height', models.IntegerField(default=20)),
                ('mapSize', models.IntegerField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=250)),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emisor', to='game.Jugador')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to='game.Jugador')),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='celda',
            name='mapa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='celdas', to='game.Mapa'),
        ),
        migrations.AddField(
            model_name='aldea',
            name='jugador',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.Jugador'),
        ),
    ]