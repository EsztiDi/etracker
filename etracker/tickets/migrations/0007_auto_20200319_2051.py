# Generated by Django 3.0.4 on 2020-03-19 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20200319_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assignee',
            field=models.IntegerField(choices=[(1, 'EsztiDi'), (2, 'Guest')]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'In Progress'), (3, 'Resolved'), (4, 'Closed')], default=1),
        ),
    ]