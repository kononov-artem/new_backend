# Generated by Django 2.1.3 on 2019-01-02 11:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0012_auto_20190102_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionaries',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 2, 14, 58, 10, 878541)),
        ),
        migrations.AlterField(
            model_name='words',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='word.Languages'),
        ),
    ]
