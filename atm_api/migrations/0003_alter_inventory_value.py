# Generated by Django 3.2.6 on 2021-12-04 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm_api', '0002_auto_20211203_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='value',
            field=models.CharField(default='', max_length=5),
        ),
    ]