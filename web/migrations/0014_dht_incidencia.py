# Generated by Django 2.2.4 on 2019-08-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_incidenciadht'),
    ]

    operations = [
        migrations.AddField(
            model_name='dht',
            name='incidencia',
            field=models.BooleanField(default=False),
        ),
    ]