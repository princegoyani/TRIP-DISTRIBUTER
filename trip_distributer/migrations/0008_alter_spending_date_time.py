# Generated by Django 3.2.9 on 2021-12-20 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_distributer', '0007_auto_20211220_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spending',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]