# Generated by Django 2.1.3 on 2019-01-02 11:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0011_auto_20180923_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionaries',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 2, 14, 57, 40, 653932)),
        ),
        migrations.AlterField(
            model_name='words',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='word.Languages'),
        ),
    ]
