# Generated by Django 3.0.4 on 2020-03-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20200319_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last updated'),
        ),
    ]
