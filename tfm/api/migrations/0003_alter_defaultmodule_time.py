# Generated by Django 4.0.1 on 2022-01-30 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211224_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultmodule',
            name='time',
            field=models.DateTimeField(default=datetime.date(2022, 1, 30), max_length=60),
        ),
    ]
