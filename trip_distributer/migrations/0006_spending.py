# Generated by Django 3.2.9 on 2021-12-19 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip_distributer', '0005_alter_trip_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
                ('spend', models.IntegerField(null=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_spend', to='trip_distributer.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_spend', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
