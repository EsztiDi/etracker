from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Ticket(models.Model):
    status_choices = [
        (0, "New"),
        (1, "In Progress"),
        (2, "Resolved"),
        (3, "Closed"),
    ]
    priority_choices = [
        (0, "Low"),
        (1, "Medium"),
        (2, "High"),
    ]

    users = User.objects.all().values_list("username", flat=True)

    assignee_choices = [
        (num, str(name)) for num, name in enumerate(users) if User.objects.get(username=str(name)).is_active
    ]

    status = models.IntegerField(
        choices=status_choices, blank=False, default=0)
    priority = models.IntegerField(
        choices=priority_choices, blank=False, default=0)
    description = models.CharField(
        max_length=255, help_text="A short summary of the issue")
    details = models.TextField(verbose_name="More details")
    assignee = models.IntegerField(choices=assignee_choices)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(
        default=date_added, verbose_name="Last updated")
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def update(self):
        self.date_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.status, self.priority, self.description, self.assignee, self.date_updated
