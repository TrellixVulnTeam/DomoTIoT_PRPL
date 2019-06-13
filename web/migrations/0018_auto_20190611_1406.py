# Generated by Django 2.2.1 on 2019-06-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20190611_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dht',
            field=models.ManyToManyField(blank=True, to='web.dht'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ldr',
            field=models.ManyToManyField(blank=True, to='web.ldr'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='led',
            field=models.ManyToManyField(blank=True, to='web.led'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mq2',
            field=models.ManyToManyField(blank=True, to='web.mq2'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='puerta',
            field=models.ManyToManyField(blank=True, to='web.puerta'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rfid',
            field=models.ManyToManyField(blank=True, to='web.rfid'),
        ),
    ]
