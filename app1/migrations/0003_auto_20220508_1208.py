# Generated by Django 3.2.5 on 2022-05-08 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20220508_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='added_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='added_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='added_on',
            field=models.DateField(),
        ),
    ]
