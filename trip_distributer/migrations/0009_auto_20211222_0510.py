# Generated by Django 3.2.9 on 2021-12-22 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_distributer', '0008_alter_spending_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateField(),
        ),
    ]
