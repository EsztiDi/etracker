from django.contrib import admin
from .models import Ticket
from django.utils import timezone


class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "added_by",
                    "date_updated", "date_added")

    fields = ("status", "priority", "assignee", "description", "details")

    def save_model(self, request, obj, form, change):
        if not change:
            obj.added_by = request.user
        elif change:
            obj.date_updated = timezone.now()
        obj.save()


admin.site.register(Ticket, TicketAdmin)
