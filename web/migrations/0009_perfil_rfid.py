# Generated by Django 2.2.1 on 2019-05-25 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20190525_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='rfid',
            field=models.ManyToManyField(blank=True, to='web.rfid'),
        ),
    ]
