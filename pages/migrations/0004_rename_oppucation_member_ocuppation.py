# Generated by Django 3.2.7 on 2021-10-06 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20211006_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='oppucation',
            new_name='ocuppation',
        ),
    ]