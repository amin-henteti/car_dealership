# Generated by Django 3.2.7 on 2021-10-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='available',
            field=models.CharField(choices=[('For Rent', 'Rent'), ('For Sale', 'Sale'), ('Not avalable', 'Not avalable')], max_length=100, verbose_name='availibility'),
        ),
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], verbose_name='doors'),
        ),
        migrations.AlterField(
            model_name='car',
            name='passengers',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], verbose_name='year'),
        ),
    ]
