# Generated by Django 3.0.4 on 2020-03-19 17:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20200319_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]