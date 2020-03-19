from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Ticket(models.Model):
    status_choices = [
        (1, "New"),
        (2, "In Progress"),
        (3, "Resolved"),
        (4, "Closed"),
    ]
    priority_choices = [
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
    ]

    users = User.objects.all().values_list("username", flat=True)

    assignee_choices = [
        (num, str(name)) for num, name in enumerate(users, 1) if User.objects.get(username=str(name)).is_active
    ]

    status = models.IntegerField(
        choices=status_choices, blank=False, default=1)
    priority = models.IntegerField(
        choices=priority_choices, blank=False, default=1)
    description = models.CharField(
        max_length=255, help_text="A short summary of the issue")
    details = models.TextField(verbose_name="More details")
    assignee = models.IntegerField(choices=assignee_choices)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(
        null=True, blank=True, verbose_name="Last updated")
    added_by = models.ForeignKey(
        User, on_delete=models.PROTECT)

    def update(self):
        self.date_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.description
