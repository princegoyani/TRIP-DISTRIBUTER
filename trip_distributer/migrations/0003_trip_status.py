# Generated by Django 3.2.9 on 2021-12-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_distributer', '0002_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='status',
            field=models.CharField(default='current', max_length=20),
        ),
    ]