# Generated by Django 2.1.3 on 2019-01-06 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0014_auto_20190102_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionaries',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dictionaries',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 7, 1, 6, 43, 499412)),
        ),
    ]