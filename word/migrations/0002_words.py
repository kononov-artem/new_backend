# Generated by Django 2.1.1 on 2018-09-22 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('is_approve', models.BooleanField(default=False)),
                ('is_in_translate', models.BooleanField(default=False)),
            ],
        ),
    ]
