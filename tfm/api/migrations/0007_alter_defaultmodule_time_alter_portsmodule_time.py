# Generated by Django 4.0.1 on 2022-02-11 00:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_defaultmodule_time_alter_portsmodule_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultmodule',
            name='time',
            field=models.DateTimeField(default=datetime.date(2022, 2, 11), max_length=60),
        ),
        migrations.AlterField(
            model_name='portsmodule',
            name='time',
            field=models.DateTimeField(default=datetime.date(2022, 2, 11), max_length=60),
        ),
    ]
