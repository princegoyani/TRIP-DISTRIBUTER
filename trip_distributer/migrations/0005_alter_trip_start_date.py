# Generated by Django 3.2.9 on 2021-12-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_distributer', '0004_auto_20211219_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
