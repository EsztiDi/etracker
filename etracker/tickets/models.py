from django.db import models
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
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="assigned_tickets", limit_choices_to={"is_active": True}, blank=True, null=True)
    watchers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="watched_tickets")
    description = models.CharField(
        max_length=255, help_text="A short summary of the issue")
    details = models.TextField("More details")
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField("Last updated", blank=True, null=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="user_tickets", blank=True, null=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.description


class Comment(models.Model):
    text = models.TextField("Comment")
    date = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="user_comments", blank=True, null=True, verbose_name="User")
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.text
