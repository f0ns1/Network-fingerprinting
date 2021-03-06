# Generated by Django 4.0.1 on 2022-02-09 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_defaultmodule_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortsModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=60)),
                ('target_ip', models.CharField(default='127.0.0.1', max_length=60)),
                ('time', models.DateTimeField(default=datetime.date(2022, 2, 9), max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='defaultmodule',
            name='target_ip',
            field=models.CharField(default='127.0.0.1', max_length=60),
        ),
        migrations.AlterField(
            model_name='defaultmodule',
            name='time',
            field=models.DateTimeField(default=datetime.date(2022, 2, 9), max_length=60),
        ),
    ]
