# Generated by Django 2.2.1 on 2019-05-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20190525_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='web',
        ),
        migrations.AddField(
            model_name='perfil',
            name='uid',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
