# Generated by Django 2.2.4 on 2019-08-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20190817_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='mq2',
            name='smokeMax',
            field=models.FloatField(default=0, null=True),
        ),
    ]