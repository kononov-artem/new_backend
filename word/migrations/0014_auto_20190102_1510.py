# Generated by Django 2.1.3 on 2019-01-02 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0013_auto_20190102_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionaries',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 2, 15, 10, 12, 296829)),
        ),
        migrations.AlterField(
            model_name='languages',
            name='language',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
