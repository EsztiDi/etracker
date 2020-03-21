from django.db import models
from django.utils import timezone
from django.conf import settings


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

    status = models.IntegerField(
        choices=status_choices, blank=False, default=1)
    priority = models.IntegerField(
        choices=priority_choices, blank=False, default=1)
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, limit_choices_to={"is_active": True},  related_name="assigned_tickets", blank=True, null=True)
    description = models.CharField(
        max_length=255, help_text="A short summary of the issue")
    details = models.TextField("More details")
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField("Last updated",
                                        blank=True, null=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="my_tickets")

    def update(self):
        self.date_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.description
