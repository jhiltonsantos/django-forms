# Generated by Django 3.1.2 on 2020-10-19 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201019_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='price',
        ),
    ]