from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {"fields": ("status", "priority", "description", "details", "assignee", "added_by")}), 
    ("Date Information", 
    {"classes": ("collapse",), 
    "fields": ("date_added", "date_updated")}),)
  readonly_fields = ("date_added", "date_updated", "added_by")

admin.site.register(Ticket, TicketAdmin)
