# Generated by Django 3.2.7 on 2021-10-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20211007_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(choices=[('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6)], verbose_name='doors'),
        ),
    ]
