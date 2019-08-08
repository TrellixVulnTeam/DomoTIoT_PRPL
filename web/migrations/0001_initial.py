# Generated by Django 2.2.4 on 2019-08-08 16:57

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=50, unique=True)),
                ('descripcion', models.CharField(default=None, max_length=250)),
                ('habitacion', models.CharField(default=None, max_length=250)),
                ('topic', models.CharField(default=None, max_length=50, unique=True)),
                ('tipo', models.CharField(choices=[('rfid', 'rfid'), ('dht', 'dht'), ('mq2', 'mq2'), ('ldr', 'ldr'), ('led', 'led'), ('puerta', 'puerta')], default=None, max_length=50)),
                ('codigoHogar', models.CharField(default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dht',
            fields=[
                ('modulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web.Modulo')),
                ('temperatura', models.FloatField(default=None, null=True)),
                ('humedad', models.FloatField(default=None, null=True)),
                ('temperaturaMax', models.FloatField(default=None, null=True)),
                ('humedadMax', models.FloatField(default=None, null=True)),
                ('fechaTMax', models.DateField(default=django.utils.timezone.now)),
                ('fechaHMax', models.DateField(default=django.utils.timezone.now)),
                ('horaTMax', models.TimeField(default=django.utils.timezone.now)),
                ('horaHMax', models.TimeField(default=django.utils.timezone.now)),
                ('temperaturaMin', models.FloatField(default=None, null=True)),
                ('humedadMin', models.FloatField(default=None, null=True)),
                ('fechaTMin', models.DateField(default=django.utils.timezone.now)),
                ('fechaHMin', models.DateField(default=django.utils.timezone.now)),
                ('horaTMin', models.TimeField(default=django.utils.timezone.now)),
                ('horaHMin', models.TimeField(default=django.utils.timezone.now)),
            ],
            bases=('web.modulo',),
        ),
        migrations.CreateModel(
            name='ldr',
            fields=[
                ('modulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web.Modulo')),
                ('luminosidad', models.FloatField(default=None, null=True)),
            ],
            bases=('web.modulo',),
        ),
        migrations.CreateModel(
            name='led',
            fields=[
                ('modulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web.Modulo')),
                ('nivel', models.IntegerField(default=0, null=True)),
            ],
            bases=('web.modulo',),
        ),
        migrations.CreateModel(
            name='mq2',
            fields=[
                ('modulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web.Modulo')),
                ('lpg', models.FloatField(default=None, null=True)),
                ('co2', models.FloatField(default=None, null=True)),
                ('smoke', models.FloatField(default=None, null=True)),
            ],
            bases=('web.modulo',),
        ),
        migrations.CreateModel(
            name='puerta',
            fields=[
                ('modulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web.Modulo')),
                ('estado', models.BooleanField(default=False)),
            ],
            bases=('web.modulo',),
        ),
        migrations.CreateModel(
            name='rfid',
            fields=[
                ('modulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web.Modulo')),
                ('uid', models.CharField(default=None, max_length=50, null=True)),
            ],
            bases=('web.modulo',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('codigoHogar', models.CharField(default=None, max_length=50, null=True)),
                ('uid', models.CharField(default=None, max_length=50, unique=True)),
                ('conectado', models.BooleanField(default=False)),
                ('dht', models.ManyToManyField(blank=True, to='web.dht')),
                ('ldr', models.ManyToManyField(blank=True, to='web.ldr')),
                ('led', models.ManyToManyField(blank=True, to='web.led')),
                ('mq2', models.ManyToManyField(blank=True, to='web.mq2')),
                ('puerta', models.ManyToManyField(blank=True, to='web.puerta')),
                ('rfid', models.ManyToManyField(blank=True, to='web.rfid')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
