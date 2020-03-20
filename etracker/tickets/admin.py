from django.contrib import admin
from .models import Ticket
from django.utils import timezone

admin.site.site_header = "ETracker Admin"
admin.site.site_title = "ETracker Admin"
admin.site.index_title = "Welcome to the ETracker admin area!"


class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "added_by",
                    "assignee", "date_updated", "date_added", )

    list_display_links = ("description", )

    list_filter = ("priority", "status", "assignee", )

    fields = ("status", "priority", "assignee", "description", "details", )

    search_fields = ("id", "description", "details",
                     "added_by__username", )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.added_by = request.user
        elif change:
            obj.date_updated = timezone.now()
        obj.save()


admin.site.register(Ticket, TicketAdmin)
