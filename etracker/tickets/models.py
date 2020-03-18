from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Ticket(models.Model):
  status_choices = [
    ("1", "New"),
    ("2", "In Progress"),
    ("3", "Resolved"),
    ("4", "Closed"),
  ]
  priority_choices = [
    ("1", "Low"),
    ("2", "Medium"),
    ("3", "High"),
  ]
  users = User.objects.all().values_list('username', flat=True)
  assignee_choices = [
    (num, name) for num, name in enumerate(users, 1) if User.objects.get(username=name).is_active
  ]

  status = models.CharField(max_length=10, choices=status_choices, blank=False, default="1")
  priority = models.CharField(max_length=10, choices=priority_choices, blank=False, default="1")
  description = models.CharField(max_length=255)
  details = models.TextField()
  assignee = models.CharField(max_length=255, choices=assignee_choices)
  date_added = models.DateTimeField(default=timezone.now)
  date_updated = models.DateTimeField(blank=True, null=True)
  added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

  def update(self):
    self.date_updated = timezone.now()
    self.save()

  def __str__(self):
    return self.status, self.priority, self.description, self.assignee

