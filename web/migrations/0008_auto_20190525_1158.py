# Generated by Django 2.2.1 on 2019-05-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20190525_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='web',
        ),
        migrations.AddField(
            model_name='perfil',
            name='dht',
            field=models.ManyToManyField(blank=True, to='web.dht'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='uid',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
