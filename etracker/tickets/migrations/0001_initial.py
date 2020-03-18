# Generated by Django 3.0.4 on 2020-03-18 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'New'), ('2', 'In Progress'), ('3', 'Resolved'), ('4', 'Closed')], max_length=10)),
                ('priority', models.CharField(choices=[('1', 'Low'), ('2', 'Medium'), ('3', 'High')], max_length=10)),
                ('description', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('assignee', models.CharField(choices=[(0, 'EsztiDi'), (1, 'Guest')], max_length=255)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
