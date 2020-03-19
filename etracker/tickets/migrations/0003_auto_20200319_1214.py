# Generated by Django 3.0.4 on 2020-03-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20200319_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')], default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'In Progress'), (2, 'Resolved'), (3, 'Closed')], default=0),
        ),
    ]
