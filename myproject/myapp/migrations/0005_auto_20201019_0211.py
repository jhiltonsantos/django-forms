# Generated by Django 3.1.2 on 2020-10-19 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20201019_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.CharField(max_length=2000),
        ),
    ]