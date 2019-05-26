# Generated by Django 2.2.1 on 2019-05-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_perfil_rfid'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='ldr',
            field=models.ManyToManyField(blank=True, to='web.ldr'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='led',
            field=models.ManyToManyField(blank=True, to='web.led'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='mq2',
            field=models.ManyToManyField(blank=True, to='web.mq2'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='puerta',
            field=models.ManyToManyField(blank=True, to='web.puerta'),
        ),
    ]
