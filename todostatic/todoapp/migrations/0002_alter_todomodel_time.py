# Generated by Django 4.1.2 on 2022-11-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='time',
            field=models.DateField(),
        ),
    ]