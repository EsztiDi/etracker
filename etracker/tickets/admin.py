from django.contrib import admin
from .models import Ticket
from django.contrib.auth.models import User


class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "added_by",
                    "date_updated", "date_added")

    fieldsets = (
        (None, {"fields": ("status", "priority",
                           "description", "details", "assignee")}),
        ("Date Information",
            {"fields": ("date_added", "date_updated"), "classes": ("collapse",), }),)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.added_by = request.user
        obj.save()


admin.site.register(Ticket, TicketAdmin)
